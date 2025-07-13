import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import joblib
import time
import os

# Load model/tokenizer/encoder
MODEL_PATH = r"C:\Users\Lenovo\OneDrive - ueh.edu.vn\Documents\doan\cuoi_ky\app\phobert_model"
TOKENIZER_PATH = r"C:\Users\Lenovo\OneDrive - ueh.edu.vn\Documents\doan\cuoi_ky\app\phobert_tokenizer"
ENCODER_PATH = r"C:\Users\Lenovo\OneDrive - ueh.edu.vn\Documents\doan\cuoi_ky\app\label_encoder.pkl"
FEEDBACK_PATH = r"C:\Users\Lenovo\OneDrive - ueh.edu.vn\Documents\doan\cuoi_ky\app\feedback.csv"


model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH).to("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
encoder = joblib.load(ENCODER_PATH)

# Predict comment
def predict(text):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64).to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).cpu().numpy()[0]
    return encoder.inverse_transform([pred])[0]

# App UI
st.set_page_config(page_title="Vietnamese Sentiment Analysis", layout="wide")
st.title("📊 Sentiment Prediction App with PhoBERT")
st.markdown("Upload file CSV chứa cột `comment` để dự đoán cảm xúc (POS/NEU/NEG), trực quan và gửi phản hồi nếu cần.")

uploaded_file = st.file_uploader("📁 Chọn file CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "comment" not in df.columns:
        st.error("⚠️ File không có cột 'comment'")
    else:
        df = df.dropna(subset=['comment']).copy()
        df['prediction'] = df['comment'].apply(predict)

        st.success("✅ Đã phân loại xong")
        st.dataframe(df.head())

        # ==== Visualization Layout ====
        st.subheader("📈 Phân phối cảm xúc")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.countplot(x='prediction', data=df, ax=ax, palette='pastel')
            ax.set_title("Bar Chart")
            st.pyplot(fig)

        with col2:
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            df['prediction'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2, colors=sns.color_palette('pastel'))
            ax2.set_ylabel("")
            ax2.set_title("Pie Chart")
            st.pyplot(fig2)

        st.subheader("☁️ WordCloud theo nhãn")

        labels = df['prediction'].unique()
        cols = st.columns(2)

        for idx, label in enumerate(labels):
            text = " ".join(df[df['prediction'] == label]['comment'].astype(str))
            wordcloud = WordCloud(width=600, height=300, background_color="white").generate(text)
            with cols[idx % 2]:
                st.markdown(f"**{label}**")
                fig_wc, ax_wc = plt.subplots(figsize=(6, 3))
                ax_wc.imshow(wordcloud, interpolation='bilinear')
                ax_wc.axis('off')
                st.pyplot(fig_wc)

        # Download
        st.subheader("📥 Tải kết quả")
        st.download_button("💾 Tải file kết quả", df.to_csv(index=False).encode('utf-8'), file_name="prediction_results.csv")

        # Feedback UI
        st.subheader("✏️ Góp ý nhãn dự đoán")
        for idx, row in df.iterrows():
            with st.expander(f"📌 Dòng {idx}: {row['comment'][:60]}..."):
                st.write(f"**Dự đoán:** {row['prediction']}")
                correct = st.selectbox("Chọn nhãn đúng:", encoder.classes_, key=f"select_{idx}")
                if st.button("📩 Gửi phản hồi", key=f"send_{idx}"):
                    fb = pd.DataFrame([{
                        "index": idx,
                        "comment": row['comment'],
                        "model_prediction": row['prediction'],
                        "correct_label": correct,
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }])
                    if os.path.exists(FEEDBACK_PATH):
                        fb.to_csv(FEEDBACK_PATH, mode="a", index=False, header=False)
                    else:
                        fb.to_csv(FEEDBACK_PATH, index=False)
                    st.success("✅ Phản hồi đã được ghi nhận")

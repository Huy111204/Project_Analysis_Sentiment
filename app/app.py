import os
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import joblib
import time
from google_sheets import append_feedback_to_gsheet

# ===== Cấu hình đường dẫn =====
MODEL_REPO = "Huy111204/phobert-vietnamese-sentiment"
TOKENIZER_REPO = "Huy111204/phobert-vietnamese-sentiment"
# Đảm bảo đúng đường dẫn dù chạy ở đâu
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ENCODER_PATH = os.path.join(APP_DIR, "label_encoder.pkl")

# ===== Load model & tokenizer & encoder =====
@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_REPO)
    return model.to("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained(TOKENIZER_REPO)

@st.cache_resource
def load_encoder():
    if not os.path.exists(ENCODER_PATH):
        url = "https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/resolve/main/label_encoder.pkl"
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f"Lỗi tải encoder từ Hugging Face: {response.status_code}")
        with open(ENCODER_PATH, "wb") as f:
            f.write(response.content)
    return joblib.load(ENCODER_PATH)

model = load_model()
tokenizer = load_tokenizer()
encoder = load_encoder()

# ===== Dự đoán cảm xúc (có cache) =====
@st.cache_data(show_spinner=False)
def predict(text):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64).to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).cpu().numpy()[0]
    return encoder.inverse_transform([pred])[0]

# ===== Giao diện Streamlit =====
st.set_page_config(page_title="Vietnamese Sentiment Analysis", layout="wide")
st.title("📊 Sentiment Prediction App with PhoBERT")
st.markdown("Upload file CSV chứa cột `comment` để dự đoán cảm xúc (POS/NEU/NEG), trực quan và gửi phản hồi nếu cần.")

uploaded_file = st.file_uploader("📁 Chọn file CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8-sig")
        except Exception as e:
            st.error(f"❌ Lỗi đọc file: {e}")
            st.stop()

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

        # ==== WordCloud ====
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

        # ==== Tải kết quả ====
        st.subheader("📥 Tải kết quả")
        st.download_button("💾 Tải file kết quả", df.to_csv(index=False).encode('utf-8'), file_name="prediction_results.csv")

        # ==== Góp ý người dùng ====
        st.subheader("✏️ Góp ý nhãn dự đoán")
        max_feedback = 50  # tránh spam
        for idx, row in df.head(max_feedback).iterrows():
            with st.expander(f"📌 Dòng {idx}: {row['comment'][:60]}..."):
                st.write(f"**Dự đoán:** {row['prediction']}")
                correct = st.selectbox("Chọn nhãn đúng:", encoder.classes_, key=f"select_{idx}")
                if st.button("📩 Gửi phản hồi", key=f"send_{idx}"):
                    feedback_data = {
                        "comment": row["comment"],
                        "model_prediction": row["prediction"],
                        "correct_label": correct,
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    success = append_feedback_to_gsheet(feedback_data)
                    if success:
                        st.success("✅ Phản hồi đã được ghi nhận")
                    else:
                        st.error("❌ Không thể ghi phản hồi lên Google Sheets")

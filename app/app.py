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

# === Load mô hình, tokenizer và label encoder từ Hugging Face ===
@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained("Huy111204/phobert-vietnamese-sentiment")
    return model.to("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("Huy111204/phobert-vietnamese-sentiment/tokenizer")

@st.cache_data
def load_encoder():
    from huggingface_hub import hf_hub_download
    encoder_path = hf_hub_download(repo_id="Huy111204/phobert-vietnamese-sentiment", filename="label_encoder.pkl")
    return joblib.load(encoder_path)

model = load_model()
tokenizer = load_tokenizer()
encoder = load_encoder()

# === Dự đoán cảm xúc ===
def predict(text):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64).to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).cpu().numpy()[0]
    return encoder.inverse_transform([pred])[0]

# === Giao diện Streamlit ===
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

        # Download kết quả
        st.subheader("📥 Tải kết quả")
        st.download_button("💾 Tải file kết quả", df.to_csv(index=False).encode('utf-8'), file_name="prediction_results.csv")

import os
import gdown
import zipfile
import streamlit as st

def download_file_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    st.write(f"📥 Đang tải file từ Google Drive: `{output_path}`")
    gdown.download(url, output_path, quiet=False)

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)
    st.write(f"✅ Đã giải nén vào `{extract_to}`")

def download_all_files():
    # === 1. PhoBERT model ===
    model_path = "app/phobert_model/config.json"
    if not os.path.exists(model_path):
        st.write("📥 Tải mô hình PhoBERT...")
        download_file_from_drive("14rWQSdiZLV0ig_Bm_3V7mtCxfj31Tb9j", "phobert_model.zip")
        unzip_file("phobert_model.zip", "app/")
    else:
        st.write("✅ Đã có model PhoBERT.")

    # === 2. Tokenizer ===
    tokenizer_path = "app/phobert_tokenizer/tokenizer_config.json"
    if not os.path.exists(tokenizer_path):
        st.write("📥 Tải tokenizer...")
        download_file_from_drive("1qn6Q9CcD0TLHAJtOlKVQvJnlh1r-4xv3", "phobert_tokenizer.zip")
        unzip_file("phobert_tokenizer.zip", "app/")
    else:
        st.write("✅ Đã có tokenizer.")

    # === 3. Label encoder ===
    if not os.path.exists("app/label_encoder.pkl"):
        st.write("📥 Tải label_encoder.pkl...")
        download_file_from_drive("1Orf15r3YuE7jO5zYxtpiIwzZVWwWKxAx", "app/label_encoder.pkl")
        st.write("✅ Tải label_encoder.pkl xong.")
    else:
        st.write("✅ Đã có label_encoder.pkl.")

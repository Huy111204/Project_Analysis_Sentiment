"""import os
import gdown
import streamlit as st

def download_file_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    st.write(f"📥 Đang tải file: `{output_path}`")
    gdown.download(url, output_path, quiet=False)

def download_all_files():
    os.makedirs("app/phobert_model", exist_ok=True)
    os.makedirs("app/phobert_tokenizer", exist_ok=True)

    # === 1. PhoBERT model ===
    model_files = {
        "config.json": "1cwQ0A6M7mcQLPvXtMcWWKadFegy1o9ke",
        "model.safetensors": "14MlFhFB1Ylm-gOIyT_O2heRDl88HkDlM"  # <-- bạn cần cập nhật đúng file_id nếu khác
    }

    for filename, file_id in model_files.items():
        dest_path = f"app/phobert_model/{filename}"
        if not os.path.exists(dest_path):
            download_file_from_drive(file_id, dest_path)
        else:
            st.write(f"✅ Đã có `{filename}` trong phobert_model")

    # === 2. Tokenizer ===
    tokenizer_files = {
        "tokenizer_config.json": "1_FZMdpv03bMSaa4OTff_y9AuRBc-ccaF",
        "vocab.txt": "1V8WOHrg41shDPuNecZZeGFagTiVmmaec",
        "special_tokens_map.json": "1XKmyRvW8DAe2wDJg2qB8m7m9Z_HxBCYt",
        "added_tokens.json": "1ioW2d-TQCM301ypHgPfcJ_eSO6zNIbv2"  # Nếu có
    }

    for filename, file_id in tokenizer_files.items():
        dest_path = f"app/phobert_tokenizer/{filename}"
        if not os.path.exists(dest_path):
            download_file_from_drive(file_id, dest_path)
        else:
            st.write(f"✅ Đã có `{filename}` trong phobert_tokenizer")

    # === 3. Label encoder ===
    encoder_path = "app/label_encoder.pkl"
    if not os.path.exists(encoder_path):
        st.write("📥 Tải label_encoder.pkl...")
        download_file_from_drive("1Orf15r3YuE7jO5zYxtpiIwzZVWwWKxAx", encoder_path)
        st.write("✅ Đã tải xong label_encoder.pkl")
    else:
        st.write("✅ Đã có label_encoder.pkl")"""

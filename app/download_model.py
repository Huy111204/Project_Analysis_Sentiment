import os
import gdown
import zipfile

def download_file_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)

def download_all_files():
    if not os.path.exists("app/phobert_model"):
        print("📥 Downloading phobert_model...")
        download_file_from_drive("1zbrVlPPHrq899Azqf8w-sddGJb51g77b", "phobert_model.zip")
        unzip_file("phobert_model.zip", "app/")

    if not os.path.exists("app/phobert_tokenizer"):
        print("📥 Downloading tokenizer...")
        download_file_from_drive("1k3l2DEBfPqAA2d1ye_OzBjM1K7eSCUpo", "phobert_tokenizer.zip")
        unzip_file("phobert_tokenizer.zip", "app/")

    if not os.path.exists("app/label_encoder.pkl"):
        print("📥 Downloading label_encoder.pkl...")
        download_file_from_drive("1Orf15r3YuE7jO5zYxtpiIwzZVWwWKxAx", "app/label_encoder.pkl")

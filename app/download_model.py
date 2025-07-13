import gdown
import zipfile
import os

def download_and_extract(id, output_dir, zip_name):
    if not os.path.exists(output_dir):
        zip_path = f"{zip_name}.zip"
        url = f"https://drive.google.com/uc?id={id}"
        gdown.download(url, zip_path, quiet=False)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)
        os.remove(zip_path)

def download_file(file_id, output_path):
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)

# Tải model & tokenizer
download_and_extract("1zbrVlPPHrq899Azqf8w-sddGJb51g77b", "app/phobert_model", "phobert_model")
download_and_extract("1k3l2DEBfPqAA2d1ye_OzBjM1K7eSCUpo", "app/phobert_tokenizer", "phobert_tokenizer")

# Tải label encoder
download_file("1Orf15r3YuE7jO5zYxtpiIwzZVWwWKxAx", "app/label_encoder.pkl")

<!-- Badges -->
[![Streamlit](https://img.shields.io/badge/Streamlit-deployed-brightgreen?logo=streamlit)](https://projectanalysissentiment.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13.5-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](https://github.com/Huy111204/Project_Analysis_Sentiment/blob/main/LICENSE)

# 🧠 Sentiment Analysis Web App with PhoBERT

Ứng dụng **Streamlit** giúp bạn:
- Tải lên file CSV có cột `comment`
- Dự đoán cảm xúc (`POS`, `NEU`, `NEG`) bằng mô hình **PhoBERT**
- Trực quan hóa kết quả qua biểu đồ cột, biểu đồ tròn và WordCloud
- Gửi phản hồi khi mô hình dự đoán sai
- Tự động lưu phản hồi trên **Google Sheets** để liên tục cải tiến

---

## 🚀Truy cập ứng dụng online
**Dùng thử ngay tại đây:**  
🔗 [https://projectanalysissentiment.streamlit.app](https://projectanalysissentiment.streamlit.app/)

---

## 📦 Các tài nguyên cần thiết cho mô hình
Ứng dụng sử dụng mô hình huấn luyện sẵn được lưu trữ tại Hugging Face:  
**Hugging Face Repo:** [Huy111204/phobert-vietnamese-sentiment](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)

Bao gồm:
- `model.safetensors`,`config.json` (phobert_model)
- `tokenizer_config.json`, `vocab.txt`, `special_tokens_map.json`,`bpe.codes`,`added_tokens.json` (phobert_tokenizer)
- `label_encoder.pkl` (mã hóa nhãn cảm xúc)

Tất cả tài nguyên có đầy đủ trên HuggingFace bạn có thể tải đầy đủ về để chạy trên local 

---

## 📊 Phản hồi người dùng

Người dùng có thể gửi phản hồi về nhãn dự đoán sai. Dữ liệu được lưu tại:  
📄 [Google Sheet - Góp ý nhãn](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?gid=0#gid=0)

---

## 🛠️ Cài đặt & chạy cục bộ
Người dùng vào link drive : (https://drive.google.com/drive/folders/1LTQgY2lwTtc_aeSQaTrPC8XnNPaLTfLm?usp=sharing)
Vào thư mục app download về máy 
Mở cmd hoặc windows PowerShell
```bash
# Cài đặt thư viện cần thiết
pip install -r requirements.txt
# Đưa tới thư mục app 
cd "Path" #Thay Path bằng đường dẫn tới thư mục app vừa tải ví dụ cd "F:\app"
# Chạy ứng dụng Streamlit
streamlit run app.py

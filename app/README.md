
[![Streamlit](https://img.shields.io/badge/Streamlit-deployed-brightgreen?logo=streamlit)](https://projectanalysissentiment.streamlit.app)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Model%20Storage-blue?logo=google-drive)](https://drive.google.com/drive/folders/1LTQgY2lwTtc_aeSQaTrPC8XnNPaLTfLm?usp=sharing)
[![HuggingFace Model](https://img.shields.io/badge/HuggingFace-phobert--vietnamese--sentiment-orange?logo=huggingface)](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)
[![Sentiment Feedback](https://img.shields.io/badge/Feedback-Google%20Sheets-yellow?logo=googlesheets)](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?usp=sharing)


# 🧠 Sentiment Analysis Web App with PhoBERT

Ứng dụng **Streamlit** giúp bạn:
- Tải lên file CSV có cột `comment`
- Dự đoán cảm xúc (`POS`, `NEU`, `NEG`) bằng mô hình **PhoBERT**
- Trực quan hóa kết quả qua biểu đồ cột, biểu đồ tròn và WordCloud
- Gửi phản hồi khi mô hình dự đoán sai
- Tự động lưu phản hồi trên **Google Sheets** để liên tục cải tiến
<img width="1919" height="893" alt="image" src="https://github.com/user-attachments/assets/8c2d6a42-f04f-47f4-81c6-9125e4c5659e" />
<img width="1919" height="935" alt="image" src="https://github.com/user-attachments/assets/cffd93a0-55ff-420b-a0ca-8ae755e0b6ab" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6458481b-cf74-4b43-bbc9-8c94c022c846" />
<img width="1919" height="723" alt="image" src="https://github.com/user-attachments/assets/5c97432b-a39f-4724-84a3-bb41d8fb1ae3" />

---

## Các tài nguyên cần thiết cho mô hình

**Hugging Face Repo:** [Huy111204/phobert-vietnamese-sentiment](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)

- `model.safetensors`,`config.json` (phobert_model)
- `tokenizer_config.json`, `vocab.txt`, `special_tokens_map.json`,`bpe.codes`,`added_tokens.json` (phobert_tokenizer)
- `label_encoder.pkl` (mã hóa nhãn cảm xúc)

---

## Phản hồi người dùng

Người dùng có thể gửi phản hồi về nhãn dự đoán sai khi truy cập ứng dụng online. Dữ liệu được lưu tại:  
📄 [Google Sheet - Góp ý nhãn](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?gid=0#gid=0)

---

## To use
link drive : (https://drive.google.com/drive/folders/1LTQgY2lwTtc_aeSQaTrPC8XnNPaLTfLm?usp=sharing)
- Open app and download 
- Terminal
```bash
# requirements
pip install -r requirements.txt

cd "Path" #Thay Path bằng đường dẫn tới thư mục app vừa tải ví dụ cd "F:\app"

# Run Streamlit
streamlit run app.py


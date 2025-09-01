# Vietnamese Sentiment Analysis from E-Commerce Comments

<!-- Badges -->
[![HuggingFace Model](https://img.shields.io/badge/HuggingFace-phobert--vietnamese--sentiment-orange?logo=huggingface)](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)
[![W&B: Traditional ML](https://img.shields.io/badge/W%26B-Traditional%20ML-yellow?logo=wandb)](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)
[![W&B: PhoBERT Fine-tune](https://img.shields.io/badge/W%26B-PhoBERT%20Fine--tune-red?logo=wandb)](https://api.wandb.ai/links/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Model%20Storage-blue?logo=google-drive)](https://drive.google.com/drive/folders/1LTQgY2lwTtc_aeSQaTrPC8XnNPaLTfLm?usp=sharing)
[![Sentiment Feedback](https://img.shields.io/badge/Feedback-Google%20Sheets-yellow?logo=googlesheets)](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?usp=sharing)


---
## Features
<img width="927" height="614" alt="image" src="https://github.com/user-attachments/assets/090c0ae5-edbe-4b8d-a6b1-374cd5e2fe4a" />

Key Features

Data collection from Sendo.vn using Selenium.

Text preprocessing: lowercase conversion, normalization (URLs, numbers, emojis), tokenization (via underthesea), stopword removal.

Comparative evaluation of traditional ML models: Logistic Regression, Linear SVM, and Multinomial Naive Bayes, with TF-IDF vectorization and metrics like Accuracy, F1-score, Precision, Recall, and Confusion Matrix.

Fine-tuning of PhoBERT (base model from wonrax/phobert-base-vietnamese-sentiment) on the processed dataset. Model and tokenizer uploaded to Hugging Face.

Interactive Streamlit app: upload CSV (with comment column), visualize results via bar charts, pie charts, word clouds, download predictions, and collect user feedback.

Continuous learning loop: user-corrected labels via feedback are saved to Google Sheets for model enhancement.
---
## Tổng quan

Pipeline phân tích cảm xúc từ bình luận thương mại điện tử tiếng Việt, bao gồm:

### 1. **Crawl & Tiền xử lý dữ liệu**
   - Crawl dữ liệu từ Sendo.vn bằng Selenium    
   - Tiền xử lý: chuyển chữ thường, chuẩn hoá biểu thức đặc biệt (URL, số, emoji), token hóa bằng `underthesea`, loại bỏ stopwords  

### 2. **So sánh mô hình truyền thống**
   - Các mô hình: **Logistic Regression**, **Linear SVM**, **Multinomial Naive Bayes**
   - - Vector hóa bằng **TF-IDF**
   - Đánh giá bằng: `Accuracy`, `F1-score`, `Precision`, `Recall`, `Confusion Matrix`  
      [🔗 Xem báo cáo W&B](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)

### 3. **Fine-tune PhoBERT**
   - Mô hình gốc: [`wonrax/phobert-base-vietnamese-sentiment`](https://huggingface.co/wonrax/phobert-base-vietnamese-sentiment)
   - Fine-tune mô hình wonrax/phobert-base-vietnamese-sentiment trên tập dữ liệu đã tiền xử lý, sử dụng Hugging Face Trainer, token hóa, huấn luyện. 
   - Lưu model & tokenizer lên Hugging Face
   - Đánh giá bằng Hugging Face `Trainer`    
      [🔗Xem báo cáo trên W&B](https://api.wandb.ai/links/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)  
      [🔗Model trên Hugging Face](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)

### 4. **Ứng dụng Streamlit** 
   - Upload file CSV có cột `comment` để phân tích cảm xúc (POS/NEU/NEG)
   - Visualize bằng Bar chart, Pie chart, WordCloud  
   - Cho phép người dùng tải kết quả `.csv` sau khi dự đoán 
   - Feedback UI: người dùng đánh giá lại nhãn → lưu trực tiếp lên Google Sheets 
      [🔗 App]([https://projectanalysissentiment.streamlit.app](https://projectanalysissentiment.streamlit.app/))

### 5. **Phản hồi & Continuous Learning** 
   - Ghi nhận phản hồi nhãn đúng từ người dùng (qua giao diện Streamlit)
   - Dữ liệu feedback được lưu vào:  
      [🔗 Google Sheets Feedback](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?usp=sharing)

---

## Cấu trúc thư mục

```bash
Project_Analysis_Sentiment/
├── crawl_data_sendo/            # thu thập data sendo 
│   └── ...
├── train_model/                 # Xây dựng mô hình Logistic Regression , SVM , Naive Bayes và phobert được Fine‑tune bởi wonrax
│   ├── ...                     
├── app/                         # Ứng dụng Streamlit
│   ├── app.py                   # Logic chính của app
│   ├── google_sheets.py         # Ghi feedback lên Google Sheets
│   ├── requirements.txt         # Dependencies cho app
│   └── README.md                # Hướng dẫn phần app trên streamlit và cách chạy app cục bộ
│   ├── ... 
├── .gitignore
└── README.md                    # # File hiện tại

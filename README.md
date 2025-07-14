# 📊 Vietnamese Sentiment Analysis from E-Commerce Comments

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue?logo=streamlit)](https://projectanalysissentiment.streamlit.app)  
[![HuggingFace Model](https://img.shields.io/badge/HuggingFace-phobert--vietnamese--sentiment-orange?logo=huggingface)](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)  
[![W&B: Traditional ML](https://img.shields.io/badge/W%26B-Traditional%20ML-yellow?logo=wandb)](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)  
[![W&B: PhoBERT Fine-tune](https://img.shields.io/badge/W%26B-PhoBERT%20Fine--tune-red?logo=wandb)](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)

---
## ✨ Features

-  Thu thập dữ liệu cảm xúc từ Sendo.vn
-  Tiền xử lý dữ liệu văn bản
-  So sánh 3 mô hình ML truyền thống: Logistic Regression, SVM, Naive Bayes
-  Fine-tune mô hình PhoBERT cho tiếng Việt
-  Giao diện Streamlit: Dự đoán & phân tích cảm xúc từ file CSV ( có cột comment)
-  Thu thập phản hồi người dùng qua Google Sheets
-  Báo cáo chi tiết mô hình qua Weights & Biases
---
## 🔥 Tổng quan

Pipeline phân tích cảm xúc từ bình luận thương mại điện tử tiếng Việt, bao gồm:

### 1. **Crawl & Tiền xử lý dữ liệu**
   - Crawl dữ liệu từ Sendo.vn bằng Selenium    
   - Tiền xử lý: chuyển chữ thường, chuẩn hoá biểu thức đặc biệt (URL, số, emoji), token hóa bằng `underthesea`, loại bỏ stopwords  

### 2. **So sánh mô hình truyền thống**
   - Các mô hình: **Logistic Regression**, **Linear SVM**, **Multinomial Naive Bayes**
   - - Vector hóa bằng **TF-IDF**
   - Đánh giá bằng: `Accuracy`, `F1-score`, `Precision`, `Recall`, `Confusion Matrix`  
   👉 [🔗 Xem báo cáo W&B](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)

### 3. **Fine-tune PhoBERT**
   - Mô hình gốc: [`wonrax/phobert-base-vietnamese-sentiment`](https://huggingface.co/wonrax/phobert-base-vietnamese-sentiment)
   - Fine-tune mô hình wonrax/phobert-base-vietnamese-sentiment trên tập dữ liệu đã tiền xử lý, sử dụng Hugging Face Trainer, token hóa, huấn luyện. 
   - Lưu model & tokenizer lên Hugging Face
   - Đánh giá bằng Hugging Face `Trainer`    
   👉 [🔗Xem báo cáo trên W&B](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)  
   👉 [🔗Model trên Hugging Face](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment)

4. **Streamlit App**:  
   - Upload CSV có cột `comment` → dự đoán POS/NEU/NEG  
   - Trực quan hoá: bar chart, pie chart, WordCloud  
   - Download kết quả `.csv`  
   - Feedback UI: người dùng đánh giá lại nhãn sai, ghi thẳng vào Google Sheets  
   👉 [🔗 App]([https://projectanalysissentiment.streamlit.app](https://projectanalysissentiment.streamlit.app/))

5. **Feedback & Continuous Learning**:  
   - Tất cả phản hồi nhãn đúng được ghi vào Google Sheets  
   👉 [🔗 Google Sheets Feedback](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?usp=sharing)

---

## 🗂️ Cấu trúc thư mục

```bash
Project_Analysis_Sentiment/
├── crawl_data_sendo/            # thu thập data sendo 
│   └── ...
├── train_model/                 # Xây dựng mô hình Logistic Regression , SVM , Naive Bayes và phobert được Fine‑tune bởi wonrax
│   ├── ...                     
├── app/                         # Ứng dụng Streamlit
│   ├── app.py                   # Logic chính
│   ├── google_sheets.py         # Ghi feedback lên Google Sheets
│   ├── requirements.txt         # Dependencies cho app
│   └── README.md                # Hướng dẫn phần app trên streamlit và cách chạy app cục bộ
├── .gitignore
└── README.md                    # File này

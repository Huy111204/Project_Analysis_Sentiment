# 📊 Project Analysis Sentiment 

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue?logo=streamlit)](https://projectanalysissentiment.streamlit.app)  
[![HuggingFace Model](https://img.shields.io/badge/HuggingFace-phobert--vietnamese--sentiment-orange?logo=huggingface)](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)  
[![W&B Report](https://img.shields.io/badge/W%26B-ML_vs_PhoBERT-violet?logo=wandb)
[![W&B Report](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)  

---

## 🔥 Tổng quan

Dự án này thực hiện pipeline phân tích cảm xúc từ bình luận tiếng Việt (thu thập chủ yếu từ Sendo.vn), bao gồm:

1. **Crawl & Tiền xử lý**:  
   - Dùng Selenium thu thập   
   - Chuẩn hoá, loại bỏ stopwords, tokenization

2. **So sánh mô hình ML truyền thống**:  
   - Logistic Regression , SVM , Naive Bayes  
   - Feature: TF‑IDF 
   - Báo cáo full metrics (accuracy, F1‑score, confusion matrix) trên Weights & Biases  
   👉 [🔗 Xem báo cáo W&B](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)

3. **Fine‑tune PhoBERT**:  
   - Base model: `wonrax/phobert-base-vietnamese-sentiment`  
   - Tập dữ liệu đã tiền xử lý  
   - Lưu model & tokenizer lên Hugging Face  
   👉 [🔗 Repository HF](https://api.wandb.ai/links/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)

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

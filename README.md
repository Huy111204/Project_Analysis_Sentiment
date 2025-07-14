# 📊 Project Analysis Sentiment – Vietnamese E‑Commerce Reviews

![Streamlit](https://img.shields.io/badge/Streamlit‑app-blue) ![HuggingFace](https://img.shields.io/badge/HuggingFace‑model-orange) ![W&B](https://img.shields.io/badge/W%26B‑report‑violet)

---

## 🔥 Tổng quan

Dự án này thực hiện pipeline phân tích cảm xúc từ bình luận tiếng Việt (thu thập chủ yếu từ Sendo.vn), bao gồm:

1. **Crawl & Tiền xử lý**:  
   - Dùng Selenium thu thập raw data  
   - Chuẩn hoá, loại bỏ stopwords, tokenization

2. **So sánh mô hình ML truyền thống**:  
   - Logistic Regression, Naive Bayes, SVM  
   - Feature: TF‑IDF, CountVectorizer  
   - Báo cáo full metrics (accuracy, F1‑score, confusion matrix) trên Weights & Biases  
   👉 [🔗 Xem báo cáo W&B](https://wandb.ai/your‑username/your‑project)

3. **Fine‑tune PhoBERT**:  
   - Base model: `vinai/phobert-base`  
   - Tập dữ liệu đã tiền xử lý  
   - Lưu model & tokenizer lên Hugging Face  
   👉 [🔗 Repository HF](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment)

4. **Streamlit App**:  
   - Upload CSV có cột `comment` → dự đoán POS/NEU/NEG  
   - Trực quan hoá: bar chart, pie chart, WordCloud  
   - Download kết quả `.csv`  
   - Feedback UI: người dùng đánh giá lại nhãn sai, ghi thẳng vào Google Sheets  
   👉 [🔗 Live App](https://projectanalysissentiment.streamlit.app)

5. **Feedback & Continuous Learning**:  
   - Tất cả phản hồi nhãn đúng được ghi vào Google Sheets  
   👉 [🔗 Google Sheets Feedback](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg)

---

## 🗂️ Cấu trúc thư mục

```bash
Project_Analysis_Sentiment/
├── crawl_data_sendo/            # Script thu thập & tiền xử lý data
│   └── ...
├── train_model/                 # So sánh các mô hình ML & PhoBERT fine‑tune
│   ├── experiments/             # configs & logs W&B
│   └── train_phobert.py
├── app/                         # Ứng dụng Streamlit
│   ├── app.py                   # Logic chính
│   ├── google_sheets.py         # Ghi feedback lên Google Sheets
│   ├── requirements.txt         # Thư viện cần thiết
│   └── README.md                # Hướng dẫn phần app
├── .gitignore
├── requirements‑base.txt        # Thư viện chung (crawl + train)
└── README.md                    # File này

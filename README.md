# Vietnamese Sentiment Analysis from E-Commerce Comments

<!-- Badges -->
[![HuggingFace Model](https://img.shields.io/badge/HuggingFace-phobert--vietnamese--sentiment-orange?logo=huggingface)](https://huggingface.co/Huy111204/phobert-vietnamese-sentiment/tree/main)
[![W&B: Traditional ML](https://img.shields.io/badge/W%26B-Traditional%20ML-yellow?logo=wandb)](https://wandb.ai/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/traditional_ml-vs-phobert/reports/So-s-nh-hi-u-su-t-c-c-m-h-nh-Machine-Learning-trong-ph-n-lo-i-c-m-x-c-ti-ng-Vi-t--VmlldzoxMzU2MTAxNA?accessToken=a01w3r7vp17l89ogcpiffnhbe18g68fe5wa437jfxin4o2z0v1g2yr4wmp6a24lu)
[![W&B: PhoBERT Fine-tune](https://img.shields.io/badge/W%26B-PhoBERT%20Fine--tune-red?logo=wandb)](https://api.wandb.ai/links/hoanghuytp9-7-tr-ng-h-kinh-t-tp-h-ch-minh-ueh/yvq0mzam)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Model%20Storage-blue?logo=google-drive)](https://drive.google.com/drive/folders/1LTQgY2lwTtc_aeSQaTrPC8XnNPaLTfLm?usp=sharing)
[![Sentiment Feedback](https://img.shields.io/badge/Feedback-Google%20Sheets-yellow?logo=googlesheets)](https://docs.google.com/spreadsheets/d/11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg/edit?usp=sharing)


---

<img width="927" height="614" alt="image" src="https://github.com/user-attachments/assets/090c0ae5-edbe-4b8d-a6b1-374cd5e2fe4a" />

## Features

Data collection from Sendo.vn using Selenium.

Text preprocessing: lowercase conversion, normalization (URLs, numbers, emojis), tokenization (via underthesea), stopword removal.

Comparative evaluation of traditional ML models: Logistic Regression, Linear SVM, and Multinomial Naive Bayes, with TF-IDF vectorization and metrics like Accuracy, F1-score, Precision, Recall, and Confusion Matrix.

Fine-tuning of PhoBERT (base model from wonrax/phobert-base-vietnamese-sentiment) on the processed dataset. Model and tokenizer uploaded to Hugging Face.

Interactive Streamlit app: upload CSV (with comment column), visualize results via bar charts, pie charts, word clouds, download predictions, and collect user feedback.

Continuous learning loop: user-corrected labels via feedback are saved to Google Sheets for model enhancement.

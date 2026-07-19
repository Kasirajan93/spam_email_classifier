# spam_email_classifier
An AI-powered Spam &amp; Phishing Email Classifier using NLP, TF-IDF, and Multinomial Naive Bayes with a professional Streamlit web application.

# 📧 AI-Powered Spam & Phishing Email Classifier

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

The AI-Powered Spam & Phishing Email Classifier is a machine learning application that detects whether an email is **Spam** or **Not Spam** by analyzing its subject and content.

The application uses Natural Language Processing (NLP) with TF-IDF feature extraction and a Multinomial Naive Bayes classifier to provide fast and accurate predictions through an interactive Streamlit web application.

---

## 🚀 Features

- Detect Spam and Legitimate Emails
- Email Subject & Body Analysis
- NLP-based Text Processing
- TF-IDF Feature Extraction
- Multinomial Naive Bayes Classification
- Prediction Confidence Score
- Professional Streamlit Dashboard
- Fast Real-Time Prediction

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- NLTK

---

## 📂 Project Structure

```
spam_email_classifier/
│
├── app.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

```
Email Input
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Multinomial Naive Bayes
     │
     ▼
Spam / Not Spam Prediction
     │
     ▼
Confidence Score
```

---

## 📊 Dataset Summary

- Total Emails : **5,851**
- Legitimate Emails : **4,425**
- Spam Emails : **1,426**

The dataset was created by combining multiple publicly available spam email datasets, cleaning the text, removing duplicates, and standardizing the format before training the model.

---

## 🤖 Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Text Preprocessing
- TF-IDF Feature Engineering
- Model Training
- Model Evaluation
- Streamlit Deployment

---

## 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 96% |
| Precision | 98% |
| Recall | 84% |
| F1 Score | 91% |
| ROC-AUC | 0.994 |

---

## 🧠 Models Compared

- Logistic Regression
- Multinomial Naive Bayes ✅
- Random Forest

The Multinomial Naive Bayes model was selected based on its overall performance on the evaluation dataset and its compatibility with TF-IDF features.

---

## ▶️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/spam_email_classifier.git

cd spam_email_classifier

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔮 Future Improvements

- Deep Learning (LSTM/BERT)
- URL Analysis
- Email Attachment Detection
- Multi-language Spam Detection
- Explainable AI (XAI)
- API Integration

---

## 👨‍💻 Author

**Doctor Shiva**

AI & Machine Learning Enthusiast

GitHub:
https://github.com/Kasirajan93

LinkedIn:
https://linkedin.com/in/kasi-rajan-488005349

---

⭐ If you found this project useful, consider giving it a star.

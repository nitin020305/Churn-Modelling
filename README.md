<div align="center">

# 🏦 BankChurn Predictor
### Customer Churn Prediction using Machine Learning

<p>
A machine learning project that predicts whether a bank customer will churn 
based on demographic and financial features.
</p>

</div>

---

## 📌 Overview

Customer churn is a major challenge in the banking industry. This project builds a supervised machine learning model to predict customer churn using structured customer data.

The model helps identify high-risk customers based on financial and behavioral attributes.

---

## 📊 Dataset Features (13 Total)

- CreditScore  
- Geography  
- Gender  
- Age  
- Tenure  
- Balance  
- NumOfProducts  
- HasCrCard  
- IsActiveMember  
- EstimatedSalary  
- (Encoded categorical features)

---

## 🤖 Models Used

The following machine learning models were trained and evaluated:

- Logistic Regression  
- Random Forest Classifier  
- Gradient Boosting  
- XGBoost   

### ✅ Final Selected Model
Random Forest Classifier (based on performance comparison)

---

## 📈 Performance Metrics

| Metric        | Score  |
|--------------|--------|
| Accuracy     | **84.2%** |
| ROC-AUC      | **0.848** |
| Precision    | ~0.83 |
| Recall       | ~0.60 |
| F1-Score     | ~0.69 |

> ROC-AUC of 0.848 indicates strong class separation capability.

---

## ⚙️ ML Pipeline

- Data Cleaning  
- Label Encoding / One-Hot Encoding  
- Feature Scaling  
- Train-Test Split  
- Model Training  
- Cross Validation  
- Hyperparameter Tuning  
- Model Evaluation  

---

## 🧠 Problem Type

- Supervised Learning  
- Binary Classification  
- Imbalanced Dataset Handling  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Flask (for deployment UI)

---

## 📂 Project Structure


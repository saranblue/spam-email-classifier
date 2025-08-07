# 📧 Spam Email Classifier – Streamlit Web App

A simple and effective **Spam Email Classifier** built using **Machine Learning (Naive Bayes)** and deployed as a **Streamlit web app**. Paste a message into the interface and instantly find out if it's **Spam** or **Not Spam**.

---

## 🚀 Live Demo
👉 [Click here to try the app](https://spam-email-classifier-5vr73p2od7jprmavi5mfvg.streamlit.app/)  


---

## 🛠️ Features

- ✅ Real-time spam detection
- ✅ Trained on SMS Spam Collection Dataset
- ✅ Clean, beginner-friendly web interface using **Streamlit**
- ✅ Accurate classification with **TF-IDF + Naive Bayes**
- ✅ Fully deployed online (free hosting)

---

## 📷 Preview

![App Screenshot]()  
![App Screenshot]()  


---

## 🧠 How It Works

1. **Preprocessing**: Cleans input message (removes punctuation, lowercases, etc.)
2. **Vectorization**: Transforms text into numerical features using TF-IDF
3. **Model**: Naive Bayes classifier trained on labeled SMS data
4. **Prediction**: Outputs “Spam” or “Not Spam” with real-time feedback

---

## 📁 Project Structure
```
spam-email-classifier/
├── spam_app.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

## 🧪 Local Setup

## 1. Clone the repository:
git clone https://github.com/saranblue/spam-email-classifier.git
cd spam-email-classifier

## 2. Install dependencies:
pip install -r requirements.txt

## 3. Run the app:
streamlit run spam_app.py

## 🧰 Tech Stack
```
- Python
- Pandas
- scikit-learn
- Streamlit
```

## 📚 Dataset
```
- 📦 SMS Spam Collection Dataset
  Link to Dataset
```


## 💡 Future Improvements
-Add model confidence percentage

-Save message history

-Deploy with custom domain

-Try other ML models like Logistic Regression or SVM



















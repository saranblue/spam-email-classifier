import re
import pandas as pd
import joblib
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# -----------------------------
# Load and Train the Model
# -----------------------------
@st.cache_resource
def load_model():
    # Load dataset
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

    # Clean text
    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text

    df['message'] = df['message'].apply(clean_text)
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    # Vectorize
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['message'])
    y = df['label']

    # Train model
    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer, clean_text

# Load model and vectorizer
model, vectorizer, clean_text = load_model()

# -----------------------------
# Streamlit App Interface
# -----------------------------
st.title("📧 Spam Email Classifier")
st.write("Paste your message below and click **Predict** to see if it's spam.")

# Text input
user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vect_input = vectorizer.transform([cleaned])
        result = model.predict(vect_input)[0]
        proba = model.predict_proba(vect_input)[0][1] * 100
        st.write(f"Model Confidence: {proba:.2f}%")
        if result == 1:
            st.error("🔴 Spam Detected!")
        else:
            st.success("🟢 This is NOT Spam.")



import streamlit as st
import pickle
import numpy as np

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define sentiment labels
sentiment_map = {
    0: 'Negative',
    1: 'Neutral',
    2: 'Positive'
}

def predict_sentiment(text):
    vect = vectorizer.transform([text])
    prediction = model.predict(vect)
    return prediction[0]

def get_sentiment_label(prediction):
    return [prediction]

# Streamlit app
st.title('Twitter Sentiment Analysis')

tweet = st.text_area('Enter the tweet')

if st.button('Analyze Sentiment'):
    sentiment_index = predict_sentiment(tweet)
    sentiment = get_sentiment_label(sentiment_index)
    st.write(f'The sentiment of the tweet is: {sentiment}')
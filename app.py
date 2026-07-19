import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence 
from tensorflow.keras.models import load_model
import streamlit as st

# 1. Load the word index maps
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# 2. Safely load the model
model = load_model('Model/simple_rnn_imdb.h5')

def decode_review(encoded_review):
    return " ".join([reverse_word_index.get(i-3, '?') for i in encoded_review])

def preprocessor_text(text):
    # Standardize to lowercase and split by spaces
    words = text.lower().split()
    
    encoded_review = []
    MAX_FEATURES = 10000 # Your training limit
    
    for word in words:
        # Get index from original dictionary (defaults to 2 if missing)
        # Shift by +3 to account for the IMDB special tokens (0=pad, 1=start, 2=oov)
        idx = word_index.get(word, 2) + 3
        
        # FIX: Check if index exceeds our embedding vocabulary limit
        if idx >= MAX_FEATURES:
            encoded_review.append(2) # Fallback to Out-Of-Vocabulary token
        else:
            encoded_review.append(idx)
            
    # Pad sequences to the exact length of 500
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# 3. Streamlit User Interface Elements
st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a Movie Review To Classify it as positive or Negative")

user_input = st.text_area("Movie Review")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text before clicking Classify.")
    else:
        preprocessed_input = preprocessor_text(user_input)
        prediction = model.predict(preprocessed_input)

        sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

        st.write(f"**Sentiment :** {sentiment}")
        st.write(f"**Prediction Score :** {prediction[0][0]:.4f}")

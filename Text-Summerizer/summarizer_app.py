import pickle
import streamlit as st
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the pickled summarizer function
with open("text_rank_summarizer.pkl", "rb") as f:
    text_rank_summarizer = pickle.load(f)

# Streamlit UI code
def main():
    # Set up the Streamlit app title and description
    st.title("Text Summarization with TextRank (Pickle version)")
    st.write("This app uses the TextRank algorithm to summarize text. Enter text, and it will generate a concise summary.")

    # Create a text input area for users to enter text
    input_text = st.text_area("Enter your text here:", height=250)
    
    # Select number of sentences for the summary
    num_sentences = st.slider("Select the number of sentences for summary", min_value=1, max_value=5, value=3)

    # Summarize button
    if st.button("Generate Summary"):
        if input_text.strip() != "":
            # Generate the summary using the loaded pickled function
            summary = text_rank_summarizer(input_text, num_sentences)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

# Run the app
if __name__ == "__main__":
    main()

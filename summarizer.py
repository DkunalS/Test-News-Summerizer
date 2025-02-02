import streamlit as st
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from transformers import pipeline
import pyttsx3

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Load the summarization model
summarizer = pipeline("summarization")

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return None

def summarize_text(text, max_length=150):
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def text_to_speech(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Streamlit UI
st.title("📰 Shruti - The News Companion")
st.write("Enter a news article URL to get a summarized version and listen to it.")

url = st.text_input("Enter News URL")

if st.button("Summarize"):
    if url:
        with st.spinner("Fetching article..."):
            article_text = scrape_article(url)
            
            if article_text:
                with st.spinner("Summarizing..."):
                    summary = summarize_text(article_text)
                    st.subheader("Summary:")
                    st.write(summary)
                    
                    if st.button("Listen to Summary"):
                        text_to_speech(summary)
            else:
                st.error("Failed to retrieve the article. Please check the URL.")
    else:
        st.warning("Please enter a valid URL.")

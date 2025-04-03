
# Access API key
import streamlit as st

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

SUPPORTED_LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese": "zh"
}

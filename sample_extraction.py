import streamlit as st
from pdf_to_text import text_extractor 

st.title("PDF Text Extractor")

file = st.file_uploader("Upload a PDF", type=["pdf"])

if file is not None:
    flag = st.button("Extract Text")
    if flag:
        text = text_extractor(file)
        st.write(text)

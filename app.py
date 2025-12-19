# app.py
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! This app is hosted on the cloud.")

if st.button("Click me"):
    st.balloons()

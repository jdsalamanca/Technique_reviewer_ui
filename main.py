import streamlit as st
import requests

st.header("Corrector de técnica")


link = ""
st.subheader("Sube un video de senatdilla")
bytes_data = None
upload = st.file_uploader("Upload video")
if upload is not None:
  bytes_data = uploaded_file.getvalue()
  
if bytes_data:
  correct = st.button("Corregir tecnica")
  feedback = ""
  if correct:
    response = requests.post(url=link, file=bytes_data)
    if "feedback" in response.json():
      feedback  = response.json()["feedback"]
    else:
      feedback = response.text
      
  if feedback:
    st.write(feedback)

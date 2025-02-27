# text to speech generator : gtts = google text to speech
import streamlit as st
from gtts import gTTS       # pip install gtts
import os # ye generated audio file ko manage karega # pip install os 
# title banaonga UI ka : heading banaonga
st.title("Text To Speech Generator")
# user ka input box banaonga 
User_input = st.text_area("Write Your Text here")
# dropdown banaonga multiple options ka 
language = st.selectbox("Select Your Language",["ar","ur","en","es","fr","de",])
# button banaonga :
if st.button("Convert Into Speech"):
    # gtts se speech generate karwana h :
    if User_input :
        tts = gTTS(text=User_input,lang=language,slow=False)
        tts.save("speech.mp3")
        st.audio("speech.mp3")


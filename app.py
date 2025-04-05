import streamlit as st
from backend import get_advisory
from voice_module import transcribe_voice

st.title(" Smart Agri Advisor")
st.markdown("Select input method:")

option = st.radio("", ["Text Input", "Voice Input"])

if option == "Text Input":
    user_input = st.text_input("Enter your crop or issue:")
elif option == "Voice Input":
    audio = st.file_uploader("Upload your voice query")
    if audio:
        user_input = transcribe_voice(audio)
        st.write(f"You said: {user_input}")

if st.button("Get Advisory") and user_input:
    advice = get_advisory(user_input)
    st.success(advice)

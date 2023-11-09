# main.py

import streamlit as st
import torchaudio
import os
from utils import TTSUtils, save_audio

st.title("SpeakEasy: Transforming Text to Speech")

# Create an instance of TTSUtils
bundle = torchaudio.pipelines.TACOTRON2_WAVERNN_PHONE_LJSPEECH
tts_utils = TTSUtils(bundle)

# Input text
text = st.text_input("Enter the text to convert to speech", "Hello World")

# Generate and save audio
if st.button("Generate and Play Audio"):
    waveforms, spec, sample_rate = tts_utils.generate_audio(text)
    audio_file_path = "output_audio.wav"  # Define the output audio file path
    save_audio(waveforms, sample_rate, audio_file_path)

    # Play the saved audio
    audio_bytes = open(audio_file_path, 'rb').read()
    st.audio(audio_bytes, format="audio/wav")

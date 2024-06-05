# This is the code to control the siren once it is triggered 
import streamlit as st
from pygame import mixer

def main():
    st.title("Siren Controller")
    
    # Load the audio file
    audio_file_path = "H:\\project final\\project final\\Siren.mpeg"

    # Initialize pygame mixer
    mixer.init()

    # Function to play the audio
    def play_audio():
        mixer.music.load(audio_file_path)
        mixer.music.play(-1)  # -1 means loop indefinitely

    # Function to stop the audio
    def stop_audio():
        mixer.music.stop()

    # Play audio on app start
    play_audio()

    # Button to stop the siren
    if st.button("Stop Siren"):
        stop_audio()

if __name__ == "__main__":
    main()

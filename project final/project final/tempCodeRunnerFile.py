import streamlit as st
from pygame import mixer

def main():
    st.title("Audio Player")

    # Load the audio file
    audio_file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\Siren.mpeg"

    # Initialize pygame mixer
    mixer.init()

    # Function to play the audio
    def play_audio():
        mixer.music.load(audio_file_path)
        mixer.music.play(-1)  # -1 means loop indefinitely

    # Function to stop the audio
    def stop_audio():
        mixer.music.stop()

    # Play audio button
    play_button = st.button("Play Audio")
    if play_button:
        play_audio()

    # Stop audio button
    stop_button = st.button("Stop Audio")
    if stop_button:
        stop_audio()

if __name__ == "__main__":
    main()

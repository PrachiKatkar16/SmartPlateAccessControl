
#numberplate+facial+siren+killswitch+arduino+nolag+welcome if authorized
import streamlit as st
import cv2
import time
import easyocr
import face_recognition
import subprocess
# import serial
import pygame

# Initialize serial communication with the Arduino board
# arduino = serial.Serial('COM5', 9600)  # Adjust COM port as needed

def play_welcome_sound():
        pygame.mixer.init()
        pygame.mixer.music.load("H:\\project final\\project final\\welcome.mp3")  # Adjust path if necessary
        pygame.mixer.music.play()

def main():
    st.title("Smart Plate Access Control")

    # Load the reference image for facial recognition
    reference_image_path = "H:\\project final\\project final\\Prachi.jpg"
    #reference_image_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\project final\\janhavi.jpeg"
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not video_capture.isOpened():
        st.error("Unable to open the webcam. Please check your webcam connection.")
        return

    # Set up the OpenCV window
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Display the webcam feed
    st.write("Webcam Feed")
    frame_container = st.empty()
    timer_text = st.empty()

    # Initialize timer
    timer_seconds = 10
    start_time = time.time()

    while time.time() - start_time < timer_seconds:
        # Read frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            st.error("Failed to capture frame from the webcam.")
            break

        # Display the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_container.image(frame, channels="RGB")

        # Update timer
        remaining_time = int(timer_seconds - (time.time() - start_time))
        timer_text.text(f"Time remaining: {remaining_time} seconds")

    # Capture picture automatically
    ret, frame = video_capture.read()
    if ret:
        file_path = "captured.jpg"
        cv2.imwrite(file_path, frame)
        st.success("Image captured successfully!")
        st.image(file_path)

        # Perform face recognition
        captured_image = face_recognition.load_image_file(file_path)
        captured_encoding = face_recognition.face_encodings(captured_image)
        
        if len(captured_encoding) > 0:
            captured_encoding = captured_encoding[0]
            # Compare the captured face with the reference face
            facial_recognition_results = face_recognition.compare_faces([reference_encoding], captured_encoding)
            facial_recognition_authorized = facial_recognition_results[0]
            st.write("Facial Recognition: ", "Authorized" if facial_recognition_authorized else "Unauthorized")
        else:
            facial_recognition_authorized = False

        # Perform number plate recognition
        reader = easyocr.Reader(['en'])
        result = reader.readtext(file_path)

        # Extract detected number plate text
        detected_number = ""
        for detection in result:
            text = detection[1].replace(" ", "").replace("-", "")  # Remove spaces and hyphens
            detected_number += text

        # Check if number plate is found and authorized
        authorized = detected_number == "MH16CZ7892"
        st.write(f"Detected Number Plate: {detected_number}")

        # Check if authorized
        if facial_recognition_authorized and authorized:
            st.success("Authorized Person")
            play_welcome_sound()
            # Send signal to Arduino board
            # arduino.write(b'a')

        else:
            st.error("Unauthorized Person")
            # Play the siren using subprocess to avoid restarting the Streamlit app
            subprocess.Popen(["streamlit", "run", "H:\\project final\\project final\\Siren.py"])

    else:
        st.error("Failed to capture image from the webcam.")

    # Release the webcam
    video_capture.release()

if __name__ == "__main__":
    main()

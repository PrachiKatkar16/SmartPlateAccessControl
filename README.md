Hii welcome to "How to operate SPAC?"


First make sure you have the following:
1. Libraries (pip install.....) : 
    streamlit
    cv2
    time
    easyocr
    face_recognition
    subprocess
    serial
    pygame
1. A number plate (MH16CZ7892 - Authorized) & (MH16BN5447 - Unauthorized)
2. A beautiful face (optional)
3. Arduino connected to your system. (Optional)



If you dont have arduiono do not worry you can still see the results just comment out(#) these lines from the codes:
SPAC.py - 13,105

Change the path:
SPAC.py - 17,24,25,110
Siren.py - 9

Once you are done with all this just go to he Siren.py and run it. You will see a command that will appear somethin like this:


pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
Hello from the pygame community. https://www.pygame.org/contribute.html
2024-04-16 18:36:01.196 
  Warning: to view this Streamlit app on a browser, run it with the following
  command:

    streamlit run c:\Users\DELL\OneDrive\Desktop\project final\SPAC.py [ARGUMENTS]
Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.)


Ignore it and just type this with your path to SPAC.py and hit enter:
streamlit run "C:\Users\DELL\OneDrive\Desktop\project final\SPAC.py" 
>> 

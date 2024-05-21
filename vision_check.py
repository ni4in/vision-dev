import cv2 
import numpy as np 
import base64
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not access the webcam")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame")
        break 

    _, buffer = cv2.imencode('.jpg', frame)
    frame_base64 = base64.b64encode(buffer).decode('utf8')

    cv2.imshow('Webcam Feed', frame)
        
        # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()





    




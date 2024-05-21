import socketio
import cv2 
import numpy as np 
import base64
import eventlet

sio = socketio.Server(ping_timeout=20)
app = socketio.WSGIApp(sio)
capturing =False

def start_capture():
    global capturing
    capturing = True
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam")

    while capturing:

        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read a frame")
            break 
        _, buffer = cv2.imencode('.jpg', frame)
        frame_base64 = base64.b64encode(buffer).decode('utf8')
        print('sending frames')
        sio.emit('result', frame_base64)
        sio.sleep(2)
    cap.release()

def stop_capture():
    global capturing
    capturing = False

@sio.event 
def start_inspection(sid,data):
    print('start video capturing')
    start_capture()

@sio.event 
def stop_inspection(sid,data):
    stop_capture()

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('',5001)),app)
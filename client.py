import socketio
import time 
import base64
import cv2
import numpy as np
sio = socketio.Client()

@sio.event
def connect():
    print("connection established with server")

@sio.event
def disconnect():
    print("disconnected from the server")

@sio.event 
def visualize(frame_base64):
    print('visualisation event started')
    image_bytes = base64.b64decode(frame_base64)
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    decoded_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    print(decoded_image)




if __name__ == "__main__":
    sio.connect("http://0.0.0.0:5001")
    time.sleep(2)
    sio.emit('start_inspection')
    time.sleep(2)
    sio.emit('stop_inspection')
    sio.wait()


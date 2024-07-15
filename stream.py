import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLO model
model = YOLO("./best.onnx")
#D:\Python\YOLO\Notes\Front\best.onnx

# Object classes
classNames = ['patient', 'on_monitor', 'doctor', 'visitor', 'nurse', 'empty_bed', 'off_monitor', 
              'empty_room', 'monitor', 'off_montior', 'docter', 'monitor2', 'doctor1', 'doctor2']

# Streamlit application
st.title("Real-Time Object Detection with YOLO")

# Video stream option
run = st.checkbox('Run Webcam')

if run:
    stframe = st.empty()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Camera not available")
            break

        results = model(frame)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                cv2.putText(frame, f'{classNames[cls]} {conf}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        
        stframe.image(frame, channels='BGR')

    cap.release()

st.write("Stopped")

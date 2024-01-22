import serial
import time
from tensorflow import keras
import cv2
import numpy as np
from PIL import Image


webcam = cv2.VideoCapture(0)

py_serial=serial.Serial(
    port='com3'
    baudrate=9600
)#uno board와 연결
model=keras.models.load_model('ai_model.h5')# 미리 학습시켜둔 모델과 가중치 로드

while True:
    status, frame=webcam.read()#웹캠 영상 가져오기
    if status:
        cv2.imshow("image",frame)#가공전 웹캠 영상 확인
        
        resized_image_array=cv2.resize(frame,(256,256))
        resized_image_array = np.expand_dims(resized_image_array, axis=0)
        
        prediction=model.predict(resized_image_array)#모델을 이용한 정위치 확인
        single_prediction=prediction[0,0]
        print('예측 확률', single_prediction)
        if single_prediction>=#임계치:
            commend='0 또는 1'
            py_serial.write(commend.encode())
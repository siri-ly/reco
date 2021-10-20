import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new

HOST=''
PORT=6789

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()
k = 0
### new
data = b''
payload_size = struct.calcsize("L") 
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###
    frame=pickle.loads(frame_data)
    print(frame)
    for i in frame:
        if (i != 'unknown'):
            cv2.imwrite('C:/Users/Siri/Desktop/sem6/Capstone/face_det/opencv-face-recognition/opencv-face-recognition/Server_output/' + i +'.png', frame[i][0])
            cv2.imwrite('C:/Users/Siri/Desktop/sem6/Capstone/face_det/opencv-face-recognition/opencv-face-recognition/Server_output/' + i +'_real.png', frame[i][1])

        else:
            cv2.imwrite('C:/Users/Siri/Desktop/sem6/Capstone/face_det/opencv-face-recognition/opencv-face-recognition/Server_output/' + i + str(k) + '.png', frame[i][0])
            cv2.imwrite('C:/Users/Siri/Desktop/sem6/Capstone/face_det/opencv-face-recognition/opencv-face-recognition/Server_output/' + i + str(k) + '_real.png', frame[i][1])

    #cv2.imshow('frame',frame)
    k += 1

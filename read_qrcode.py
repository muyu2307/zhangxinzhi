import cv2
import numpy as np
from pyzbar.pyzbar import decode

#对本地的二维码图片进行读取：
img = cv2.imread("/home/zxz/work/opencv_test/qrcode.png")
for barcode in decode(img):
    print(barcode.rect) #空间信息
    print(barcode.data)
    myData=barcode.data.decode('utf-8')
    print(myData)  #解码
 
#利用摄像头读取二维码：
'''
cap=cv2.VideoCapture(0)
cap.set(3,640)  #
cap.set(4,480)  #

while True:
    success,img=cap.read()
    for barcode in decode(img):
        myData =barcode.data.decode('utf-8')
        print(myData)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        cv2.putText(img,myData,(pts2[0],pts[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
'''
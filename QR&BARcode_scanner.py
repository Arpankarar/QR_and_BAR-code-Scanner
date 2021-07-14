import cv2
import numpy as np
from pyzbar.pyzbar import decode
#img=cv2.imread("sample_bar-code.jpeg")
cap=cv2.VideoCapture(0)
cap.set(3,650)
cap.set(4,480)

while True :
    success,img=cap.read()
    for barcode in decode(img):
        myData=barcode.data.decode('utf-8') # to change the data to string.
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,0),4)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,0,255),1)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
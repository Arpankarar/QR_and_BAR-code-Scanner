import cv2
import numpy as np
from pyzbar.pyzbar import decode
img=cv2.imread("sample_bar-code.jpeg")
dimg=decode(img)
for barcode in decode(img):
    # print(barcode.data) # to print only the data associated with that barcode.
    myData=barcode.data.decode('utf-8') # to change the data to string.
    print(myData)
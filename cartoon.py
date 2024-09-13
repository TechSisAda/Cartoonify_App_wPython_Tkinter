import cv2
from PIL import Image
import numpy as np 


def cartooned(image_path,output_path):
    img = cv2.imread(image_path)
    if image_path is None:
        print("desired image not found")
        return
    img = cv2.resize(img, (600,650))#resize

    for _ in range(8):
        img= cv2.bilateralFilter(img, d=7, sigmaColor=20, sigmaSpace=10)#smoothing
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convert to grayscale
    gray = cv2.medianBlur(gray,3) #add blur filter

    edge = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,blockSize=7,C=3)
    
    cartoon = cv2.bitwise_and(img, img, mask=edge)#to combine img with edge

    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)#convert BGR to RGB
    pil_image = Image.fromarray(cartoon)
    pil_image.save(output_path)

cartooned('images/ada6.png', 'images/ada62_cartoon.jpeg')





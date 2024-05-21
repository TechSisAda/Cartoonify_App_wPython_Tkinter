import cv2
from PIL import Image
import numpy as np

def cartoonify(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error 404: Image can not be read.")
        return 
    image = cv2.resize(image, (800, 1000))
    for _ in range(2):
        image = cv2.bilateralFilter(image, d=9, sigmaColor=35, sigmaSpace=35)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, blockSize=7, C=1.5)
    color = cv2.bilateralFilter(image, d=9, sigmaColor=5, sigmaSpace=5)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cartoon)
    pil_image.save(output_path)

cartoonify('images/ada1.jpeg', 'images/ada2cartoon.jpeg')
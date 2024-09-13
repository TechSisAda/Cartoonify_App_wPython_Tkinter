import cv2
from PIL import Image
import numpy as np

def cartoonify(image_path, output_path):
    # Read the image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        print("Error 404: Image cannot be read.")
        return
    
    # Resize the image to make the process easier to handle
    image = cv2.resize(image, (800, 800))

    # Smoothing image using bilateral filter multiple times
    for _ in range(3):
        image = cv2.bilateralFilter(image, d=9, sigmaColor=20, sigmaSpace=20)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Create an edge mask using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, blockSize=9, C=4)
    
    # Further smooth the color image
    color = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    # Combine the edges with the color image using bitwise AND
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Convert to RGB for PIL compatibility and save the image
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cartoon)
    pil_image.save(output_path)

# Properly call the function outside the definition
cartoonify('images/ada6.png', 'images/ada61_cartoon.jpeg')

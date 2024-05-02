import cv2
from PIL import Image
import numpy as np

def cartoonify(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)
    # Check if image is loaded
    if img is None:
        print("Error: Image could not be read.")
        return
    
    # Resize image to speed up processing
    img = cv2.resize(img, (800, 800))
    
    # Apply bilateral filter multiple times to achieve smoothing
    for _ in range(5):
        img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply median blur
    gray = cv2.medianBlur(gray, 5)
    # Use adaptive thresholding to create an edge mask
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, blockSize=9, C=2)
    
    # Convert to a color image
    color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Combine edges and color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # Convert the result to RGB and save using PIL to maintain JPEG quality and metadata
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cartoon)
    pil_image.save(output_path)

# Example usage:
cartoonify('images/ada2.jpeg', 'images/ada2CLR.jpeg')
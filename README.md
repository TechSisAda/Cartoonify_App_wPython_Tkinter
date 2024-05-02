This is for the project assigned to ADAEZE NNONYELU
https://github.com/TechSisAda/PythonBasics.git as the git repo 
Python Project to Cartoonify images

first thing i did was to install PIP, followed by OpenCV and PILLOW as additional libraries

Next is to load the image, you want to cartoonify  using PILLOW:

Next  is to convert the image to grayscale (L)

Applying Edge Detection is next

Applying bilateral filtering to smooth the edges and reduce colors

Next is to display{show()} OR save the cartoonified image {save()}


********************************************************************************

                        INDEX 3
First you import the necesary libraries:
    cv2 is OpenCV library for handling image processing tasks.
    Image is a part of the PIL,pillow, library used for handling  image files ie saving them in differnt formats.
    numpy is a library for handling arrarys and matrices used for handling image manipulation bc images are viewed as arrays.

SECOND: Define the Cartoonify function:
    the function CARTOONIFY takes two arg: IMAGE_PATH to show the location of the image and OUTPUT_PATH to show where to save the cartooned image.

THIRD Load and check the image
    cv2.imread is for reading the image from the given path.
    checks if the image is loaded correctly or if the path is incorrect or corrupt.
    it then returns an error message if there's any, and leaves the function.

FOURTH Resize Image:
    Resize the image in order to speed up the subsequent processing

FIFTH Apply Bilateral Filter for Smoothing Images and Reducing Noise still keeping the Edges
    The FOR loop applys bilateral filter 3 times to the image. This bilateral filter is a type of filter that reduces the noise and keeps edges sharp, this is cruical for the cartoon effect.
    D, SIGMA COLOR, and SIGMA SPACE are parameters of the filters operation.
    SIGMA COLOR decides which colors to merge and which to keep separate. the smller it is, the more edges preserved.

SIXTH Convert to Grayscale and Apply Medium Blur:
    cvtColor converts the color image to grayscale for edge detection.
    medianBlur reduces noise the grayscale in order to improve the quality of edge detection.

SEVENTH Adaptive Thresholding for Edge Detection:
    This detects edges by adjusting the threshold value based on the local image regions, creating a binary image of edges.

EIGHTH Reapply Bilateral Filter to Smooth Color Image
    reapplying the bilateral filter to the original image to further enhance the smoothness for the final cartoon effect.

NINTH Combine Edges and Color Image
    it combines the color image and the edge mask. Making the edges black and the inner regions colored, therefore creating the cartoon effect. 

TENTH Convert back to RGB and Save the Image
    cvtcolor converts the image from BGR, which is the default color format for OpenCV, to RGB.
    Image.fromarray converts the array representation of the image into a PIL Image Object.
    Then save the image to a specific path in a suitable format(JPEG in this case).

LASTLY Call the cartoonify function with the specified paths to the iput and output files.
    
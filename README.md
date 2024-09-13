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
    cv2 is OpenCV library for handling image processing tasks. It helps with reading the images, processing them and performing operations like filtering or edge detetction.
    Image is a part of the PIL (PILLOW) library used for handling  image files and saving them in different formats.
    numpy is a library essntial for handling arrays, which is how images are stored (as matrices of pixels).

SECOND: Define the Cartoonify function:
    the function CARTOONIFY takes two arg: IMAGE_PATH to show the location of the image and OUTPUT_PATH to show where to save the cartooned image.

THIRD Load, Read and check the image
    cv2.imread is for reading the image from the given path. Here the image is converted into a format that OpenCV can process.
    checks if the image is loaded correctly or if the path is incorrect or corrupt.
    it then returns an error message if there's any, and leaves the function.

FOURTH Resize Image:
    Resize the image in order to speed up the subsequent processing

FIFTH Apply Bilateral Filter for Smoothing Images and Reducing Noise still keeping the Edges
    The FOR loop applys bilateral filter 3 times to the image.
    The underscore is a place-holder (i dont care about the loop index, just that it runs 3 times)
    This bilateral filter is a type of filter that reduces the noise and keeps edges sharp, this is cruical for the cartoon effect.
    D, SIGMA COLOR, and SIGMA SPACE are parameters of the filters operation.
    d=9:Diameter of each pixel neighborhood.
    SIGMA COLOR decides which colors to merge and which to keep separate. the smaller it is, the more edges preserved.
    SigmaColor=20: How much to smooth the colors.
    SigmaSpace=20: How much to smooth the spatial details.


SIXTH Convert to Grayscale and Apply Medium Blur:
    cvtColor converts the color image to grayscale for creating the cartoon-like edges (edge detection).
    medianBlur reduces noise on the grayscale in order to improve the quality of edge detection. 5 show the size of the filter applied to the pixels.

SEVENTH Adaptive Thresholding for Edge Detection:
    It creates a mask of the edges in the image, just ike drawing the outlines of the image.
    255: maximum intensity for the edges(white)
    Adaptive_thresh_mean_c: this method looks at the small regions of the image to determine if theyshould be white(edge) or black(not an edge).
    thresh_binary: it applies a binary threshold(black or white)
    blocksize=9: size of the area used to calculate the threshold.
    c=4: a constant subtracted from the mean to fine-tune edge detection.

EIGHTH Reapply Bilateral Filter to Smooth Color Image
    reapplying the bilateral filter to the original image to further enhance the smoothness for the final cartoon effect. The effects of smoothing of this one are stronger than the first one.

NINTH Combine Edges and Color Image
    It combines the edges(black and white lines) with the color image, like coloring inside the cartoon outlines.
    mask=edges: ensures that the edges are apllied to the color image, therefore creating the cartoon effect. 

TENTH Convert back to RGB and Save the Image
    OpenCV uses BGR(Blue-Green-Red) format for colors but other image libraries use RGB(Red-Green-Blue).
    cvtcolor converts the image from BGR, which is the default color format for OpenCV, to RGB.
    Image.fromarray converts the array representation of the image into a PIL Image Object(which PIL understands).
    Then save the image to a specific path(output_path) in a suitable format(JPEG in this case).

LASTLY Call the cartoonify function with the specified paths to the input and output files. Telling it to process the image found at the image_path and save the cartoon version to the output_path.
    
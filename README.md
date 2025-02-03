This is for the project assigned to ADAEZE NNONYELU
https://github.com/TechSisAda/PythonBasics.git as the git repo 
Python Project to Cartoonify images

*****************************************************************************************************************************************
                        Tkinter Cartoonified App
First thing i did was to install the libraries i needed:
i. TKINTER
ii. PIP
iii. OPEN CV
iv. NUMPY
<b>
Tkinter is used to create the Graphical User Interface (GUI); Pillow (PIP) is used to handle and converts images and displays them in the GUI; OpenCV is for image processing.<p></p>

I then imported these libraries into the code including *filedialog* for users to open a file selection dialog, *messagebox* to display error messages, *numpy* for array manipulations; and *os* which is the standard python library for interacting with the operating system.<b>

The first class we are dealing with is *ImageLoader* handles the loading of the images from the user's file system.
Under this ImageLoader class, we have defined two methods:
 *__init__* method: which initilaizes the *file_path* variable to store the path of the selected image
 *load_image* method: opens a file dialog for the user to select an image. I selected an initial folder. And on this folder it'll show only file types under jpeg, png, and jpg.
 Under the *load_image* method, we have an if statement that checks to see if the file extension of the is under jpeg, jpg, or png and an error message is shown for them to pick another file. Otherwise it returns back to the file path.<b>

 The second class is the *Cartoonifier* class that applies a cartoon effect to any of the selected images.
 Under this Cartoonifier class, we have defined two methods:
 *__init__* method: which initializes the class with the image path passed when creating the cartoon.
 *cartoonify_image* method: it reads the image and resizes it to 850x850 pixels.
 Next, is the *for loop* that applies a bilateral filter to the image 4 times.
 Gray is the an assigned variable that converts the image to gray scale which in turn creates edges and applying median blur to reduce noise, the of the grayscale improving edge detection .<b>

Next is assigning the variable *Edge* to a value for edge detection; adaptive threshold detects edges turning the images  into black and white outlines.
255: is the maximum intensity for edges.
Adaptive_thresh_mean_c: this method looks at the small regions of the image to determine if they should be white(edge) or black(not an edge).
thresh_binary: it applies a binary threshold(black or white)
blocksize=5: size of the area used to calculate the threshold.
c=2: a constant subtracted from the mean to fine-tune edge detection.<b>

Next is to combine the edge with original image under *cartoon*. *bitwise_and* joins edges and color like coloring inside of the a cartoon outline.
mask=edges ensures the edges are applied to the color image.
Then we convert the image back to RGB as OpenCV works in BGR returning the cartoonified image as a PIL image.<b>

The third class is *FileSaver* which handles the cartoonified image
*save_image* method: opens a save dialog allowing the user to choose where the cartooned image will be saved.
<p></p>
The Fourth Class is *CartoonifyApp* the class handling the GUI and integrates the other classes. And it has 5 methods:<b>
*__init__* method that initializes the main window *root*; sets the title, and defines its size. *image_label* is initialized as *None* to later hold the image displayed in the GUI.
Next creating a *load_image* button that calls the load_image method when clicked.
A *cartoonify_image* button disabled initially until an image is loaded, and applied when clicked.
A *save_image* is created too, disabled until a cartoonified image is generated.
<p>
self.image_label is None : stores the label widget that holds the image.

</p>
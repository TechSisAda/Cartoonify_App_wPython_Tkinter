import tkinter as tk 
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk


#the Class handling loading of the images.
class ImageLoader:
    def __init__(self):
        self.file_path = None 

    def load_image(self):
        #set the initial directory to the folder you want to open
        initial_folder = r"C:\Users\ADA NNONYELU\Desktop\dummy_folder"
        
        # opens file dialog in order to choose an image starting with the specified folder(dummy folder)
        self.file_path = filedialog.askopenfilename(initialdir=initial_folder) #filetypes=[("Image files", "*.jpeg;*.jpg;*.png")]) #to limit the files for this application to just image files(jpeg &png)
        
        if self.file_path:
            if not (self.file_path.endswith('.jpeg') or self.file_path.endswith('.jpg') or self.file_path.endswith('.png')):
                #error if the file selected is not a jpeg or png file
                messagebox.showerror("Error 404","Pick another image")
                return None
            return self.file_path
        return None
    
class Cartoonifier: #class to process the image selected and give it a cartoon-like effect
    def __init__(self,image_path):
        self.image_path = image_path #takes the file path of the image and stores it.
    
    def cartoonify_image(self):
        img =cv2.imread(self.image_path) #to reads the image form the file path
        img = cv2.resize(img, (850,850)) # to resize the image to 850:850

        for _ in range(8): 
            img = cv2.bilateralFilter(img, d=9, sigmaColor=15, sigmaSpace=12) #applies a bilateral filter 4 times to smooth the images while still preserving the edges.
                    #d = diameter of each pixel; sC = the smaller the num, the more edges preserved; sS = smooths spatial details

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting to gray scale to create edges
        gray = cv2.medianBlur(gray, 5) #reduces noise of the gray scale, improving the quality of the edge detection, 5 is the size of the filter.

        # edge detection: what this does is to create black and white lines(outlines) using adaptive threshold. the cartoon is therefore visible
        edge = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=5, C=2) #bS must be an odd num; c = finetunes the edges

        cartoon =cv2.bitwise_and(img, img, mask=edge)# this combines the edge and original image together. keeping the color in non-edge areas and making the edges darker;
                                                     #mask=edges ensures the edges are applied to the color image.

        cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB) #OpenCV works with BGR but PIL accepts RGB, so the image is converted.
        return Image.fromarray(cartoon) #the processed image is returned as a PIL image object


class FileSaver:
    def __init__(self):
        pass
    def save_image(self, image): 
        #saves cartoon image
        file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg"), ("PNG files", "*.png")])
        if file_path:
            image.save(file_path)


class CartoonifyApp:
    def __init__(self, root):
        self.root = root #initializes the main window; root
        self.root.title("Cartoonify Your Pictures")
        self.root.geometry("800x700")
        self.image_label = None #initialized as None to hold the image in the GUI later.

    #Buttons:
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=15) #creates a *load_image* button that calls the load_image method when clicked

        self.cartoonify_button = tk.Button(root, text="Cartoonify Image", command=self.cartoonify_image,state=tk.DISABLED)
        self.cartoonify_button.pack(pady=15)#creates a cartoonify image which is disabled in the beginning until an image is loaded, applies when clicked.

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=15)#creates a save button, disabled initialy until a cartooned image is generated

        self.loaded_image = None
     
    def load_image(self):
        loader = ImageLoader() #uses the ImageLoader class to load the image
        file_path = loader.load_image()

        if file_path:
            self.loaded_image = Image.open(file_path) #if successful,
            self.display_image(self.loaded_image)#it displays the image 
            self.cartoonify_button.config(state=tk.NORMAL)#enabling the caroonify image button


    def cartoonify_image(self):
        if self.loaded_image:
            cartoonifier =Cartoonifier(self.loaded_image.filename) #usesthe cartoonifier class
            self.cartoon_image = cartoonifier.cartoonify_image() #to apply the cartoon effect
            self.display_image(self.cartoon_image)# displays it 
            self.save_button.config(state=tk.NORMAL) # and then the save image button is enabled.

    def save_image(self):
        if self.cartoon_image:
            saver = FileSaver()# uses the File Saver class 
            saver.save_image(self.cartoon_image) #to save the cartoonified image
    
    def display_image(self,img): #Display Image method
        img.thumbnail((500, 500)) # Resizes the iamge to fit the display area.
        img_tk = ImageTk.PhotoImage(img) #Converting it to a format suitable to display on Tkinter.

        if self.image_label is None: #if no image is loaded, a label is created to display the image, if an image is already shown, it updates the label
            self.image_label= tk.Label(self.root, image=img_tk)
            self.image_label.image = img_tk #assigns img_tk to the label
            self.image_label.pack(pady=10)
        else:
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

#if __name__ == "__main__": #it checks if this script is run directly or if i imported it from another module
root = tk.Tk() #Create the main window
app = CartoonifyApp(root) #Create an instance of the CartoonifyApp class managing everything related to the app's behaviour inside tkinter window
root.mainloop() #Starts the program and would close only after the window is closed
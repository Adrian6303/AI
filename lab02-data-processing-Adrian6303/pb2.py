import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from PIL import Image, ImageFilter
import cv2

image_path = "data\images\chatGPT.png"

#a
def view_image(image_path):
    try:
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis('off') 
        plt.show()
    except Exception as e:
        print("Error:", e)


view_image(image_path)



#b

def resize_image(image_path, size=(128, 128)):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        return img
    except Exception as e:
        print("Error:", e)


image_directory = "data\images"


image_files = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]


resized_images = [resize_image(img_file) for img_file in image_files if resize_image(img_file)]


num_images = len(resized_images)
num_cols = 4
num_rows = -(-num_images // num_cols)  


fig, axes = plt.subplots(num_rows, num_cols)


plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

for i, ax in enumerate(axes.flat):
    ax.axis('off') 
    if i < num_images:
        ax.imshow(resized_images[i])
    else:
        ax.set_visible(False)  

plt.show()

#c
def view_image_grayscale(image_path):
    try:
        img = Image.open(image_path)
        img_gray = img.convert('L') 
        plt.imshow(img_gray, cmap='gray') 
        plt.axis('off') 
        plt.show()
    except Exception as e:
        print("Error:", e)

view_image_grayscale(image_path)

#d

def view_blurred_image(image_path, kernel_size):
    try:
        img = Image.open(image_path)
        blurred_img = img.filter(ImageFilter.GaussianBlur(kernel_size))
        
        _, axs = plt.subplots(1, 2, figsize=(10, 5))
        
        axs[0].imshow(img)
        axs[0].axis('off')
        axs[0].set_title('Original Image')
        
        axs[1].imshow(blurred_img)
        axs[1].axis('off')
        axs[1].set_title(f'Blurred Image')
        
        plt.show()
    except Exception as e:
        print("Error:", e)


kernel_size = 5  
view_blurred_image(image_path, kernel_size)

#e


def apply_canny_edge_detection(image_path):
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Apply Canny edge detection
        edges = cv2.Canny(img, 100, 200)  # Adjust threshold values as needed
        return edges
    except Exception as e:
        print("Error:", e)


image_path = "data\images\Turing.webp"

def indent_image(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        indented_img = apply_canny_edge_detection(image_path)

        _, axs = plt.subplots(1, 2, figsize=(10, 5))
        
        axs[0].imshow(img)
        axs[0].axis('off')
        axs[0].set_title('Original Image')
        
        axs[1].imshow(indented_img)
        axs[1].axis('off')
        axs[1].set_title(f'Indented Image')
        
        plt.show()
    except Exception as e:
        print("Error:", e)


indent_image(image_path)

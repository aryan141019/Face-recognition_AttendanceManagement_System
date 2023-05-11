import tkinter as tk
import cv2
from PIL import Image, ImageTk

def comaptible_image_format(path, size=(30,30)):
    img_button = Image.open(path)
    img_button = img_button.resize(size)
    img_photo = ImageTk.PhotoImage(img_button)
    #img_button.close()
    #path=''
    return img_photo
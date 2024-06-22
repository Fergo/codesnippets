import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL.ImageChops import invert
import sys
import os

root = tk.Tk()
root.withdraw()

def extract():
    file = filedialog.askopenfilename(title=f"Select image")

    image = Image.open(file)
    if len(image.getbands()) == 3:
        bands = image.split()

        ch = ['R', 'G', 'B']
        for i, band in enumerate(bands):
            new_file = f'{os.path.splitext(file)[0] + f"_{ch[i]}" + os.path.splitext(file)[1]}'

            band.save(new_file)


def combine():
    files = []
    images = []

    for ch in ['R', 'G', 'B']:
        files.append(filedialog.askopenfilename(title=f"Select image for channel {ch}"))

    for file in files:
        image = Image.open(file)
        if len(image.getbands()) > 1:
            image = image.convert('L').getchannel(0)

        images.append(image)

    composed = Image.merge('RGB', (images[0], images[1], images[2]))
    composed.save(filedialog.asksaveasfilename(title=f"Save combined file"))

# extract()
# combine()

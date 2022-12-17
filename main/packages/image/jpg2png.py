"""
Python Imaging Library (expansion of PIL) is the de facto 
image processing package for Python language
Convert jpg to png
"""

import os, pathlib
from PIL import Image # Look Here

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

a = Image.open("01.jpg")    # .jpg
b = Image.open("02.jpeg")   # .jpeg
print(a.format)             # JPEG
print(b.format)             # JPEG

a.save("03.png")            # Look Here
c = Image.open("03.png")    # .png
print(c.format)             # PNG
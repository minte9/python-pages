"""
Python Imaging Library (expansion of PIL) is the de facto 
image processing package for Python language
Convert jpg to png
"""

import os, pathlib
from PIL import Image       # Look Here

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

a = Image.open("files/01.jpg")
a.save("files/02.png") # Look Here

b = Image.open("files/02.png")
print(a.format) # JPEG
print(b.format) # PNG
"""
Python Imaging Library (expansion of PIL) is the de facto 
image processing package for Python language
Convert jpg to png
"""

import os, pathlib
from PIL import Image # Look Here

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

a = Image.open(DIR / "01.jpg")
b = Image.open(DIR / "02.jpeg")

a.save(DIR / "03.png") # Look Here

c = Image.open(DIR / "03.png")

print(a.format) # JPEG
print(b.format) # JPEG
print(c.format) # PNG
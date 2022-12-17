"""
Python Imaging Library (expansion of PIL) is the de facto 
image processing package for Python language
Convert jpg to png
"""

import os, pathlib
from PIL import Image # Look Here

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

a = Image.open(DIR / "01.jpg")  # .jpg
b = Image.open(DIR / "02.jpeg") # .jpeg

print(a.format) # JPEG
print(b.format) # JPEG

a.save(DIR / "03.png") # Look Here
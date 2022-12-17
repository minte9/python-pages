"""
Python Imaging Library (expansion of PIL) is the de facto 
image processing package for Python language
Convert jpg to png
"""

import os, pathlib
from PIL import Image

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

img = Image.open(DIR / "01.jpeg")
img.save(DIR / "01.png")

print(Image.open(DIR / "01.png").format)
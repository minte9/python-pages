"""Image to text
Open Cv (Open Source Computer Vision Library) used to load images.
Tesseract used for optical character recognition.
"""
import os
DIR = os.path.dirname(os.path.realpath(__file__))

import cv2, pytesseract
img = cv2.imread(DIR + '/files/01.png')
text = pytesseract.image_to_string(img)

print(text)
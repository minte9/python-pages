"""Image to text
Get only highlighted text
"""
import os
import cv2, pytesseract
import numpy as np

DIR = os.path.dirname(os.path.realpath(__file__))
img = cv2.imread(DIR + '/files/01.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert BGR to HSV

# Range of yellow color in HSV
lower = np.array([22, 93, 0]) 
upper = np.array([45, 255, 255])

# Mask to get only yellow colors
mask = cv2.inRange(hsv, lower, upper)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img, img, mask= mask)

# Invert the mask to get black letters on white background
res2 = cv2.bitwise_not(mask)

text = pytesseract.image_to_string(img)
highlighted = pytesseract.image_to_string(res2).strip()
modified = text.replace(highlighted, f'<i>{highlighted}</i>').strip()

print(modified)

# display image
cv2.imshow("img", res)
cv2.imshow("img2", res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
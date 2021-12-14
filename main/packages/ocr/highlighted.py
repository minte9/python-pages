"""Image to text
Get only highlighted text
"""
import os
import cv2, pytesseract
import numpy as np
DIR = os.path.dirname(os.path.realpath(__file__))
DEBUG = False

def imread_highlighted(img):

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

    # Range of yellow color in HSV
    lower = np.array([22, 93, 0]) 
    upper = np.array([45, 255, 255])

    # Mask to get only yellow colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask= mask)

    # Invert the mask to get black letters on white background
    res2 = cv2.bitwise_not(mask)

    # Display images
    if DEBUG:
        cv2.imshow("img", res)
        cv2.imshow("img2", res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return res2


img = cv2.imread(DIR + '/files/02.png')
img2 = imread_highlighted(img)

text = pytesseract.image_to_string(img).strip()
highlighted = pytesseract.image_to_string(img2).strip()
replaced = text.replace(highlighted, '<i>%s</i>' % highlighted)

print('Text: \n' + text, '\n')
print('Highlighted: \n' + highlighted, '\n')
print('Replaced: \n' + replaced, '\n')

"""
Text: 
where it was writing some big file. We took really
good advantage of multithreading in Java, which
was less painful than I had expected it to be. It was
just really pleasant to work on. From the API we
had designed we saw all these directions it could
grow. 

Highlighted: 
We took really
good advantage of multithreading in Java, which
was less painful than I had expected it to be, It was
just really pleasant to work on. 

Replaced: 
where it was writing some big file. We took really
good advantage of multithreading in Java, which
was less painful than I had expected it to be. It was
just really pleasant to work on. From the API we
had designed we saw all these directions it could
grow. 
"""
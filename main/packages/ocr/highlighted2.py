"""Image to text - highlight mask
Some character might not be correctly detected, so we use only
first and last 20 chars of the highlighted string.
"""
import os, sys
import cv2, pytesseract, numpy
DIR = os.path.dirname(os.path.realpath(__file__))

def imread_highlighted(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convert BGR to HSV
    lower = numpy.array([22, 93, 0]) # yellow range
    upper = numpy.array([45, 255, 255])
    mask = cv2.inRange(hsv, lower, upper) # Mask to get only yellow colors
    res = cv2.bitwise_and(img, img, mask= mask)
    res2 = cv2.bitwise_not(mask) # Invert the mask
    return res2

for root, dirs, files in os.walk(DIR + '/files/'):
    for file in files:

        img = cv2.imread(DIR + '/files/' + file)
        img2 = imread_highlighted(img)

        text = pytesseract.image_to_string(img)
        highlighted = pytesseract.image_to_string(img2)
        
        text = '\n'.join(text.split('\n\n')).strip() # remove double newlines
        highlighted = '\n'.join(highlighted.split('\n\n')).strip()

        start = highlighted[0:20]
        end = highlighted[-20:]

        assert start in text
        assert end in text

        replaced = text.replace(start, '<i>%s' % start)
        replaced = replaced.replace(end, '%s</i>' % end)

        print(replaced + "\n")


"""
where it was writing some big file. <i>We took really
good advantage of multithreading in Java, which
was less painful than I had expected it to be. It was
just really pleasant to work on.</i> From the API we
had designed we saw all these directions it could
grow.

I've also done a lot of testing since LiveJournal.
<i>Once I started working with other people
especially. And once I realized that code I write
never fucking goes away and I'm going to be a
maintainer for life.</i> I get comments about blog
posts that are almost 10 years old. “Hey, I found
this code. I found a bug,” and I'm suddenly
maintaining code.

<i>When I'm just writing the first version of the
program, I tend to put everything in one file.
And then I start seeing structure in that file.</i>
Like there's this block of things that are pretty
similar, That's a thousand lines now, so why don't
I move that into another file. And the API sort of
builds up organically that way. The design process
"""
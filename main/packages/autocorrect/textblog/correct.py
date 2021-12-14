"""Text autocorrection with TextBlob package
"""
from textblob import TextBlob

text = """
As far as I am abl to judg, after long attnding to the sbject, 
the condiions of lfe apear to act in two ways—directly.
"""

blob = TextBlob(text)
correct = blob.correct()
print(correct)

# Is far as I am all to judge, after long attending to the subject, 
# the conditions of life appear to act in two ways—directly.

text = """
I remember coming wp 
"""

blob = TextBlob(text)
correct = blob.correct()
print(correct)
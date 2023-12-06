from textblob import TextBlob

text = """
As far as I am ablie to judg, after long attnding to the sbject, 
the condiions of lfe apear to act in two ways—directly.
"""

blob = TextBlob(text)
correct = blob.correct()

# Output corrected text
print(correct)

"""
    Is far as I am able to judge, after long attending to the subject, 
    the conditions of life appear to act in two ways—directly.
"""
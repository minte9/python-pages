"""Replace matched group
https://stackoverflow.com/questions/6711567/how-to-use-python-regex-to-replace-using-captured-group/6711631
"""
import re

text = 'end, Wrong punctuation.'
pattern = re.compile(r', ([A-Z])')
text = pattern.sub(r'. \1', text)
print(text)
    # end. Wrong punctuation.

text = 'excellence, excellence,'
pattern = re.compile(r',$')
text = pattern.sub(r'.', text)
print(text)
    # excellence, excellence.
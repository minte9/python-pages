"""Pyinputplus 
Contains functions similar to input() for other kind of data:
number, date, email, adress
Pyinputplus is not part of the standar distribution:
pip install pyinputplus
Import as pyip save us from typing pyinputplus every time.
"""
import pyinputplus as pyip

response = pyip.inputNum('What is your age? ', min=10, limit=4)
print(f'Your age is: {response}')
    # What is your age? 6
    # Number must be at minimum 10.
    # What is your age? -10
    # Number must be at minimum 10.
    # What is your age? abc
    # 'abc' is not a number.
    # What is your age? 5
    # Exception: pyinputplus.RetryLimitException

response = pyip.inputMenu(['dog', 'cat', 'horse'], lettered=True,
    prompt='What is your favorite animal? \n'
)
print(f'Your favorite animal is: {response}')
    # What is your favorite animal? 
    # A. dog
    # B. cat
    # C. horse
    # b
    # Your favorite animal is: cat
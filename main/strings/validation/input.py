"""Input validation:
We repeatedly ask user for input values.
"""

while True:
    age = input('What is your age? ')
    try:
        age = int(age)
    except:
        print('Please use numberic values!')
        continue
    if age < 0:
        print('Please enter a positive number!')
        continue

    break

print(f'Your age is: {age}')
    # What is your age? abc
    # Please use numberic values!
    # What is your age? -10
    # lease enter a positive number!
    # What is your age? 20
    # Your age is: 20
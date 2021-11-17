# Semantic error
#
# The program performs concatenation instead of addition
# The programmer failed to convert the inputs to integers

num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
sum = num1 + num2

if sum != int(num1) + int(num2):
    print("Sum = " + sum + " / Incorrect - Semantic error")

num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
sum = int(num1) + int(num2)

print("Sum = " + str(sum) + " / Correct")
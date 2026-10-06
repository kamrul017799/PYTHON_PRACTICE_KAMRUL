#Take a number as input and check whether it is positive, negative, or zero.
number = input()
number = int(number)
if number%2 == 0:
    print('positive')
elif number%2  != 0:
    print('negative')
elif number == 0:
    print('zero')

#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam =input()
spam = int(spam)
if spam == 1:
    print('hello')
elif spam == 2:
    print('howdy')

else:
    print('greting;')

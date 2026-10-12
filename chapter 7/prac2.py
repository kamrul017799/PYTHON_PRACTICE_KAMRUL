
#Create a dictionary containing five products and their prices. Ask the user to enter a product name and a new price, then update the dictionary and print it.
import sys
product = {'banana':50, 'date': 23,'juice':100, 'apple':100}

while True:
    guava = input('enter name: ')
    if guava == ' ':
        break
    print('not listed yet')
    value = input('enter value: ')
    product[guava] = value
    print(product)
    sys.exit()



    
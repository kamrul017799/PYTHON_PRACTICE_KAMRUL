#Create two functions where Function A calls Function B, and Function B calls Function C. Make each function print a message so you can observe the order in which they execute.


def functionA():
    print('this is function A')
    functionB()
    print('this is function A1')
def functionB():
    print('this is function B')
    functionC()
    print('this is function B1')
def functionC():
    print('this is function C')

functionA()

#Create a program with a global variable and a function that changes its value using the global statement. Print the value before and after calling the function.
vari = 'kamrul'
print(vari)

def func():
    global vari
    vari = 'hasan'

func()
print(vari)
   



     


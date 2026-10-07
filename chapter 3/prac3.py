#Take a number from the user and calculate the sum of all numbers from 1 to that number.
print('take a number')
num = int(input())
sum = 0
for i in range(1, num+1):
    
    sum = sum + i
    
print('the sum of total numbers is '+' '+str(sum))



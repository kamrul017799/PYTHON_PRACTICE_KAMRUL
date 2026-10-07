#Print the numbers 1 to 30, but skip all numbers that are divisible by 3 using continue.
for number in range(1,30,1):
    if number%3 == 0:
        continue
    print(number)
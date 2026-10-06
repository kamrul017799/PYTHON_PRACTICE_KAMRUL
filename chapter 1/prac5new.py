#Take the user's first name and last name as input. Print their full name and the length of the full name.
print('enter first name')
fname = input()
print('enter last name')
lname = input()
fullname = str(fname) + str(lname)
print('full name is ' + fullname + 'and the length of the name' + str(len(fullname)))

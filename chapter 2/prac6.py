#Take a username and password as input. Check whether they match a predefined username and password. Print "Login successful" or "Invalid login".
username = 'kamrul123@'
password = 'kamrul9876'
print('enter username')
user = input()
print('enter password')
passs = input()

if username == user and password == passs :
    print('login successful')
else :
    print('invalid login')
    


#Escape Sequences
print("hello'world")
print("Name\tAge")
print("He said \"Hi\"")

#raw string
print(r"Hello\nWorld")
print(r"C:\Users\Alice\Desktop")

#Multiline Strings
print('''Dear Alice,
Can you feed Eve's cat this weekend?
Sincerely,
Bob''')

#Multiline Comments

# Indexes and Slices

# new = "kamrul hasan bhuiyan?1"
print(len(new))
print(new[13:])
# in , not in
print('kamrul' in new)
print('345' in new)

#f string
name= 'american international university bangladesh'
loca = 'kuratoli , dhaka'
print(f'the name of my university is {name} and it located in {loca}')


#F-String Alternatives: %s and format()
name= 'american international university bangladesh'
loca = 'kuratoli , dhaka'
age = 23

print('my university is %s and located in %s'%(name,loca))

print('currently i am %s years old, next 10 year later i will  be %s '%(age, age+10))

me = 'kamrul hasan'
print('my name is {} and my age is {}. i will leave this country after {} year later'.format(me,age, age-22))

print('{1} year ago i was born and my parents decided called me name {0}'.format(me, age))


#Changing the Case
name = 'Hello word, it Ai Calling'
print(name.upper())
print(name.lower())

call =input('hey how was your day: ')
if call.lower() == 'great':
    print('work')
else:
  print('not warked')

print(name.islower())




#Checking String Characteristics

check = 'kamrul'
print(check.isalpha())
check1 = 'kamrul123'
print(check1.isalnum())
check2 = '123'
print(check2.isnumeric())
print(check2.isdecimal())
sp = ''
print(sp.isspace())
title = 'This The Title Of This Paper'
print(title.istitle())


while True:
    name = input('enter your name')

    if name.isdecimal():
        break
    print(name)
    break



# birthdays ={'alice':'apr 1','blice':'feb 12','slice':'mar 16'}
# while True:
#     name = input('enter name: ')
#     if name ==' ':
#         break

#     if name in birthdays:
#         print( birthdays[name]+ 'is the birhday of ' + name)
#     else:
#         print('i dont have birthday information about' + name)
#         print('what is their bithday')
#         bday = input('enter birth date: ')
#         birthdays[name] = bday
#         print('birthday database updated')



new = {'name':'kamrul','age': 23,'city':'dhaka'}\

# for i in new.items():
#     print(i)

# if 23 in new.values():
#     print('true')
# else:
#     print('false')

# print(list(new.keys()))

# for k,v in new.items():
#     print('key:' + str(k) + 'value: ' + str(v))

# print('I am  ' + str(new.get('name', 0)))

# print('my age is' + str(new.get('age',0)))

# picnic_items = {'apples': 5, 'cups': 2}
# #print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')

# if 'banana' not in picnic_items:
#     picnic_items['banana'] = 6
# print(picnic_items)


# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character,0)
#     count[character] += 1
# print(count)


all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
       num_brought = num_brought + v.get(item, 0)
    return num_brought
print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))







# string = input('enter the sentence: ')

# #words = string.split()

# for word in string:
#     if word.isnumeric():
#         print(word)
#         break


# text = "I have 25 books and 10 pens."

# words = text.split()

# for word in words:
#     if word.isdigit():
#         print(word)
#         break



# #Write a program that extracts all numbers from a string

# word = input('enter sentence: ')
# dic =[]
# text = word.split()

# for w in text:

#     if w.isnumeric():
#         dic.append(w)

# print(dic)




# #Write a program that finds all phone numbers in a text using regular expressions.
# text = 'my phone number is 0177001333 and my fnd number is 01892332489'
# li = []
# word = text.split()
# for w in word:
#     if w.isnumeric():
#         li.append(w)

# print(li)
        
       
# #Write a program that replaces every occurrence of the word "Python" with "Java" in a given string using

# program = input('Enter program: ')

# word = program.split()

# for w in word:
#     if w =='python' or w == 'java':
#         w.replace('python' , 'java')
#         print(program)
    






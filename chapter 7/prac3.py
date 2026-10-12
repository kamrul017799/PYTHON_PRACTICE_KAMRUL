#Ask the user to enter a string. Use a dictionary to count how many times each character appears in the string.

dic ={}


def count_s(st):
    for character in st:
        dic.setdefault(character,0)
        dic[character]= dic[character]+1

count_s('hello')
print(dic)

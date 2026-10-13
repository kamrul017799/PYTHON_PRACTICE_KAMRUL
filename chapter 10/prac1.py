#absolute path
from pathlib import Path

file_path = Path('D:/PYTHON PRACTICE/chapter 10/p.txt')

print(file_path.is_absolute())

# relative path

p = Path('notes.txt')

print(p.is_absolute())
 

# find directory

print(Path.cwd())

#home directory
print(Path.home())

#change directory
import os

os.chdir('C:/OneDriveTemp')
print(Path.cwd())

os.chdir('D:/PYTHON PRACTICE/chapter 10')
print(Path.cwd())

file_path = Path('D:/PYTHON PRACTICE/chapter 10/p.txt')
print(p.name)
print(p.stem)
print(p.suffix)


#Creating folders
# from pathlib import Path

# p = Path.home() / 'practice_folder'

# p.mkdir()

#Checking whether a path exists
p = Path('D:/PYTHON PRACTICE')

print(p.exists())
print(p.is_file())
print(p.is_dir())

#check file
p = Path('D:/PYTHON PRACTICE/chapter 10/p.txt')

print(p.exists())
print(p.is_file())

#check file size

p = Path('D:/PYTHON PRACTICE/chapter 9/prac3.py')

info = p.stat()

print(info.st_atime)

# Finding files using glob patterns


folder = Path.home()

for file in folder.glob('*.txt'):
    print(file)

files = list(folder.glob('*.txt'))

print(files)


# Reading and writing files


p = Path('D:/PYTHON PRACTICE/chapter 10/p.txt')

p.write_text('Hello, dhaka!', encoding='utf-8')

content = p.read_text(encoding='utf-8')

print(content)


#read using open()
file_obj = open('p.txt', 'r', encoding='utf-8')

content = file_obj.read()

file_obj.close()

print(content)

#write \n line 
file_obj = open('message.txt', 'w', encoding='utf-8')

file_obj.write('First line\n')
file_obj.write('Second line\n')
file_obj.write('Third line')

file_obj.close()

with open('message.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('I am learning Java.')

with open('message.txt', 'a', encoding='utf-8') as file_obj:
    file_obj.write('\nPython is also useful.')



import shelve

shelf_file = shelve.open('mydata')

shelf_file['student'] = {
    'name': 'Kamrul',
    'marks': [80, 85, 90]
}

shelf_file.close()


shelf_file = shelve.open('mydata')

print(shelf_file['student'])

shelf_file.close()
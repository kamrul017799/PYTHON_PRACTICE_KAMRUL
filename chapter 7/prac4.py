# Create a dictionary containing the names and marks of five students. Write a program to:




stu_details ={'kamrul': 80,'hasan':86,'bhuiyan':70,'kam':90,'has':95}



# Print each student's name and marks.
for k,v in stu_details.items():
    print('key ' + str(k) + ' and mark is ' + str(v))


# Find the student with the highest marks.

high = 0
top_student = ''
for k,v in stu_details.items():
       if  v> high:
           high = v
           top_student = k
print(top_student)

# Calculate the average marks.
all_mark = stu_details.values()
sum = 0
for v in stu_details.values():
     sum = sum+v
print(sum)
     
avarage = sum/ len(stu_details)
print(avarage)

# # Count how many students passed (marks 40 or above)


for v in stu_details.values():
     if v > 40:
          print(len(stu_details))
          break





        


    






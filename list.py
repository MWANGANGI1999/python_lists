#creating a list of students
Student = ["Stephen", "Gabriel", "Julius","Teddy","Leroy","Collins"]

print(Student)
#indexing
#displays the first student in the list
print(Student[0])
#displays the second student in the list
print(Student[1])
#displays the fifth student starting from the back of the list upto the second last student in the list
print(Student[-5:-1])
#displays the second student in the list to then fifth student
print(Student[2:5])
#displays the from the second student in the list upto the last student
print(Student[2:])
#displays the from the fifth student in the list back to the  student
print(Student[:5])

#replacing an existing with a new student
Student[3]= "Grace"
Student[0]= "Mwangangi"
Student[1]= "Kyalo"
Student[5]= "Sossie"
print(Student)

#looping through the list
for Student in Student:
  print(Student)

#check if item exists
if "Mwangangi" in Student:
    print("Mwangangi is there")

#methods
#len(),append(),insert(),pop()
print(len(Student))

#append()-adds an item
Student.append("Esther")
print(Student)
#insert()-inserts an item
Student.insert(3,"Omar")
print(Student)
#remove()-removes the specified item
Student.remove("Julius")
print(Student)
#pop()-removes the specified index
Student.pop()
print(Student)
#del-removes the specified index
del Student[0]
print(Student)

#clear()-empties the list
Student.clear()
print(Student)

#reverse()-Reverse the order of the student list
Student.reverse()
print(Student)

#sort()-sorts the list ascending by default
Student.sort()
print(Student)

#creating an empty list
Student = [""]

print(Student)


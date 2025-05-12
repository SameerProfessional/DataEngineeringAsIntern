# Create a list of student names and insert a new student name before the last student.

Student_names = [] # Initialized the empty list 

# Take the input of the number of students 
count = int(input("Enter the number of students : "))

student_name = '' # Initialized the empty student_name variable

# Take the input of all the students 

for i in range(count): # Loop from 0 to count-1
    student_name = input("Enter the name of the student : ")
    Student_names.insert(i, student_name)

# Elements of the Student_names list are 
print("Names of the student in the student list are :", Student_names)

# Take input the name of new student 

new_student = input("Enter the name of the student : ")

# Insert a new student name before the last student name

Student_names.insert(-1, student_name)

# Get the name of all students

print("Elements of the list are :", Student_names)





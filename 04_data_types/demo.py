# Data Types 

# Numeric Types 

data = 10 
print(type(data))

data = -10 
print(type(data))

data = 10.5 
print(type(data))

data = -10.5 
print(type(data))

data = 0.0
print(type(data))

# complex: In maths we have a + ib 
# data = 3 + i5 # Error
# print(type(data))

# complex: In Python we have a + bj
data = 3 + 5j
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None 
print(type(data))

data = "python"
print(type(data))

# Complex Data Types 

# List 
data = [1,2,3,4,5]
print(type(data))

# Tuples 
data = (1,2,3,4,5)
print(type(data))

# Sets 
data = {1,2,3,4,5}
print(type(data))

# FrozenSet
data = frozenset({1,2,3,4,5})
print(type(data))

# Dictionary
data = {"name":"Ravi","course":"python","time":10}
print(type(data))

# Custom Data Types

# data = Student() # NameError: name 'Student' is not defined
# print(type(data))

class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_enrolled_courses = ["Python","DevOps","AI"]
    student_enrolled_courses_prices = (10000,20000,30000)
    
data = Student()
print(type(data))
# print(student_name) # NameError: name 'student_name' is not defined
print("Student Name: ", data.student_name)
print("Student Enrolled First Course: ", data.student_enrolled_courses)
print("Student Enrolled First Course: ", data.student_enrolled_courses[0])

# Type Conversion & Type Casting 
n1 = 10
n2 = 5.5 
sum = n1 + n2 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
n1 = 10.5 
n2 = int(n2)
print(n2)
print(type(n2))
print(type(n1))

#  Some User in a web site was filling some form (text boxes) --> Behind the scenes these are strings
rating = "4"

# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
if rating >= 4:
    print("Positive Feedback")
else:
    print("Negative Feedback")
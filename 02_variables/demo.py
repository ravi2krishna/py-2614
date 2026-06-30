# Variables

# Assign Data (Store Data)
student_name = "Ravi"
student_age = 25 
student_gpa = 9.3
student_passed = True 
STUDENT_AADHAR = None # Absence of value

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(STUDENT_AADHAR)

# Concatenation: Combining / Joining Strings Using + Operator  
print("Student Name: "+student_name)
# print("Student Age: "+student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ",student_age)
print("Student GPA: ",student_gpa)
print("Student Passed: ",student_passed)
print("Student Aadhar: ",STUDENT_AADHAR)

print("=====================")

# type(): Used To tell data type 
type(student_name)
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(STUDENT_AADHAR))

print("=====================")

# id(): Used To tell Memory Address Of Variable 
id(student_name)
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(STUDENT_AADHAR))

print("=====================")

# Memory Model In Python 
value_x = 10 
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10 
print(id(value_z))
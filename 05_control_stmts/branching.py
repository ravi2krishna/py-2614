# Branching Structures (Jump Statements)

for num in range(1,11,1):
    print(num)
    
print("===================")

# break - Helps to exit the loops
for num in range(1,11,1):
    if num == 5:
        break 
    print(num)
    
print("===================")

# continue: Helps to skip the current iteration
for num in range(1,11,1):
    if num == 5:
        continue 
    print(num)
    
print("===================")

# pass: Acts as a placeholder, does nothing 
# Requirement - To Perform Some Operation in the future 

# emp_salary = 15000
# if emp_salary > 25000:
    # i want to do something not now, but in future 
    # IndentationError: expected an indented block after 'if' statement on line 28

emp_salary = 15000
if emp_salary > 25000:
    pass 

# After 6 Months You Decided, When Salary is above 25000
# Promote To Associate Software Engineer
emp_salary = 35000
if emp_salary > 25000:
    print("Employee Promoted To Associate Software Engineer")
    
print("===================")

# Working With OOP 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_enrolled_courses = ["Python","DevOps","AI"]
    student_enrolled_courses_prices = (10000,20000,30000)
    
class Trainer:
    pass 

class Mentor:
    pass 

class Institute:
    institute_name = "Digital Institute"
    institute_email = "digital@gmail.com"
    
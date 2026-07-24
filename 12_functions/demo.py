# Functional Programming 

# Without Functions 

# User One, who wants to calculate for below values 
num1 = 10
num2 = 5

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# User Two, who wants to calculate for below values 
num1 = 20
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# User Three, who wants to calculate for below values 
num1 = 200
num2 = 50

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)   

# User One, who wants to calculate for below values 
num1 = 10
num2 = 5
math_ops()
print("=" * 10)

# User Two, who wants to calculate for below values 
num1 = 20
num2 = 5
math_ops()
print("=" * 10)

# User Three, who wants to calculate for below values 
num1 = 200
num2 = 50
math_ops()
print("=" * 10)

# math_ops(10,5) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# Functions With Parameters 
def math_ops(num1, num2): # num1, num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)   

# User One, who wants to calculate for below values 
math_ops(10,5) # 10,5 are arguments 
print("=" * 10)

# User Two, who wants to calculate for below values 
math_ops(20,5)
print("=" * 10)

# User Three, who wants to calculate for below values 
math_ops(200,50)
print("=" * 10)

# Process Data 
def process_string(email_id):
    print(email_id.lower()+"@gmail.com")

process_string("RAvi")

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info("Hyderabad","Ravi","ravi@gmail.com")
employee_info("Ravi","ravi@gmail.com","Hyderabad")

print("=" * 50)
    
# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi@gmail.com")
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")

print("=" * 50)

# Without Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",org_name="IBM")    
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com",org_name="IBM")    
employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com",org_name="IBM")    

print("=" * 50)

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="IBM"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")    
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com")    
employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com")
employee_info(emp_location="USA",emp_name="Mark",emp_email="mark@gmail.com",org_name="META")

# Placement Requirement: Default arguments
# def employee_info(emp_name,emp_email,emp_location,org_name="IBM",emp_mobile): 
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# Non-default argument follows default argumentPylance

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="IBM"): 
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
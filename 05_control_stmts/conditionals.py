# Conditional Structures (Decision Making Statements) 

# if - Runs a block of code, if the condition is True 

if True:
    print("this")
    print("is")
    print("block")
    print("of")
    print("code")
    
print("===================")

if False: # Code is not analyzed because condition is statically evaluated as false
    print("this")
    print("is")
    print("block")
    print("of")
    print("code")
    
print("===================")

if 5 > 2:
    print("Yes 5 > 2 is True")
    
print("===================")

if 5 < 2:
    print("NO 5 < 2 is Not True")
    
print("===================")

num = 10 
if num > 0:
    print("Given Number is Positive")

num = -10 
if num < 0:
    print("Given Number is Negative")
    
print("===================")

# if else - Runs a block of code, if the condition is True 
# Runs another block of code, if the condition is False 

num = -10 
if num > 0:
    print("Given Number is Positive")
else:
    print("Given Number is Negative")
    
print("===================")

# Without input(), data is static 
name = "Ravi" 
print(name) # This is fixed i.e static 

print("===================")

# With input(), data is Dynamic 
name = input("Enter Your Name: ")
print(name) # This is Dynamic 

print("===================")

# With input() and Interpolation Using "f-strings"
username = input("Enter Your Username: ")
print("Welcome To Python Sessions " +username) # This is Dynamic 
print("Welcome To Python Sessions ",username) # This is Dynamic 
print("Welcome To Python Sessions username") # This is Static 
print("Welcome To Python Sessions {username}") # This is Static 
print(f"Welcome To Python Sessions {username}") # This is Dynamic 

print("===================")

# Making It Dynamic
num = int(input("Enter Number: "))
# if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
if num > 0: # Do Type Casting
    print(f"Given Number {num} is Positive")
else:
    print(f"Given Number {num} is Negative")
    
print("===================")

# Voting App 
age = int(input("Enter Your Age: ")) 
if age >= 18:
    print("You Can Vote")
else:
    print(f"You Cannot Vote, You are Still {age} Years Only")
    
print("===================")


# Conditional Expression - Evaluates Conditional and returns one of the two values 
# based on whether Condition is True or False 
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age Again: ")) 
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)

print("===================")

# if else - Pass or Fail
marks = int(input("Enter Marks: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED")
    
# elif ladder - Grades 
marks = int(input("Enter Marks: "))
if marks >= 75:
    print("A Grade")
elif marks >= 65:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
elif marks >= 30:
    print("D Grade")
else:
    print('Fail')
    
print("===================")

# match case - You are comparing one variable, Against fixed constant values

error_code = int(input("Enter Error Code: "))
match error_code:
    case 200:
        print("Success - OK")
    case 404:
        print("Error - Not Found")
    case 503:
        print("Error - Service Unavailable")
    case _:
        print("Unknown Error Code")
        
print("===================")

role = input("Enter Your Role: ")
match role:
    case "developer":
        print("Write Code")
    case "admin":
        print("Install Server")
    case "devops":
        print("Setup CI/CD Pipeline")
    case _:
        print("Invalid Role") 
        
print("===================")   
    
# Exception Handling 

# When No Errors -> Nothing To Handle 

print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ",num1/num2)

print("Program Execution Completed")

print("=" * 50)

# # Let's add some issues

# print("Program Execution Started")

# num1 = 10
# num2 = "5"

# print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("Program Execution Completed")

# print("=" * 50)

# Let's add some issues -> With Exception Handling
print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING! Don't Divide Numerics With Strings")
print("Program Execution Completed")

print("=" * 50)


# Let's add some issues -> With Exception Handling
print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING! Don't Divide Numerics With Strings")
print("Program Execution Completed")

print("=" * 50)

# # Classic Exception 
# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ",num1/num2) # ZeroDivisionError: division by zero

# print("Program Execution Completed")

# print("=" * 50)


# Classic Exception 
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! Check Here - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# Multiple Exceptions 
print("Program Execution Started")

# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data: # 1/1, 1/2, 1/three, 1/0, 1/4 
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50)

# Multiple Exceptions 
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data: # 1/1, 1/2, 1/three, 1/0, 1/4 
    try:
        print(1/num)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except:
        print("OOPS! Something Went Wrong!!!!")

print("Program Execution Completed")

print("=" * 50)

# Multiple Exceptions Handling
print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data: # 1/1, 1/2, 1/three, 1/0, 1/4 
    try:
        print(1/num)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except TypeError:
        print("WARNING! Don't Divide Numerics With Strings")
    except ZeroDivisionError:
        print("OOPS! Check Here - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# else 
print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ",num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't Divide Numerics With Strings")
else: # if No Exception was raised in try block
    print("Calculation Was Successful") # Then Only Check OTP
    
print("Program Execution Completed")

print("=" * 50)

# finally 
print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't Divide Numerics With Strings")
else: # if No Exception was raised in try block
    print("Calculation Was Successful") # Then Only Check OTP
finally:
    print("Closing All Opened File Streams & Database Connections") 
print("Program Execution Completed")

print("=" * 50)

# raise 
# CustomErrors 
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
print("=" * 50)

# CustomErrors for voting app 
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
    # raise UnderAgeError("Below 18 Cannot Vote")
else:
    print("You Can Vote")
    
    
# CustomErrors 
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
print("=" * 50)

# CustomErrors for voting app 
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Age: "))
try:
    if age < 18:
        raise UnderAgeError("Below 18 Cannot Vote")
except:
    print("You are not 18 Yet")
else:
    print("You Can Vote")
finally:
    print("Closing Program")
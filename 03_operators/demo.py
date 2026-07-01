# Operators

# Arithmetic Operators 
num1 = 10
num2 = 5 

print("Sum Of Numbers: ", num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ", num1 * num2)
print("Division Of Numbers: ", num1 / num2)
print("Modulus Of Numbers: ", num1 % num2)

print("Floor Division Of Numbers: ", num1 // num2)

print("Division Of Numbers: ", 3/2 )
print("Floor Division Of Numbers: ", 3//2 )

print("Exponentiation Of Numbers: ", 3 ** 2 ) # 3 ^ 2

print("=======================")

# Compound Assignment Operators 
num = 10
num = num + 5 # Long Form 
print(num) 

num = 10
num += 5 # Short Form 
print(num) 

# ++ Increment (Increases the value)
count = 0
print(count)
# count++ # SyntaxError: invalid syntax
count += 1 # Incrementing
print(count)

# -- Decrement (Decreases the value)
count = 10
print(count)
# count-- # SyntaxError: invalid syntax
count -= 1 # Incrementing
print(count)

print("=======================")

# Comparison Operators 
num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)

print("=======================")

# Logical Operators 

num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num2 > num4) # T and T -> T 
print(num1 > num2 and num2 < num4) # T and F -> F

print(num1 > num2 or num2 < num4) # T or F -> T
print(num1 < num2 or num2 < num4) # F or F -> F

print(num1 > num2) # T
print(not num1 > num2) # F

print("=======================")

# Membership Operators
data = "python is interpreted language"
find_word = "java"

status = find_word in data 
print(status)

data = "python is interpreted language"
find_word = "python"

status = find_word in data 
print(status)

data = "python is interpreted language"
find_word = "java"

status = find_word not in data 
print(status)

# List Data Type -> Complex Data Type, To Store Multiple Values, represented using []
employee_ids = ["101","102","103","104","105","100000"]
find_emp_by_id = "108"

status = find_emp_by_id in employee_ids

print("Employee Found: ",status)

employee_ids = ["101","102","103","104","105","100000"]
find_emp_by_id = "103"

status = find_emp_by_id in employee_ids

print("Employee Found: ",status)


print("=======================")

# Identity Operators

value_x = 10 
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10 
print(id(value_z))

print(value_x is value_y)

print(value_x is value_z)

print("=======================")

# Bitwise Operators

n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000001
       # 0000000000000111
       
print(n1 & n2) # 1
print(n1 | n2) # 7

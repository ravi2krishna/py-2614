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

print("=" * 50)    
    
# Without Arbitrary Positional Arguments
def add_numbers_one(n1):
    print(n1)
    
def add_numbers_two(n1,n2):
    print(n1+n2)
    
def add_numbers_three(n1,n2,n3):
    print(n1+n2+n3)
    
add_numbers_one(10)
add_numbers_two(10,20)
add_numbers_three(10,20,30)

# add_numbers_three(10,20,30,40,50) # TypeError: add_numbers_three() takes 3 positional arguments but 5 were given

print("=" * 50)   

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(10)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50)

def add_numbers(*numbers):
    for num in numbers:
        print(num)

add_numbers(10,20,30,40,50)

def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Total Sum is {total}")    
    
add_numbers(10)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50)

def profile(*info):
    print(info)
    
profile("ravi","krishna")
profile("jon","doe",9090909090)

# Real World Use Case w.r.t Ecommerce Applications Cart Functionality 
def cart_total_value(*products):
    total = 0
    for product in products:
        total += product
    print(f"Total Cart Value is ₹ {total}")    

cart_total_value(1299,599,1899)

print("=" * 50)   

# Arbitrary Keyword Arguments
def profile(**info):
    print(info)
    
profile(fname="ravi",lname="krishna")
profile(fname="ravi",lname="krishna",mobile=90909090)

def profile(**info):
    for data in info:
        # print(data) # keys 
        print(info[data]) # value = dict['key']

profile(fname="ravi",lname="krishna",mobile=90909090)

print("=" * 50)   

# Real World Use Case -> jan=3000, feb=4500, mar=9000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000, may=3000
# Requirement: Calculate Total Transaction Amount and Number Of Transactions Made

def bank_transactions(**transactions):
    print(transactions)
    total_transactions_value = 0
    number_of_transactions = 0
    for transaction in transactions: # jan, feb etc 
        total_transactions_value += transactions[transaction] # 3000, 4500 etc 
        number_of_transactions += 1 
    print(f"Total Transactions Amounts To {total_transactions_value} For {number_of_transactions} Transactions")
        
bank_transactions(jan=3000, feb=4500, mar=9000)
bank_transactions(jan=3000, feb=4500, mar=9000, apr=6000, may=3000)
    
    
print("=" * 50)   

# Without return 

def add(a,b):
    a + b 
    
add(10,20)
print(add(10,20))

# Without return 
def add(a,b):
    return a + b 

add(10,20)

b = add(10,20)
print(b)

print(add(100,200))

# Problem 
# def add(a,b):
#     print(a + b)
    
# # function composition 
# def sub(c,d,e): # add c & d then minus - e --> c + d - e
#     print(add(c,d) - e)

# sub(3,4,5)  

# Solution 
def add(a,b):
    return a + b
    
# function composition 
def sub(c,d,e): # add c & d then minus - e --> c + d - e
    print(add(c,d) - e)

sub(3,4,5)  

# return - make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started")
    return a + b # last part of statement to be executed
    print("Calculation Completed") # Code is structurally unreachable
    
print(add(100,40))

a = 50
b = 60
a = 70
print(a) 

# multiple return statements --> first return will be considered
def math_ops(a,b):
    return a + b 
    return a - b
    return a * b
    
print(math_ops(10,20))

# multiple returns are present, and used with conditionals, you can control the flow 
def math_ops(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        return "Invalid Operator"

print(math_ops(1,2,"+"))
print(math_ops(100,200,"*"))
print(math_ops(5,10,"$"))

# Local Scope
def add():
    la = 10 # local variable declared "inside the function" 
    lb = 20 # local variable declared "inside the function" 
    print(la)
    print(lb)
    
add()
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
# print(lb)

def add(la,lb): # local variable declared "inside the function" 
    print(la)
    print(lb)
    
add(40,50)

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

# Global Scope
ga = 100
def add(la,lb): # local variable declared "inside the function" 
    print(la)
    print(lb)
    print(ga) # Global variable accessed within function
    
add(80,90)
print(ga)

# name conflicts
ga = 500
def add(la,lb,ga): # local variable declared "inside the function" 
    print(la)
    print(lb)
    print(ga)

add(1,2,3)
print(ga)

ga = 500
def add(la,lb,ga): # local variable declared "inside the function" 
    print(la)
    print(lb)
    print(ga) # access local variable ga
    print(globals()['ga']) # access global variable ga 
    
add(4,5,6)

# global variable outside the function 
count = 0 # global variable
print(count)
count += 1
print(count)

# global variable inside the function 
count = 0 # global variable
print(count)
def increment():
    global count 
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count

print(increment())

# Without Lambda Functions 
def add(a,b):
    return a + b 
print(add(200,300))

# With Lambda Function
# lambda arguments:expression 
lambda a,b:a + b # lambda expression 
print((lambda a,b:a + b)(1,2)) # IILE

# Without Lambda Functions 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 
    
print(is_even_num(11))
print(is_even_num(10))

# With Lambda Function
# lambda arguments:expression 
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0)(13))
print((lambda num:num % 2 == 0)(12))

# Without Lambda Functions 
# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")

# With Lambda Function
# lambda arguments:expression 
lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
# print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"))(emp_location="Hyderabad",emp_name="Mike",emp_email="mike@gmail.com"))
print((lambda emp_name,emp_email,emp_location:(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"))(emp_location="Hyderabad",emp_name="Mike",emp_email="mike@gmail.com"))

# Without Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]

def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num) 
    return squared_list

print(square_list([1,2,3,4,5]))


# With Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
# map(function, iterable)
(lambda num:num*num)
map((lambda num:num*num), [1,2,3,4,5])
print(map((lambda num:num*num), [1,2,3,4,5]))
print(list(map((lambda num:num*num), [1,2,3,4,5])))

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Requirement: find me prices after discounts

prices_after_discounts = []
for product in products:
    print(product)
    price = product['price']
    print(price)
    discount = product['discount']
    print(discount)
    
    price_after_discount = price - (price * discount / 100)
    print(price_after_discount)
    prices_after_discounts.append(price_after_discount)
    
print("Prices After Discount: ",prices_after_discounts)

# Requirement: find me prices after discounts Using Higher Order Function map()
print("=" * 50)
print(list(map((lambda product:product['price'] - product['price'] * product['discount'] / 100), products)))

print("=" * 50)

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Requirement: Find the Premium Products i.e product with price above 25000
# https://miro.medium.com/v2/resize:fit:1200/1*Jf5GJS1XtRsHWbZldcvOiQ.png
# Without filter() - Imperative Approach - What To Do 

premium_products = []

for product in products:
    # print(product)
    price = product['price']
    if price > 25000:
        print(product)
        premium_products.append(product)
        
print("All Products: ",products)

print("=" * 50)

print("Premium Products: ",premium_products)
    
print("=" * 50)
    
# Requirement: Find the Premium Products i.e product with price above 25000
# https://miro.medium.com/v2/resize:fit:1200/1*Jf5GJS1XtRsHWbZldcvOiQ.png
# With filter() - Declarative Approach - How To Do 
# filter(function, iterable)
print("With Filter")
print(filter((lambda product:product['price'] > 25000), products))
print(list(filter((lambda product:product['price'] > 25000), products)))

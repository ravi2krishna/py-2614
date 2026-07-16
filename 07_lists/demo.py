# Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# List With Numeric Data 
data = [10,20,30,40,50]
print(data)

# List With Text Data 
data = ["python","ai","cloud"]
print(data)

# List With Mixed Data 
data = [10,20,30,"python","ai",5.5,True]
print(data)

# Accessing Data In Lists 
data = [10,20,30,40,50]
print(data)

# first element 
first_element = data[0]
print(first_element)

# last element
last_element = data[-1]
print(last_element)

# Index out of range leads to Index Error
# unknown_element = data[10] # IndexError: list index out of range
# print(unknown_element)

# Slicing is same as strings 
data = [10,20,30,40,50]
print(data)
print(data[1:3:1]) # 20,30

# Access Individual Elements 
data = [10,20,30,40,50]
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Elements -> 10k elements 
data = [10,20,30,40,50,100000]
print(data)
print(data[0])
print(data[1])

# Applying Loops Access Individual Elements -> 10k elements 
data = [10,20,30,40,50,100000]
for num in data:
    print(num)
    
# Operators We Can Apply -> Requirement: Multiply Each Number with 10 
data = [10,20,30,40,50,100000]
for num in data:
    print(num * 10)

# Requirement: Give Courses in Upper Case
data = ["python","ai","cloud"]
for course in data:
    print(course.upper())
    
# Conditionals We Can Apply -> Requirement: Give Only Even Numbers 
data = [10,20,35,45,50]
for num in data:
    if num % 2 == 0:
        print(num)
        
# Duplicates Allowed 
data = [10,20,30,10,40,30,50]
print(data)

# Insertion Order Is Preserved 
data = [10,20,30,10,40,30,50]
print(data)

# List Operations / Methods
print(dir(data))
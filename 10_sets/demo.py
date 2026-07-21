# Sets

# empty set 
empty_set = {} # This is Dictionary, Empty Set Cannot be created with {}
print(empty_set)
print(type(empty_set))

empty_set = set()
print(empty_set)
print(type(empty_set))

# Set With Numeric Data 
data = {10,20,30,40,50}
print(type(data))
print(data)

# Set With Text Data 
data = {"python","ai","cloud"}
print(data)

# Set With Mixed Data 
data = {10,20,30,"python","ai",5.5,True}
print(data)

# Accessing Data In Dictionary
data = {10,20,30,40,50}
print(data)

# first element 
# first_element = data[0] # KeyError: 0
# first_element = data[1] # TypeError: 'set' object is not subscriptable
# print(first_element)

# # last element
# last_element = data[5]
# print(last_element)

# Access Individual Elements -> We Cannot 
data = {10,20,30,40,50}
# print(data)
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])
# print(data[5])

# Applying Loops Access Individual Elements -> 10k elements 
data = {10,20,30,40,50}
for num in data: 
    print(num)
    
# Operators We Can Apply -> Requirement: Multiply Each Value with 10 
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
    
# Requirement: Give Courses in Upper Case
data = {"python","ai","cloud"}
for course in data:
    print(course.upper())
    
# Conditionals We Can Apply -> Requirement: Give Only Even Numbers 
data = {10,20,35,45,50}
for num in data:
    if num % 2 == 0:
        print(num)

# Duplicates Not Allowed & Insertion Order Not Preserved
data = {10,20,30,10,40,10,50}
print(data)

# Set Operations 
print(dir(data))

# frozenset
data = frozenset({10,20,30,10,40,10,50})
print(data)

print(type(data))

print(dir(data))

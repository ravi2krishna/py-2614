# Dictionaries

# empty dictionary 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# Dictionary With Numeric Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# Dictionary With Text Data 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)

# Dictionary With Mixed Data 
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","avg":5.5,"passed":True}
print(data)

# Accessing Data In Dictionary
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# first element 
# first_element = data[0] # KeyError: 0
first_element = data[1]  
print(first_element)

# last element
last_element = data[5]
print(last_element)

# unknown_element = data[10] # KeyError: 10
# print(unknown_element)

# Slicing -> Not Supported In Dictionaries
# data = {1:10,2:20,3:30,4:40,5:50}
# print(data)
# print(data[1:3:1]) # 20,30

# Access Individual Elements 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Elements -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,10000:50000}
print(data)
print(data[1])
print(data[2])
# .......
print(data[10000])

# Applying Loops Access Individual Elements -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,10000:50000}
for num in data: # Only Keys We Get 
    print(num)
    
for key in data: # Only Keys We Get 
    print(key)
    
# Access Value Using key # data[key]
for key in data: # Access Value Using key
    print(data[key])
    
# Operators We Can Apply -> Requirement: Multiply Each Value with 10 
data = {1:10,2:20,3:30,4:40,5:50,10000:50000}
for key in data:
    print(key * 10)
    
data = {1:10,2:20,3:30,4:40,5:50,10000:50000}
for key in data:
    print(data[key] * 10)
    
# Requirement: Give Courses in Upper Case
data = {"c1":"python","c2":"ai","c3":"cloud"}
for course in data:
    print(data[course].upper())
    
# Conditionals We Can Apply -> Requirement: Give Only Even Numbers 
data = {1:10,2:20,3:35,4:45,5:50}
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
        
# Duplicates Allowed 
data = (10,20,30,10,40,30,50)
print(data)
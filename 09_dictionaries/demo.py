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
data = {1:10,2:20,1:30,3:10,4:10,5:30,6:50}
print(data)

# Keys Must Be Immutable Objects
data = {'ten':10,'twenty':20}
print(data)

# data = {['ten']:10,['twenty']:20} # TypeError: unhashable type: 'list'
# print(data)

data = {('ten'):10,('twenty'):20} # TypeError: unhashable type: 'list'
print(data)

# Insertion Order Preserved
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# Immutability -> Dictionary is Mutable
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

data[1] = 100

print(data)


# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

students = {"101":{},"102":{}}
print(type(students))

students = {
    "101":{
        "name":"Ravi",
        "email":"ravi2krishna@gmail.com",
        "courses":["python","ai","cloud"],
        "courses_fee":(10000,30000,20000)
        },
    "102":{
        "name":"Mike",
        "email":"mike@yahoo.com",
        "courses":["java","ai","devops"],
        "courses_fee":(10000,30000,25000)
    }
}
print(type(students))

print(students)

print("=" * 50)

# Get 101 Student Details 
student_id = "101"
print(students[student_id])

print("=" * 50)

# Get 102 Student Enrolled Courses  
print(students["102"])
print(students["102"]["courses"])
# First Course Of 102 
print(students["102"]["courses"][0])

# Is 102 Student Google Customer or not ??
if students["102"]["email"].endswith("@gmail.com"):
    print(f"User {students["102"]["name"]} is Google Customer ")
else:
    print(f"User {students["102"]["name"]} is Not Google Customer ")
    
# Dictionary Operations
print(dir(students))
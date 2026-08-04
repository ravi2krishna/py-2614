# Working With JSON Files / Data 

import json 

student = {
    "id": "101",
    "name": "ravi",
    "email": "ravi2krishna@gmail.com",
    "courses":["ai","python","cloud"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Write Data To JSON File
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)

# Write Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
# Read Data From JSON File
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))
    
# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
print("Student Name: ",data['name'])
print("Student Joined Courses: ",data['courses'])
print("Total Joined Courses: ",len(data['courses']))

# Requirement: Check If Student Passed Or Not, based on GPA above 7 from student.json 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)

if data['gpa'] > 7:
    print("Student Passed")
else:
    print("Student Failed")
    
# Object based - dumps() & loads()

student = {
    "id": "101",
    "name": "ravi",
    "email": "ravi2krishna@gmail.com",
    "courses":["ai","python","cloud"],
    "gpa": 9.5
}

print(type(student))
print(student)

# dumps() Serializes a Python object to a JSON-formatted string ("dump string")
json_data = json.dumps(student)
print(json_data)
print(type(json_data))

#loads() Deserializes a JSON-formatted string to a Python object ("load string").
string_data = '{"id": "101", "name": "ravi", "email": "ravi2krishna@gmail.com", "courses": ["ai", "python", "cloud"], "gpa": 9.5}'
print(type(string_data))
python_data = json.loads(string_data)
print(type(python_data))
print(python_data)

# Assume i'm a full stack developer 
# Requirement: We have an API, when requested we are getting JSON Data 
# https://dummyjson.com/
# https://dummyjson.com/users 

# Requirements: Find Number Of Users in the platform 
import requests
response = requests.get('https://dummyjson.com/users') 
status_code = response.status_code
if status_code == 200:
    print("api is working doing further processing")
    # Finding Number Of Users in the platform 
    data_fetched = json.loads(response.text)
    print(data_fetched)
    print(type(data_fetched)) # dict
    
    all_users = data_fetched['users']
    print("Printing All Users")
    print(all_users)
    print("Numbers Of Users In Platform: ",len(all_users))
    
    # Requirements: Fetch All Users Who are Young i.e age below 30
    for user in all_users:
        print(user['id'], user['username'],user['age'])
    
    print("=" * 20)
       
    # Requirements: Fetch All Users Who are Young i.e age below 30
    for user in all_users:
        if user['age'] < 30: # if data['temperature'] < 0: # if data['server_cpu'] > 95:
            print(user['id'], user['username'],user['age']) # print("Dark Blue Image With Snow Falling") # print("Server Under Stress - Reboot / Scale Up")
    
else:
    print("api is not working, stop further processing")
    
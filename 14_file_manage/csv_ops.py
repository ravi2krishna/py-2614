# Working With CSV Data il.e CSV Files 

# Read Data From CSV File
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data)
    print(file_data.read())
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data)
    print(file_data.read().find("Hyderabad"))

print("=" * 50)

# Read Data From CSV File Using csv module 
import csv 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)
        
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        if row[-1] == 'Hyderabad':
            print(row)

print("=" * 50)
            
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from tcs 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[1].endswith('@tcs.com'):
            print(row)

print("=" * 50)
            
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from tcs and from Hyderabad Location
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[1].endswith('@tcs.com') and row[-1] == 'Hyderabad':
            print(row)

print("=" * 50)
            
# NOW DATA SETS ARE CHANGED
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        if row[2] == 'Hyderabad':
            print(row)
# With Above use case we can say reader() is not dynamic 

print("=" * 50)

# Using DictReader For Dynamic Nature i.e CHANGING DATA SETS 
# NOW DATA SETS ARE CHANGED
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['address'] == 'Hyderabad':
            print(row)

print("=" * 50)

# Using DictReader For Dynamic Nature i.e CHANGING DATA SETS 
# NOW DATA SETS ARE CHANGED
# Assume we have 50k student records in CSV file         
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['address'] == 'Hyderabad':
            print(row)

print("=" * 50)

# Write Data To CSV File Using writer 
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'])
    csv_writer.writerows([
        ['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
        ['Ramu', 'ramu661@tcs.com', '9833214959', 'Bangalore'],
        ['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai']
    ])
    
print("=" * 50)

# Write Data To CSV File Using DictWriter 
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/new.csv","w") as file_data:
    # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames) 
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'})
    csv_writer.writerows([
        {'name': 'Vijay', 'email': 'vijay586@gmail.com', 'mobile': '9626631025', 'address': 'Hyderabad'},
        {'name': 'Suresh', 'email': 'suresh602@gmail.com', 'mobile': '9578381099', 'address': 'Hyderabad'},
        {'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
        {'email': 'ravi@gmail.com', 'name': 'Ravi',  'mobile': '9879744557', 'address': 'Hyderabad'}
    ])
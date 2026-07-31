# File Management With Python 

# Syntax - 1

# file = open("file_path","mode")
# file = open("file.txt","r")  

# file_data = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# print(file_data)

file_data = open("14_file_manage/file.txt","r") 
print(file_data)

print(file_data.closed) # False --> Still Open 
file_data.close() # Flush and close the IO object.
print(file_data.closed) # True --> Now Closed

# Syntax - 2 (Recommended)
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed) # True --> Implicitly Closed

# Read Data From File Using Python with r mode 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())

# Create File Using Python with w mode 
with open("14_file_manage/write.txt","w") as file_data:
    print("File Created")
    
# Write Data To File Using Python with w mode 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Hello From Python")
    
# Delete File Using Python with os module
file_path = "14_file_manage/write.txt"
# os.remove(file_path) # NameError: name 'os' is not defined. Did you forget to import 'os'?
import os 
os.remove(file_path)
    
# Folder / Directory Management 
# folder_path = "14_file_manage/students_data"
# os.mkdir(folder_path) # 2nd Time - FileExistsError: [Errno 17] File exists: '14_file_manage/students_data'

folder_path = "14_file_manage/students_data"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    
# Delete Empty Folder - os.rmdir()
os.rmdir(folder_path)

# Delete Non-Empty Folder - shutil.rmtree()
folder_path = "14_file_manage/my_data"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
with open("14_file_manage/my_data/write.txt","w") as file_data:
    file_data.write("Hello From Python")
# os.rmdir(folder_path) # OSError: [Errno 66] Directory not empty: '14_file_manage/my_data'
# shutil.rmtree(folder_path) # NameError: name 'shutil' is not defined. Did you forget to import 'shutil'?
import shutil
shutil.rmtree(folder_path)
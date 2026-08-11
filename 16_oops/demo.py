# OOP 

# Class - Blue Print

class Student: # CLASS 
    
    # Student HAS Something - Characteristics / Properties (Variables)
    student_name = "Ravi" # VARIABLE
    student_email = "ravi2krishna@gmail.com"
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(): # METHOD
        print("Student Is Studying Python")
        
# To Use This Class, We Need Object 
student_object = Student() # OBJECT

print('Student Name: ',student_object.student_name)
print('Student Email: ',student_object.student_email)
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

class Student: # CLASS 
    
    # Student HAS Something - Characteristics / Properties (Variables)
    student_name = "Ravi" # VARIABLE
    student_email = "ravi2krishna@gmail.com"
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(self): # METHOD
        print("Student Is Studying Python")
        
# To Use This Class, We Need Object 
student_object = Student() # OBJECT

print('Student Name: ',student_object.student_name)
print('Student Email: ',student_object.student_email)
student_object.student_studies()

print("=" * 50)

class Student: # CLASS 
    
    # Student HAS Something - Characteristics / Properties (Variables)
    student_name = "Ravi" # VARIABLE
    student_email = "ravi2krishna@gmail.com"
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(self): # METHOD
        print("Student Is Studying Python")
        print('Student Name: ',student_object.student_name)
        print('Student Email: ',student_object.student_email)
        
# To Use This Class, We Need Object 
student_object = Student() # OBJECT

student_object.student_studies()

print("=" * 50)

class Student: # CLASS 
    
    # Student HAS Something - Characteristics / Properties (Variables)
    student_name = "Ravi" # VARIABLE
    student_email = "ravi2krishna@gmail.com"
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(self): # METHOD
        print("Student Is Studying Python")
        print('Student Name: ',self.student_name) # Recommended
        print('Student Email: ',student_object.student_email)
        
# To Use This Class, We Need Object 
student_object = Student() # OBJECT

student_object.student_studies()

print("=" * 50)

# We Have Multiple Objects i.e Multiple Students 
class Student: #  
    
    # Student HAS Something - Characteristics / Properties (Variables)
    student_name = "Ravi" 
    student_email = "ravi2krishna@gmail.com"
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(self): 
        print("Student Is Studying Python")
        print('Student Name: ',self.student_name) # Recommended
        print('Student Email: ',student_object.student_email)
        
# To Use This Class, We Need Object 
student_ravi = Student() 
student_ravi.student_studies()

student_john = Student() 
student_john.student_studies()

student_mike = Student() 
student_mike.student_studies()

print("=" * 50)

# We Have Multiple Objects i.e Multiple Students Using Constructor 
class Student: 
    
    # Student HAS Something - Characteristics / Properties (Variables)
    # student_name = "Ravi" 
    # student_email = "ravi2krishna@gmail.com"
    
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # Student DOES Something - Behaviors / Actions (Methods)
    def student_studies(self): 
        print("Student Is Studying Python")
        print('Student Name: ',self.student_name) # Recommended
        print('Student Email: ',self.student_email)
        
# To Use This Class, We Need Object 
student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Instance Members 
class Student: 
    
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student DOES Something - Behaviors / Actions (Methods)
    # Below is instance method 
    def student_studies(self): 
        print("Student Is Studying Python")
        print('Student Name: ',self.student_name) # Recommended
        print('Student Email: ',self.student_email)
        
# To Use This Class, We Need Object 
student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Class Members 
class Student: 
    
    # Class Variable - Shared By All Objects 
    institute_name = "Digital Institute"
    
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student DOES Something - Behaviors / Actions (Methods)
    # Below is instance method 
    def student_studies(self): 
        print("Student Is Studying Python")
        print("Institute Name: ",Student.institute_name) # Recommended for class variable
        print('Student Name: ',self.student_name) # Recommended for instance variable
        print('Student Email: ',self.student_email)
        
    # Class Method
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print('Student Email: ',self.student_email) # Accessing instance data inside a class method gives error 
    
        
# To Use This Class, We Need Object 
student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Class Method
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Static Members 
class Student: 
    
    # Class Variable - Shared By All Objects 
    institute_name = "Digital Institute"
    
    def __init__(self,student_name,student_email):
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student DOES Something - Behaviors / Actions (Methods)
    # Below is instance method 
    def student_studies(self): 
        print("Student Is Studying Python")
        print("Institute Name: ",Student.institute_name) # Recommended for class variable
        print('Student Name: ',self.student_name) # Recommended for instance variable
        print('Student Email: ',self.student_email)
        
    # Class Method
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print('Student Email: ',self.student_email) # Accessing instance data inside a class method gives error 
    
    # Static Method
    @staticmethod
    def something():
        print("I Do Something That Is Not Associated With Classes / Objects")
    
        
# To Use This Class, We Need Object 
student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

print("=" * 50)

# Class Method
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com") 
student_ravi.student_studies()

student_john = Student("john","john@gmail.com") 
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com") 
student_mike.student_studies()

# Static Method
Student.something()

print("=" * 50)


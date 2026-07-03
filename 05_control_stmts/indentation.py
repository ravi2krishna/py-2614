# Indentation Rules 

# -> When to use Space ? -> When We Write Blocks Of Code 

# -> When Not to use Space ? -> Single Statement 

# -> How many spaces to use ? -> At least one space is must, but Recommended standard is 4 Spaces (tab)

print("Good Morning") # -> When Not to use Space ? -> Single Statement

# Let's Break Above Rule i.e Add Space 
#  print("Good Day") # IndentationError: unexpected indent
#    print("Good Day") # IndentationError: unexpected indent

# Taking class use case for indentation 
# class Student:
# student_name = "Ravi"  # IndentationError: expected an indented block after class definition on line 16

# -> When to use Space ? -> When We Write Blocks Of Code 
# -> How many spaces to use ? -> At least one space is must, but Recommended standard is 4 Spaces (tab)

# At least one space is must
class Student:
 student_name = "Ravi"

# two spaces 
class Student:
  student_name = "Ravi"
  
# twenty spaces 
class Student:
                     student_name = "Ravi"
                     
# Recommended Indentation standard is 4 Spaces (tab)
class Student:
    student_name = "Ravi"
    
# "Consistent Number Of Spaces" - Must 
# class Student:
#     student_name = "Ravi" # 4 spaces
#   student_email = "ravi2krishna@gmail.com" # 2 spaces i.e IndentationError: unindent does not match any outer indentation level


class Student:
  student_name = "Ravi" # 2 spaces
  student_email = "ravi2krishna@gmail.com" # 2 spaces
  
class Student:
    student_name = "Ravi" # 4 spaces
    student_email = "ravi2krishna@gmail.com" # 4 spaces
    
class Trainer:
 trainer_name = "Ravi" # 1 space
 trainer_email = "ravi2krishna@gmail.com" # 1 space
    # student_email = "ravi2krishna@gmail.com" # 4 spaces
 
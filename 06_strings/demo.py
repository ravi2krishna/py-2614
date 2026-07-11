# Strings 

# Single Line Strings

s1 = 'hello' # Recommended
print(s1)
print(type(s1))

s2 = "hello" # Recommended
print(s2)
print(type(s2))

s3 = '''hello''' # Not Recommended
print(s3)
print(type(s3))


s4 = """hello""" # Not Recommended
print(s4)
print(type(s4))

# Multi Line Strings

# SyntaxError: unterminated string literal (detected at line 23)
# define_python = 'Python is a high-level, general-purpose programming language 
#         that emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, an extensive ("batteries-included") 
#         standard library, and garbage collection'
# print(define_python)

define_python = '''Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection'''
        
print(define_python)

define_python = """Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection"""
        
print(define_python)

# Rules 

# When You Use Single quote in a string, enclose them in Double Quotes

question = "how are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 50)
answer = "i'm fine"
print(answer)

# When You Use Double quote in a string, enclose them in Single Quotes
question = "how are you ?"
# answer = "i"m fine" # SyntaxError: unterminated string literal (detected at line 56)
answer = 'i"m fine'
print(answer)

# When You Use Both Single quote and Double quote in a string, 
# enclose them in Triple Single Quotes / Triple Double Quotes

question = "how are you ?"
# answer = 'i'm fine i"m fine' # SyntaxError: unterminated string literal (detected at line 64)
answer = '''i'm fine i"m fine'''
print(answer)
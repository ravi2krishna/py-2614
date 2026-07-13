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

# Accessing Strings 
text = "python"
print(text)

# Access Characters Using Index 
# Positive Indexing
print(text[0])
print(text[1])

# Negative Indexing
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# Access All Characters 
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print("=================")

# Access All Characters 
text = "python is language"

for character in text:
    print(character)
    
# text = 12345 
# for character in text: # TypeError: 'int' object is not iterable
#     print(character)

print("=================")

text = "python"
print(dir(text))

print("=================")

text = 12345
print(dir(text))

print("=================")

text = ["hello","hi",1,2,3]
print(dir(text))
for data in text:
    print(data)

print("=================")

# Slicing
text = "python"
print(text)

print(text[:])
print(text[::])

print(text[0:4:1]) # pyth

        #     0   1 2  3  4  5
        #     p   y t  h  o  n
        #     -6 -5 -4 -3 -2 -1    
        
print(text[0:4]) # pyth
print(text[1:3]) # yt
print(text[0:5:2]) # pto 

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # oht(X) -> empty 
print(text[-4:-6:-1]) # ty

print("=================")

# String Concatenation 
s1 = "good"
s2 = " "
s3 = "morning"
print(s1+s2+s3)

# Formatted String Literals (f-strings)
age = 20
# print("MY Age Is: "+age) # TypeError: can only concatenate str (not "int") to str
print(f"MY Age Is: {age}")

# String Repetition 
laugh = "Haha"
print(laugh)

hard_laugh = laugh * 10
print(hard_laugh)

print("=" * 50)

# String Immutability 
greet = "hello"
print(greet)
greet = "hi" # Reassigning 
print(greet)

# String Immutability 
greet = "hello"
print(greet)
# Requirement is Print Hello 
print(greet[0])
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet)

print("=" * 50)

# Example Of a Mutable Data Type 
greet = ['h','i']
print(greet[0])
greet[0] = 'H'
print(greet[0])

# String Methods 
# capitalize() - Return a copy of the string with its first character capitalized and the rest lowercased.

greet = "hello"
# Requirement is Print Hello 
print(greet.capitalize())
result = greet.capitalize()
print(result)
print(greet) # Original String Didn't Change
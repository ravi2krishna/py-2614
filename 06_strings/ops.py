# String Methods 

# manipulations, transformations, and checks(validations)

# Simulate Gmail Functionality 

#        RAvi2kRiSHna        -> ravi2krishna@gmail.com 
email = input("Enter Email ID: ")
print("Original Email Given: "+email)

# lower(): To convert a string to lowercase in Python, use the built-in lower() method.
transformed_email = email.lower()
print("Transformed Email: "+transformed_email)

# strip(): Removes whitespace from both ends.
# lstrip(): Removes whitespace from the left side only.
# rstrip(): Removes whitespace from the right side only.

# Remove Spaces from both ends i.e strip()
transformed_email = transformed_email.strip() # Manipulation
print("Transformed Email: "+transformed_email)

# Add Domain Name Using Concatenation 
domain = "@gmail.com"
print("Final Transformed Email: "+transformed_email+domain)


# Simulate PAN Card Functionality - Validations 
# https://www.pan.utiitsl.com/

pan = input("Enter PAN ID: ") # amkpl9912w
print("Original PAN: "+pan) # @mkpl9912w - 12kpl9912w

# isalnum() Used to check if a string contains only letters and numbers
valid_pan = pan.isalnum()
print(f"Given PAN {pan} is {valid_pan}")

valid_pan = pan.isalnum() and len(pan) == 10
print(f"Given PAN {pan} is {valid_pan}")

# pan should be alphanumeric and length of 10 
if pan.isalnum() and len(pan) == 10:
    print("Original PAN: "+pan)
    # Transformation: Upper Case 
    # upper(): To convert a string to uppercase in Python, use the upper() method
    print("Transformed PAN: "+pan.upper())
else:
    print(f"Given PAN {pan} is Invalid")
    
# https://swarajya.gumlet.io/swarajya/2019-02/6dff1a72-4302-49c0-87b0-5ef4bf3a9b2b/pancard_500x500.jpg?w=610&q=75&compress=true&format=auto


pan = input("Enter PAN ID: ") # amkpl9912w
print("Original PAN: "+pan) # @mkpl9912w - 12kpl9912w

if len(pan) == 10:
    first_five = pan[0:5:1]
    middle_four = pan[5:9:1]
    last_one = pan[9]
    
    # isalpha(): It returns True if all characters in the string are alphabet letters (a-z, A-Z)
    # isdigit(): It returns True if all characters are digits
    if first_five.isalpha() and middle_four.isdigit() and last_one.isalpha():
        print("Transformed PAN: "+pan.upper())
    else:
        print(f"Given PAN {pan} is Invalid")
else:
    print("Pan Should Be 10 Characters Exactly")
    


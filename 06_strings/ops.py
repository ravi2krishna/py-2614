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
    

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

# startswith() used to check if a string starts with a specific substring
# endswith() used to check if a string ends with a specific substring



# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg


# Name,Email,Age,City,Job_Role
# emp_data = "John,john@apple.com,30,Hyderabad,Developer"

# Requirement: Display Employee Name & Job Role

emp_data = "John,john@apple.com,30,Hyderabad,Developer"
emp_name = emp_data[0]
print('Employee Name: ',emp_name)

emp_name = emp_data[0:4]
print('Employee Name: ',emp_name)

emp_data = "Michael,michael@apple.com,40,Hyderabad,Admin"
emp_name = emp_data[0:7]
print('Employee Name: ',emp_name)

# Above Logic is Hard Coded, which is not good in Dynamic Form 
# split(): method divides a string into a list of substrings based
# on a specified delimiter. By default, it splits the string by any consecutive whitespace

emp_data = "Michael,michael@apple.com,40,Hyderabad,Admin"
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael michael@apple.com 40 Hyderabad Admin"
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael,michael@apple.com,40,Hyderabad,Admin"
data_splitted = emp_data.split(",")
print(data_splitted)
print(type(data_splitted))

# List also works on Index Basis, Same as Strings 

emp_name = data_splitted[0]
emp_role = data_splitted[-1]
print('Employee Name: ',emp_name)
print('Employee Role: ',emp_role)

emp_data = "John,john@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split(",")
emp_name = data_splitted[0]
emp_role = data_splitted[-1]
print('Employee Name: ',emp_name)
print('Employee Role: ',emp_role)

# Simulate Amazon Order Email / SMS / OTP Confirmation Template 

order_template = "Hello, Your Order with order_id has been shipped"
order_ids = "AMAZON-ID-1010029202,AMAZON-ID-8090029202,AMAZON-ID-9090029202,AMAZON-ID-7080029202"
order_ids_splitted = order_ids.split(",")

print(order_ids)
print(order_ids_splitted)

for order_id in order_ids_splitted:
    print(order_id)

order_template = "Hello, Your Order with order_id has been shipped"
order_ids = "AMAZON-ID-1010029202,AMAZON-ID-8090029202,AMAZON-ID-9090029202,AMAZON-ID-7080029202"
    
# replace() method is used to swap out a specific substring for a new one within a string
for order_id in order_ids_splitted:
    # print(order_id)
    send_email = order_template.replace("order_id",order_id)
    print(send_email)
    
# Reset Password 
# old_password -> 
# new_password ->
# reenter_new_password

# if old_password == "Admin123" and new_password == "Login123" and reenter_new_password == "Login123"
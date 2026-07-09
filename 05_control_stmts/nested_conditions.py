# Nested Conditionals 

# inner condition is only checked if the outer condition is True  

if True:
    print("1")
if True:
    print("This is NOT Nested Condition")

# Nested 
if True: # Outer Condition 
    print("1")     
    if True: # Inner Condition 
        print("This is Nested Condition")
        
# Nested 
if False: # Outer Condition 
    print("1")     
    if True: # Inner Condition # Code is not analyzed because condition is statically evaluated as false
        print("This is Nested Condition")

# Nested Condition Use Case 
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID Proof")    
else:
      print("You Cannot Vote - Under Age")           

# Real World Use Case 
# Net Banking Login -> Enter Username & Password (authentication) -> Enter OTP (authorization)

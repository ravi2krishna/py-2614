# Simulate Authentication Functionality 
# Net Banking Logins / ATM Withdraws / Login Systems etc 

correct_pin = 2345 

attempts = 3

# print(type(correct_pin))

# len() function - Return the number of items in a container.

# print(len(correct_pin)) # TypeError: object of type 'int' has no len()

# correct_pin_str = str(correct_pin)
# print(len(correct_pin_str))

while attempts > 0:
    print(f"You Have {attempts} Attempts Left")
    
    user_pin = int(input("Enter PIN: ")) 
    
    # Scenario for not 4 Digit PIN
    if len(str(user_pin)) != 4:
        print("Transaction Failed") 
        attempts -= 1 
        continue 
    
    # Scenario for 4 Digit PIN -> Correct PIN
    if user_pin == correct_pin:
        print("Transaction Success") 
        break 
    
    # Scenario for 4 Digit PIN -> InCorrect PIN 
    else:
        print("Transaction Failed") 
        attempts -= 1 

else:
    print("Maximum Attempts Reached, Try After 24 Hours!!!")
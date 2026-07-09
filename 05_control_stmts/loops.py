# Looping Structures (Iteration Statements) (Repetition)

# while loop 

# while True:
#     print("Repeat....")
#     print("Repeat........")
#     print("Repeat..............")

# To terminate loop use control + c

while False:
    print("Repeat....")
    print("Repeat........")
    print("Repeat..............")
    
# Counter 
count = 1
while count <= 5:
    print("Count is: ",count)
    count += 1

print("===================")
    
# use while loop, When we don't know number of Iterations/Repetitions in advance 

# You Found a Lost Phone, Trying To Break Password 
# Tell me at which attempt, the phone will be Unlocked ?

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter Phone PIN: ")
print("Phone Unlocked")
    
print("===================")

# For Loop 
prices_products = [1000,1500,2000,2500,3200,3500,4000,4500,5000,100000]

# Some Offer is running -> Provide discount of 250 on each product 
# In lists we have index, which starts from zero and keeps increasing 

print(prices_products[0])
print(prices_products[1])
print(prices_products[2])
print(prices_products[3])
print(prices_products[4])

print("===================")

# Applying Discount 

print(prices_products[0] - 250)
print(prices_products[1] - 250)
print(prices_products[2] - 250)
print(prices_products[3] - 250)
print(prices_products[4] - 250)

print("===================")

# Now Applying Discount for 10000 products is lot of repetition 
# print(prices_products[9999] - 250)

prices_products = [1000,1500,2000,2500,3200,3500,4000,4500,5000,100000]
print("Prices Before Discount")
for price in prices_products:
    print(price)

print("===================")
    
print("Prices After Discount")
for price in prices_products:
    print(price - 250)
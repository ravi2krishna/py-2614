# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e __ prefix is there, which means private 

obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

# Real World Use Case Scenario
class CreditCardPayment:
    def __init__(self,card_number,card_cvv):
        # self.card_number = card_number # This is not encapsulated  
        self.__card_number = card_number # Recommended i.e Private 
        self.__card_cvv = card_cvv # Recommended i.e Private 
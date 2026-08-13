
# Private Access 

# class A:
#     def __init__(self,a):
#         self.__a = a # Private i.e __ prefix is there, which means private 

# class B(A):
#     def showA(self):
#         a = A(10)
#         print(a.__a) # AttributeError: 'A' object has no attribute 
        
# obj = B(100)
# obj.showA()

# Protected Access
class A:
    def __init__(self,a):
        self._a = a # Protected i.e _ prefix is there, which means protected and subclasses can use it 

class B(A):
    def showA(self):
        a = A(10)
        print(a._a) # Now Accessible inside sub class 
        
obj = B(100)
obj.showA()

# obj = A(20)
# print(obj.a) # AttributeError: 'A' object has no attribute 'a' i.e Outside the class and sub-class no access 
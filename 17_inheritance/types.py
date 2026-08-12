# Types Of Inheritance

# Without Inheritance 

class Father:
    def house(self):
        print("Has House")
        
class Son:
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
# son_object.house() # AttributeError: 'Son' object has no attribute 'house'

print("=" * 50)

# With Inheritance 

class Father:
    def house(self):
        print("Has House")
        
class Son(Father): # Single Level Inheritance: -> Parent -> Child 
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house() 

print("=" * 50)

# Multi Level Inheritance: GrandParent -> Parent -> Child 
class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Son(Father): # Multi Level Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house() 
son_object.land() 

print("=" * 50)

# Multiple Inheritance : Father | Mother
#                             Child
class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother:
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # Multiple Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house() 
son_object.land() 
son_object.gold()

print("=" * 50)

# Hierarchical Inheritance: One Parent -> Multiple Child 

#               Parent
#           Son   |   Daughter

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother:
    def gold(self):
        print("Has Gold")
        
class Son(Father): # Hierarchical Inheritance
    def car(self):
        print("Has Car")
        
class Daughter(Father): # Hierarchical Inheritance
    def business(self):
        print("Has Business")
        
son_object = Son()
son_object.car()
son_object.house() 
son_object.land() 

daughter_object = Daughter()
daughter_object.house() 
daughter_object.land() 
daughter_object.business()

print("=" * 50)

# Hybrid Inheritance: Combination Of Types Of Inheritance
class A:
    def a(self):
        print("Has A")
        
class B(A):
    def b(sef):
        print("Has B")
        
class C(A):
    def c(sef):
        print("Has C")
        
class D(B,C):
    def d(sef):
        print("Has D")
        
object_d = D()
object_d.d()
object_d.c()
object_d.b()
object_d.a()
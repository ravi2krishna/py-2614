# provides a new implementation 
# of a method that already exists in parent class 

class Animal:
    def sound(self):
        print("Animal Making Sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog Making Sound - Woof")
        
class Cat(Animal):
    def sound(self):
        print("Cat Making Sound - Meow")
        
animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()
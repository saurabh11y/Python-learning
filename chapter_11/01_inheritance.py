# parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# create object of child class
d = Dog()
d.speak()   # from parent class
d.bark()    # from child class

# Polymorphism : Polymorphism means "many forms" and allows the same method, 
# function or operator to behave differently depending on the object or data 
# it works with. This flexibility helps create more reusable, maintainable and scalable code.













# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
class Animal:
   def sound(self):
       return "Some generic sound"
class Dog(Animal):
   def sound(self):
       return "Bark"
class Cat(Animal):
   def sound(self):
       return "Meow"
# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
   print(animal.sound())
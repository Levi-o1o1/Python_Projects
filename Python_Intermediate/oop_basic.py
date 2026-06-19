class student():
    name = "yash"

s1 = student()
print(s1.name)

class Car():
    color = "yellow"
    model = "AMG-02"

m1 = Car()
print(m1.model)
print(m1.color)

# classes and constractor 

class Bike:
    def __init__(self, model,color):
        self.model = model
        self.color = color
        print("Things are doing well :")


b1 = Bike("bajaj 150cc", "Green-Black")
b2 = Bike("activa 100cc", "Grey")

print(b1.model)
print(b1.color)
print(b2.model)
print(b2.color)

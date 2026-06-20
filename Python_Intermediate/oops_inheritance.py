# inheritance : when one class(child/derived) derives the properties & methods of another class(parent/base)
#  its have 3 types single , multi-level , multiple inheritance 
# this is e.g: of single inheritance ,

class Car:    # parent class
    @staticmethod  # its use to a fuction belongs to a class but does not need to access to the object(self) to use staticmethod
    def start():  
        print("car is started...")


    @staticmethod # it doesn't use instance variables (self.name, self.age, etc...) it doesn't use class var either.
    def stop():  
        print("car stopped.")


class nishan(Car):
    def __init__(self, name):
        self.name = name


car1 = nishan("gtr")
car2 = nishan("skyline")

print(car1.start())

# super method 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..

class Car:    
    def __init__(self, type):
        self.type = type

    @staticmethod  
    def start():  
        print("car is started...")


    def stop():  
        print("car stopped.")


class nishan(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = nishan("gtr", "electric")
print(car1.type)
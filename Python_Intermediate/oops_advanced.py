#  del keyword : used to delete object properties or object itself.

# class stu:
#     def __init__(self, name):
#         self.name = name


# s1 = stu("raj")
# print(s1.name)
# del s1.name
# print(s1.name)

# private attributes & methods
#private fuction made for __ after attribute and methods only use for class when we private that not accesible outside the class

class person:
    __name = "unknow"

    def __hello(self):
        print("Hidden")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())
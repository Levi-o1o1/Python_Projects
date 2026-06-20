#  del keyword : used to delete object properties or object itself.

class stu:
    def __init__(self, name):
        self.name = name


s1 = stu("raj")
print(s1.name)
del s1.name
print(s1.name)

# private attrivutes & methods

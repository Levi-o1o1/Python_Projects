# classmethod decorator @classmethod is bound to the class & receives the class as an implict
# in we have 3 type of method first static , class , instance(self) called methods 


class person:
    name = "unkown"

    # def changeName(self, name):
    #     self.name = name
    @classmethod
    def changeName(cls, name):
        cls.name = name 

p1 = person()
p1.changeName("rajkumar")
print(p1.name)
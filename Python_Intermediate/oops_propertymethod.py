# propertymethod: 

class stu:
    def __init__(self, phy, chem, math, eng):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.eng = eng

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math + self.eng) / 3) + "%"


stu1 = stu(98,44,33,22)
print(stu1.percentage)

stu1.phy = 44
print(stu.percentage)
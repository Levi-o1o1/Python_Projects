class stu:
     def __init__(self, name, mark):
          self.name = name 
          self.mark = mark

     @staticmethod
     def hello():
         print("hello")

     def get_avg(self):
       sum = 0 
       for val in self.mark: # store mark value in val varble
          sum += val       # sum of both
          print("hi", self.name , "your avg score is :", sum/3)


s1 = stu("raj", [99,33,10])
s1.get_avg()
s1.hello()
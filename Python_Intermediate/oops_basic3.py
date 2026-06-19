# abstraction : is hinding some details in class like user don't care about things things so hide it called abstraction
#abstraction hide unnessary things only show essential features to the user
# example :

class car():
   def __init__(self):
      self.acc = False
      self.brk = False
      self.clutch = False
   def start(self):
      self.clutch = True
      self.acc = True
      print("car is started ........")

car1 = car()
car1.start()

# Encapsulation : is waraping data and fucnction into a single unit (object)

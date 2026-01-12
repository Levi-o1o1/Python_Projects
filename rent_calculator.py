# This is a basic level of rent calu , if you want to check your total rent calulation , so you can use this method.
# you need to give these details first: total rent, total electricity units spend, charge per unit of elec,
# or aditional charges if you want to calu or how many persons are leving you if you want to divide 
# How to run : in terminal type this >>>>   python3 rent_calculator.py

try:
  rent = int(input("Enter your total rent amount: "))
  additional_charges = int(input("Enter additional charges (if not, enter 0):"))
  electricity_spend = int(input("Enter total electricity units you spend :"))
  charage_per_unit = int(input("Enter charge per unit of electricity:"))
  persons = int(input("Enter how many 'bande' are living in your room/flat : "))
    
  total_amount = electricity_spend * charage_per_unit
  if persons > 0:
        output = ( additional_charges+rent+total_amount) // persons
        total = (additional_charges+rent+total_amount )
        print("Each person will pay = ", output)
        print("And your total amount is = ", total)

  else:
          output = ( additional_charges+rent+total_amount) 
          print("Your total bill is =", output)


except ValueError:
    print("You are enter worng value please check again ! 😠")
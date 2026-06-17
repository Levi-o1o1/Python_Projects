# Membership operators 

students = {"roy", "kumar", "raj", "yash"}

student = input("Enter the name of a student you want to find :")

if student  in students:
    print(f"{student} it is you want ")
else:
    print(f"{student} was not found ")
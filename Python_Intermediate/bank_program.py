def show_bal():
    pass

def deposit():
    pass

def withdraw():
    pass

balance = 0
is_run = True

while is_run:
    print("Banking Program ")
    print("1. show balacne")
    print("2. Deposit ")
    print("3. Withdraw")
    print("4. Exit ")

    choice = input("Enter your choice (1-4):")

    if choice == "1":
        show_bal()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_run = False
    else:
        print("That is not a valid choice : please choice again !")

print(" Thank you vist again !")     

def show_bal(balance):
    print("**********************************")
    print(f"Your balance is {balance:.2f}")
    print("**********************************")
def deposit():
    print("**********************************")
    amount = float(input("Enter an amount to be depostited:"))
    print("**********************************")
    if amount < 0:
        print("**********************************")
        print("that's not a valid amount")
        print("**********************************")
        return 0
    else:
        return amount
     

def withdraw(balance):
    print("**********************************")
    amount = float(input("Enter amount to be withdrwal:"))
    print("**********************************")

    if amount > balance:
        print("**********************************")
        print("Insufficient funds")
        print("**********************************")
        return 0 
    elif amount < 0:
        print("**********************************")
        print("Amount must be greater than 0 ")
        print("**********************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_run = True

    while is_run:
        print("**********************************")
        print("        Banking Program           ")
        print("**********************************")
        print("1. show balacne")
        print("2. Deposit ")
        print("3. Withdraw")
        print("4. Exit ")
        print("**********************************")

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            show_bal(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
           balance -= withdraw(balance)
        elif choice == "4":
            is_run = False
        else:
            print("**********************************")
            print("That is not a valid choice : please choice again !")
            print("**********************************")

    print("**********************************")
    print(" Thank you vist again !")    
    print("**********************************")

if __name__ == '__main__':
    main()
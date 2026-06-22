def show_bal(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be depostited:"))
    if amount < 0:
        print("that's not a valid amount")
        return 0
    else:
        return amount
     

def withdraw(balance):
    amount = float(input("Enter amount to be withdrwal:"))

    if amount > balance:
        print("Insufficient funds")
        return 0 
    elif amount < 0:
        print("Amount must be greater than 0 ")
        return 0
    else:
        return amount

def main():
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
            show_bal(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
           balance -= withdraw(balance)
        elif choice == "4":
            is_run = False
        else:
            print("That is not a valid choice : please choice again !")

    print(" Thank you vist again !")    

if __name__ == '__main__':
    main()
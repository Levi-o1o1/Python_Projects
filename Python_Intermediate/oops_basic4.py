class Account:
    def __init__(self, bal, acc):
        self.bank_bal = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.bank_bal -= amount
        print("Rs", amount, "was debited .")
        print("total amount is :", self.get_bal())

    def credit(self, amount):
        self.bank_bal += amount
        print("Rs", amount, "was credited ")
        print("total amount is :", self.get_bal())

    def get_bal(self):
        return self.bank_bal

acc1 = Account(10000, 123433)
acc1.debit(1000)
acc1.credit(900)

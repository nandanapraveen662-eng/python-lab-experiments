class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Current Balance:", self.balance)


a = BankAccount(101, "Anu", "Savings", 5000)

a.deposit(2000)
a.withdraw(1000)
a.display()
class Account:
    def __init__(self, balance, deposit, withdraw): 
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw

    def dp(self): # deposit money
        self.deposit = float(input("How much would you like to deposit? "))
        self.balance += self.deposit
        print("P%s" % (self.deposit) + " has been added to your account.")

    def wd(self): 
        self.withdraw = float(input("How much would you like to withdraw? "))
        self.balance -= self.withdraw
        print("P%s" % (self.withdraw) +
              " has been subtracted from your account.")

    def bal(self):
        print("Your current balance is P" + "%s" % (self.balance))

    def Menu(self):
        print("Welcome to Bank of Batangas!")
        print("[1] Deposit")
        print("[2] Withdrawal")
        print("[3] Balance")
        print("[4] Exit")


acc = Account(2000, 0, 0)

while True:

    print("Welcome to Bank of Batangas!")
    print("[1] Deposit")
    print("[2] Withdrawal")
    print("[3] Balance")
    print("[4] Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        acc.dp() # deposit money
    elif n == 2:
        acc.wd()  # withdraw money
    elif n == 3:
        acc.bal() # check balance
    elif n == 4:
        break # exit

class BankAccount:

    def __init__(self, name):
        self.name = name
        self.bal = 0
        print(f"Account {self.name} created! Initial balance = Rs. 0")
    
    def deposit(self, amt):
        self.bal += amt
        print(f"Rs. {amt} deposited to account {self.name}. Available balance = Rs. {self.bal}")

    def withdraw(self, amt):
        if self.bal <= amt:
            print(f"Transaction failure! Account {self.name} does not have enough balance amount.")
        else:
            self.bal -= amt
            print(f"Withdraw successful! Available balance = Rs. {self.bal}")

    def check_balance(self):
        print(f"Available Balance on account {self.name} is Rs. {self.bal}")
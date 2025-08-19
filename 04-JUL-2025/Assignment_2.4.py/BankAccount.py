class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance + self.overdraft_limit:
            print("Exceeded overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


# Create a savings account
savings = SavingsAccount("Atharv", 1000, interest_rate=0.05)
savings.display_balance()
savings.apply_interest()

# Create a checking account with $200 balance and $100 overdraft limit
checking = CheckingAccount("Rahul", 200, overdraft_limit=100)
checking.display_balance()
checking.withdraw(250)  # Allowed due to overdraft
checking.withdraw(100)  # Exceeds overdraft


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
# Create an account for Sham with an initial balance of $100
account = BankAccount("Sham", 100)

account.display_balance()

# Deposit and withdraw money
account.deposit(50)
account.withdraw(30)
account.withdraw(150)  # Should display insufficient funds
account.display_balance()

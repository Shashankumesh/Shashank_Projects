
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount:.2f} | Balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount:.2f} | Balance: {self.balance:.2f}")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    def show_passbook(self):
        print(f"\nPassbook for {self.account_holder}:")
        for entry in self.transactions:
            print(entry)
        print(f"Current Balance: {self.balance:.2f}\n")

# Example usage
if __name__ == "__main__":
    account = BankAccount("John Doe")
    account.deposit(1000)
    account.withdraw(250)
    account.deposit(500)
    account.show_passbook()
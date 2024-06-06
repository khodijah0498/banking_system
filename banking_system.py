class Account:
    def __init__(self, account_number, account_holder, account_type, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} to {recipient_account.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def view_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")


class BankingSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder, account_type):
        new_account = Account(account_number, account_holder, account_type)
        self.accounts.append(new_account)
        print(f"Account created: {account_number}")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found")
        return None


banking_system = BankingSystem()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Account Details")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder's name: ")
        account_type = input("Enter account type (Savings/Current): ")
        banking_system.create_account(account_number, account_holder, account_type)

    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        account = banking_system.get_account(account_number)
        if account:
            account.deposit(amount)

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        account = banking_system.get_account(account_number)
        if account:
            account.withdraw(amount)

    elif choice == "4":
        sender_account_number = input("Enter sender's account number: ")
        recipient_account_number = input("Enter recipient's account number: ")
        amount = float(input("Enter amount to transfer: "))
        sender_account = banking_system.get_account(sender_account_number)
        recipient_account = banking_system.get_account(recipient_account_number)
        if sender_account and recipient_account:
            sender_account.transfer(amount, recipient_account)

    elif choice == "5":
        account_number = input("Enter account number: ")
        account = banking_system.get_account(account_number)
        if account:
            account.view_details()

    elif choice == "6":
        break

    else:
        print("Invalid option. Please try again.")

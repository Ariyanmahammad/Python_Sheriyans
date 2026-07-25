import json
import os
from datetime import datetime


DATA_FILE = "accounts.json"


class BankAccount:
    """Represents a single bank account."""

    def __init__(self, acc_no, name, balance=0.0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self.balance += amount
        self.history.append(
            f"{datetime.now()} : Deposited ₹{amount:.2f}"
        )

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self.history.append(
            f"{datetime.now()} : Withdrawn ₹{amount:.2f}"
        )

    def transfer(self, receiver, amount):
        if receiver.acc_no == self.acc_no:
            raise ValueError("Cannot transfer to same account.")

        self.withdraw(amount)
        receiver.deposit(amount)

        self.history.append(
            f"{datetime.now()} : Sent ₹{amount:.2f} to {receiver.name}"
        )

        receiver.history.append(
            f"{datetime.now()} : Received ₹{amount:.2f} from {self.name}"
        )

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance,
            "history": self.history
        }

    @staticmethod
    def from_dict(data):
        account = BankAccount(
            data["acc_no"],
            data["name"],
            data["balance"]
        )
        account.history = data.get("history", [])
        return account


class Bank:

    def __init__(self):
        self.accounts = {}
        self.load()

    def load(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        for item in data:
            account = BankAccount.from_dict(item)
            self.accounts[account.acc_no] = account

    def save(self):
        with open(DATA_FILE, "w") as file:
            json.dump(
                [acc.to_dict() for acc in self.accounts.values()],
                file,
                indent=4
            )

    def create_account(self):
        print("\n----- Create Account -----")

        acc_no = input("Account Number : ")

        if acc_no in self.accounts:
            print("Account already exists.")
            return

        name = input("Account Holder Name : ")

        try:
            balance = float(input("Opening Balance : "))
        except ValueError:
            print("Invalid amount.")
            return

        account = BankAccount(acc_no, name, balance)

        account.history.append(
            f"{datetime.now()} : Account Created"
        )

        self.accounts[acc_no] = account

        print("Account created successfully.")

    def search_account(self):
        acc_no = input("Enter Account Number : ")

        account = self.accounts.get(acc_no)

        if account:
            print("\n------ Account Details ------")
            print("Account :", account.acc_no)
            print("Name    :", account.name)
            print(f"Balance : ₹{account.balance:.2f}")
        else:
            print("Account not found.")

    def show_all_accounts(self):

        if not self.accounts:
            print("No accounts available.")
            return

        print("\n----------- Accounts -----------")

        for acc in self.accounts.values():
            print(
                f"{acc.acc_no:<10}"
                f"{acc.name:<20}"
                f"₹{acc.balance:.2f}"
            )

    def deposit_money(self):

        acc_no = input("Account Number : ")

        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found.")
            return

        try:
            amount = float(input("Deposit Amount : "))
            account.deposit(amount)
            print("Deposit successful.")
        except Exception as e:
            print(e)

    def withdraw_money(self):

        acc_no = input("Account Number : ")

        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found.")
            return

        try:
            amount = float(input("Withdraw Amount : "))
            account.withdraw(amount)
            print("Withdrawal successful.")
        except Exception as e:
            print(e)
    def transfer_money(self):
        """Transfer money between two accounts."""

        sender_no = input("Sender Account Number : ")
        receiver_no = input("Receiver Account Number : ")

        sender = self.accounts.get(sender_no)
        receiver = self.accounts.get(receiver_no)

        if not sender:
            print("Sender account not found.")
            return

        if not receiver:
            print("Receiver account not found.")
            return

        try:
            amount = float(input("Amount : "))
            sender.transfer(receiver, amount)
            print("Transfer successful.")
        except Exception as e:
            print(e)

    def check_balance(self):
        """Display account balance."""

        acc_no = input("Account Number : ")

        account = self.accounts.get(acc_no)

        if account:
            print(f"\nCurrent Balance : ₹{account.balance:.2f}")
        else:
            print("Account not found.")

    def transaction_history(self):
        """Display transaction history."""

        acc_no = input("Account Number : ")

        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found.")
            return

        print("\n------ Transaction History ------")

        if not account.history:
            print("No transactions available.")
            return

        for transaction in account.history:
            print(transaction)

    def delete_account(self):
        """Delete an account."""

        acc_no = input("Account Number : ")

        if acc_no not in self.accounts:
            print("Account not found.")
            return

        confirm = input("Delete this account? (y/n): ").lower()

        if confirm == "y":
            del self.accounts[acc_no]
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")

    def sort_by_balance(self):
        """Display accounts sorted by balance."""

        if not self.accounts:
            print("No accounts available.")
            return

        accounts = sorted(
            self.accounts.values(),
            key=lambda account: account.balance,
            reverse=True
        )

        print("\n------ Accounts Sorted By Balance ------")

        for account in accounts:
            print(
                f"{account.acc_no:<10}"
                f"{account.name:<20}"
                f"₹{account.balance:.2f}"
            )

    def bank_statistics(self):
        """Display bank statistics."""

        if not self.accounts:
            print("No accounts available.")
            return

        balances = [
            account.balance
            for account in self.accounts.values()
        ]

        total = sum(balances)
        average = total / len(balances)
        highest = max(balances)
        lowest = min(balances)

        richest = max(
            self.accounts.values(),
            key=lambda account: account.balance
        )

        poorest = min(
            self.accounts.values(),
            key=lambda account: account.balance
        )

        print("\n========== Bank Statistics ==========")
        print(f"Total Accounts : {len(self.accounts)}")
        print(f"Total Balance  : ₹{total:.2f}")
        print(f"Average Balance: ₹{average:.2f}")
        print(f"Highest Balance: ₹{highest:.2f}")
        print(f"Lowest Balance : ₹{lowest:.2f}")
        print(f"Richest Person : {richest.name}")
        print(f"Poorest Person : {poorest.name}")

    def menu(self):
        """Display the menu."""

        while True:

            print("\n")
            print("=" * 45)
            print("        BANK MANAGEMENT SYSTEM")
            print("=" * 45)
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Check Balance")
            print("6. Search Account")
            print("7. Show All Accounts")
            print("8. Transaction History")
            print("9. Sort Accounts By Balance")
            print("10. Bank Statistics")
            print("11. Delete Account")
            print("12. Save Data")
            print("13. Exit")
            print("=" * 45)

            choice = input("Enter choice : ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.deposit_money()

            elif choice == "3":
                self.withdraw_money()

            elif choice == "4":
                self.transfer_money()

            elif choice == "5":
                self.check_balance()

            elif choice == "6":
                self.search_account()

            elif choice == "7":
                self.show_all_accounts()

            elif choice == "8":
                self.transaction_history()

            elif choice == "9":
                self.sort_by_balance()

            elif choice == "10":
                self.bank_statistics()

            elif choice == "11":
                self.delete_account()

            elif choice == "12":
                self.save()
                print("Data saved successfully.")

            elif choice == "13":
                self.save()
                print("Thank you for using Bank Management System.")
                break

            else:
                print("Invalid choice. Try again.")

import random


def generate_demo_data(bank):
    """
    Creates some demo accounts if no account exists.
    This helps first-time users test the program quickly.
    """

    if bank.accounts:
        return

    names = [
        "Ariyan",
        "Rahul",
        "Sneha",
        "Ankit",
        "Priya"
    ]

    for i, name in enumerate(names, start=1):
        acc_no = f"100{i}"
        balance = random.randint(1000, 10000)

        account = BankAccount(acc_no, name, balance)
        account.history.append(
            f"{datetime.now()} : Demo Account Created"
        )

        bank.accounts[acc_no] = account


def welcome():
    """Display welcome banner."""

    print("=" * 55)
    print("         WELCOME TO BANK MANAGEMENT SYSTEM")
    print("=" * 55)
    print("Features Included:")
    print("✔ Create Account")
    print("✔ Deposit Money")
    print("✔ Withdraw Money")
    print("✔ Transfer Money")
    print("✔ Search Account")
    print("✔ Transaction History")
    print("✔ Statistics")
    print("✔ Sorting")
    print("✔ JSON File Storage")
    print("✔ Exception Handling")
    print("=" * 55)


def main():
    """Program entry point."""

    welcome()

    bank = Bank()

    # Creates sample accounts only when accounts.json is empty
    generate_demo_data(bank)

    try:
        bank.menu()

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")

    finally:
        bank.save()
        print("\nData saved successfully.")
        print("Goodbye!")


if __name__ == "__main__":
    main()
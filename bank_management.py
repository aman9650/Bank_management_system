import tkinter
import tkinter as tk

from tkinter import simpledialog, messagebox

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, name, balance):
        if account_number in self.customers:
            return "Account already exists."
        else:
            self.customers[account_number] = {'name': name, 'balance': balance}
            return "Account created successfully."

    def deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number]['balance'] += amount
            return f"Deposited ${amount}. New balance: ${self.customers[account_number]['balance']}"
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number]['balance'] >= amount:
                self.customers[account_number]['balance'] -= amount
                return f"Withdrew ${amount}. New balance: ${self.customers[account_number]['balance']}"
            else:
                return "Insufficient balance."
        else:
            return "Account not found."

    def check_balance(self, account_number):
        if account_number in self.customers:
            return f"Account balance for {self.customers[account_number]['name']}: ${self.customers[account_number]['balance']}"
        else:
            return "Account not found."

class BankManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.bank = Bank()

        self.label = tk.Label(root, text="Bank Management System")
        self.label.pack()

        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def create_account(self):
        account_number = self.prompt("Enter account number:")
        name = self.prompt("Enter customer name:")
        balance = float(self.prompt("Enter initial balance:"))
        result = self.bank.create_account(account_number, name, balance)
        self.show_message(result)

    def deposit(self):
        account_number = self.prompt("Enter account number:")
        amount = float(self.prompt("Enter the amount to deposit:"))
        result = self.bank.deposit(account_number, amount)
        self.show_message(result)

    def withdraw(self):
        account_number = self.prompt("Enter account number:")
        amount = float(self.prompt("Enter the amount to withdraw:"))
        result = self.bank.withdraw(account_number, amount)
        self.show_message(result)

    def check_balance(self):
        account_number = self.prompt("Enter account number:")
        result = self.bank.check_balance(account_number)
        self.show_message(result)

    def prompt(self, message):
        return simpledialog.askstring("Input", message)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankManagementApp(root)
    root.geometry("800x600")
    root.mainloop()

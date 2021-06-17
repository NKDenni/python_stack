# Objectives:
    # Practice writing classes with associations
    # Make sure that by the end of this assignment that you:
        # have both the User and BankAccount classes in the same file for your assignment
        # only create BankAccount instances inside of the User's __init__ method
        # only call BankAccount methods inside of the methods in the User class

    # Update the User class __init__ method
    # Update the User class make_deposit method
    # Update the User class make_withdrawal method
    # Update the User class display_user_balance method
    # SENSEI BONUS: Allow a user to have multiple accounts, update methods so the user has to specify which account they are withdrawing or depositing to

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = SavingAccount()
        self.checking = CheckingAccount()

    def deposit(self, amount, atype=""):
        if atype == "Savings":
            self.savings.deposit(amount)
            print(f"${amount} has been deposited to {atype}.")
        elif atype == "Checking":
            self.checking.deposit(amount)
            print(f"${amount} has been deposited to {atype}.")
        else:
            print("Specify account type.")
        return self

    def withdraw(self, amount, atype=""):
        if atype == "Savings":
            self.savings.withdraw(amount)
            print(f"${amount} has been deposited to {atype}.")
        elif atype == "Checking":
            self.checking.withdraw(amount)
            print(f"${amount} has been deposited to {atype}.")
        else:
            print("Specify account type.")
        return self

    def interest(self, amount, atype="", user =""):
        if atype == "Savings":
            self.savings.yield_interest(amount, atype, user)
        elif atype == "Checking":
            self.checking.yield_interest(amount, atype, user)
        else:
            print("Specify account type.")
        return self

    # def transfer(self, amount, target, user=""):
    #     self.user = user
    #     if self.balance >= amount:
    #         self.balance -= amount
    #         if target == "Savings" and user == "":
    #             self.savings.deposit(amount)
    #         elif target == "Checking" and user == "":
    #             self.checking.deposite(amount)
    #             print("\n" f"${amount} has been transfered to {target}.")
    #         elif atype == "Checking" and user == user:
    #             user.checking.deposite(amount)
    #             print(
    #                 "\n" f"${amount} has been transfered to {user}'s {target}.")
    #         else:
    #             atype == "Savings" and user == user
    #             user.savings.deposit(amount)
    #             print(
    #                 "\n" f"${amount} has been transfered to {user}'s {target}.")
    #     else:
    #         print(f"Insufficient funds in {self.balance}")
    #     return self
    # # def transfer_money(self, atype, amount, target):
    # #     if atype == "Savings":
    # #         self.savings.transfer(amount, target)
    # #     elif atype == "Checking":
    # #         self.checking.transfer(amount, target)
    # #     else:
    # #         print("Specify account type.")
    # #     return self

    def display_user_balance(self, atype=" "):
        if atype == "Savings":
            self.savings.display_account_info()
            print(f"Current balance is ${self.savings.balance} in {atype}.")
        elif atype == "Checking":
            self.checking.display_account_info()
            print(f"Current balance is ${self.checking.balance} in {atype}.")
        else:
            print("Specify account type.")
        return self


class BankAccount:
    def __init__(self, atype, int_rate):
        self.atype = atype
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return self

    def yield_interest(self):
        amount = int(self.balance * self.int_rate)
        print(f"New balance in {self.atype} after interest is ${amount}.")
        self.balance = amount
        return self

class CheckingAccount(BankAccount):
    def __init__(self):
        self.int_rate = 1.02
        self.balance = 0
        self.atype = "Checking"

class SavingAccount(BankAccount):
    def __init__(self):
        self.int_rate = 1.04
        self.balance = 0
        self.atype = "Savings"


Eric = User('Eric Johnson', 'EJ@gmail.com')
Alan = User('Alan Becker', 'AB@gmail.com')

print("\n", "-"*20, "New Transaction", "-"*20)
print("\r")
Eric.deposit(5000, "Savings").withdraw(200, "Savings").withdraw(100, "Savings").withdraw(300, "Savings").interest("Savings").display_user_balance("Savings")
print("\n", "-"*20, "End Transaction", "-"*20)
print("\r")

print("\n", "-"*20, "New Transaction", "-"*20)
print("\r")
Eric.deposit(1000, "Checking").withdraw(200, "Checking").withdraw(100, "Checking").interest("Checking").display_user_balance("Checking")
print("\n", "-"*20, "End Transaction", "-"*20)
print("\r")

print("\n", "-"*20, "New Transaction", "-"*20)
print("\r")
Eric.display_user_balance("Savings")
print("\n", "-"*20, "End Transaction", "-"*20)
print("\r")

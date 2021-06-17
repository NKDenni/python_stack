# Objectives:
    # Practice writing classes

# Functionallity
    # deposit(self, amount) - increases the account balance by the given amount 
    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    # display_account_info(self) - print to the console: eg. "Balance: $100"
    # yield_interest(self) - increases the account balance by the current balance * the interest rate(as long as the balance is positive)

class BankAccount:
    def __init__(self, anumber):
        self.anumber = anumber
        self.int_rate = 1.1
        self.balance = 0

	# your code here! (remember, this is where we specify the attributes for our class)
	# don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance += amount
        print("\n" f"{self.anumber}s new balance after ${amount} deposite is ${self.balance}.")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print("\n" f"{self.anumber}'s new balance after ${amount} withdrawn is ${self.balance}.")
        return self

    def display_account_info(self):
        print("\n" f"Current balance is ${self.balance}.")
        return self

    def yield_interest(self):
        amount = int(self.balance * self.int_rate)
        print("\n" f"{self.anumber}s new balance after interest is ${amount}.")
        self.balance = amount
        return self


a001 = BankAccount("a001")
a001.deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()

print("\n", "-"*20, "New Transaction", "-"*20)

a002 = BankAccount("a002")
a002.deposit(1000).deposit(200).withdraw(50).withdraw(60).withdraw(20).withdraw(200).yield_interest().display_account_info()

print("\r")

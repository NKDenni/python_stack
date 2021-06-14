# Objectives:
    # Practice creating a class and making instances from it
    # Practice accessing the methods and attributes of different instances

# Functionallity
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    # display_user_balance(self) - have this method print the user's name and account balance to the terminaleg. "User: Guido van Rossum, Balance: $150
    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposite(self, amount):
        self.account_balance += amount
        print("\n" f"{self.name}'s new balance is ${amount}.")
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print("\n" f"{self.name}'s new balance is ${amount}.")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("\n" f"${amount} has been transfered to {other_user.name}'s account.")

    def display_user_balance(self):
        print("\n" f"Account for {self.name}, email {self.email} has a current balance of ${self.account_balance}.")


John = User("John Doe", "JohnD@gmail.com")
Eric = User("Eric Ericson", "EE@gmail.com")
Bob = User("Bob Builder", "BB@gmail.com")
print("\n", "-"*20, "New Transaction", "-"*20)

Bob.make_deposite(1000)
Bob.make_deposite(200)
Bob.make_deposite(900)
Bob.make_withdrawal(400)
Bob.display_user_balance()
print("\n", "-"*20, "New Transaction", "-"*20)

John.make_deposite(300)
John.make_deposite(2000)
John.make_withdrawal(100)
John.make_withdrawal(600)
John.display_user_balance()
print("\n", "-"*20, "New Transaction", "-"*20)

Eric.make_deposite(5000)
Eric.make_withdrawal(200)
Eric.make_withdrawal(100)
Eric.make_withdrawal(300)
Eric.display_user_balance()
print("\n", "-"*20, "New Transaction", "-"*20)

Bob.transfer_money(Eric, 400)
print("\n", "-"*20, "End of Program", "-"*20)
print("\r")

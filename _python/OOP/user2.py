class User:
    def __init__(self, name):
        self.account = 0
        self.name = name

    def current_balance(self):
        print(f'Current balance for {self.name} is ${self.account}')
        return self

    def make_deposite(self, amount):
        self.account += amount
        print('New balance is: $',self.account)
        return self
    
    def make_withdrawal(self, amount):
        if self.account == 0:
            print('Insufficent funds to make a withdrawl')
        elif self.account < amount:
            print('Insufficent funds to withdrawl $',amount)
        else:
            self.account -= amount
            print(f'Amount withdrawn: ${amount}. Current balance: ${self.account}')
        return self
    
    def transfer(self, amount, other):
        if self.account == 0:
            print('Insufficent funds to make a transfer from this account')
        elif self.account < amount:
            print(f'Insufficent funds to transfer ${amount}')
        else:
            self.account -= amount
            other.account += amount
            print(f'${amount} was transfered from {self.name} to {other.name}')
            print(f'Current balance for {self.name} is ${self.account}')
            print(f'Current balance for {other.name} is ${other.account}')
        return self


Greg = User('Greg')
Greg.make_deposite(200)

Nathan = User('Nathan')
Nathan.make_deposite(500)
Nathan.transfer(200,Greg)


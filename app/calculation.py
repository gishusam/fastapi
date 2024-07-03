
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds('Insufficient funds')
        self.balance -= amount

    def get_balance(self):
        return self.balance
    

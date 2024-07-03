import pytest
from app.calculation import add, subtract, multiply, divide, BankAccount,InsufficientFunds

@pytest.fixture
def zero_balance_account():
    return BankAccount()

@pytest.fixture
def account():
    return BankAccount(100)

@pytest.mark.parametrize("x, y, expectation", [
    (1,3,4),
    (2,3,5),
    (3,3,6) 
])

def test_add(x, y, expectation):
    assert add(x, y) == expectation

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():    
    assert divide(6, 3) == 2

def test_bank_initial_balance(account):
    assert account.get_balance() == 100

def test_default_initial_balance(zero_balance_account):
    assert zero_balance_account.get_balance() == 0  

def test_deposit(account):
    account.deposit(50)
    assert account.get_balance() == 150

def test_withdraw(account):
    account.withdraw(50)
    assert account.get_balance() == 50

@pytest.mark.parametrize("deposit, withdrew, expectation", [
    (600,300,300),
    (500,300,200),
    (1200,300,900) 
])

def test_deposit_withdraw(zero_balance_account, deposit, withdrew, expectation):
    zero_balance_account.deposit(deposit)
    zero_balance_account.withdraw(withdrew)
    assert zero_balance_account.get_balance() == expectation

def test_insufficient_funds(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(200)   






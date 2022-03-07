from utils import print_failure, print_success


class Account:

    # Minimum Balance
    _MIN_BAL = 20

    def __init__(self, holder_name, holder_address, holder_age, account_number):
        self.holder_name = holder_name
        self.holder_address = holder_address
        self.holder_age = holder_age
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print_success(f'Amount {amount} deposited. New Balance: {self.balance}')
        else:
            message = f'Cannot Deposit {amount} to account for Account Number {self.account_number}'
            print_failure(message)
            raise Exception(message)

    def withdrawal(self, amount):
        if self.balance - amount >= self.MIN_BAL:
            self.balance -= amount
            print_success(f'Amount {amount} withdrawn. New Balance: {self.balance}')
        else:
            message = f'Cannot Withdraw {amount} from account for Account Number {self.account_number}'
            print_failure(message)
            raise Exception(message)

    def __str__(self):
        return f'Name: {self.holder_name}, Balance: {self.balance}'

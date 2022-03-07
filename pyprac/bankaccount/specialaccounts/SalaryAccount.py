from ..account import Account, print_success, print_failure


class SalaryAccount(Account):

    _MIN_BAL = 0
    __POINTS = 0

    @property
    def points(self):
        return self.__POINTS

    @points.setter
    def set_points(self, value):
        self.__POINTS = value

    def __init__(self, holder_name, holder_address, holder_age, account_number):
        super().__init__(holder_name, holder_address, holder_age, account_number)
        self.holder_name = holder_name
        self.holder_address = holder_address
        self.holder_age = holder_age
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        try:
            super().deposit(amount)
            self.POINTS += round(amount / 100)
            print_success(f'Point Balance: {self.POINTS}')
        except Exception as e:
            print_failure(e)

    def __str__(self):
        return f'Name: {self.holder_name}, Balance: {self.balance}, Points: {self.POINTS}'

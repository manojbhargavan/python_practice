from bankaccount.account import Account
from bankaccount.specialaccounts.SalaryAccount import SalaryAccount

simple_account = Account('John', '19 Kensington AVE, NJ', 45, 1)
print(simple_account)
simple_account.deposit(100)
print(simple_account)
try:
    simple_account.withdrawal(1000)
except Exception as e:
    print(e)
simple_account.withdrawal(70)
simple_account.withdrawal(9)
print(simple_account)

sal_account = SalaryAccount('Marshal', '20 Kensington AVE, NJ', 45, 1)
'''
print(sal_account)
sal_account.deposit(200)
print(sal_account)
sal_account.withdrawal(200)
print(sal_account)
'''
sal_account.points = 10
print(sal_account.points)


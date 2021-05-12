class BankAccount:
    all_accts = []

    def __init__(self, int_rate = 0.01, balance =0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accts.append(self)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('please enter a positive amount')
        return self
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accts:
            account.display_account_info
        

account1 = BankAccount()
account2 = BankAccount(.03, 100000)

account1.deposit(500).deposit(600).deposit(1000).withdraw(800).yield_interest().display_account_info()

account2.deposit(10000).deposit(33000).withdraw(1500).withdraw(1200).withdraw(23000).withdraw(5).yield_interest().display_account_info()

BankAccount.all_balances()
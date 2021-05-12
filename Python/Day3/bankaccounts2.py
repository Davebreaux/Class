class BankAccount:
    all_accts = []

    def __init__(self, int_rate, balance): 
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
            account.display_account_info()
        

class User:
    

    def __init__(self, name, email):
        self.account_list = []
        self.name = name
        self.email = email
        self.num_accts = 1
        self.account_list.append(BankAccount(int_rate=0.02, balance=0))
    def make_deposit(self, amount, acct_num = 1):
        self.account_list[self.which_account() - 1].deposit(amount)
        return self
    def make_withdrawal(self, amount,):
        self.account_list[self.which_account()-1].withdraw(amount)
        return self
    def make_transfer(self, other_user, amount):
        self.account_list[self.which_account()-1].withdraw(amount)
        other_user.account_list[other_user.which_account() - 1].deposit(amount)
        return self
    def display_user_balance(self,):
        print(f"Hello, {self.name}. You have ${self.account_list[self.which_account()-1].balance} in your account")
        return self
    def add_account(self):
        self.account_list.append(BankAccount(int_rate=0.02, balance=0))
        self.num_accts += 1
    def which_account(self):
        if self.num_accts > 1:
            acct_num = input(f'{self.name}, you have {self.num_accts} accounts. Select an account number between 1 and {self.num_accts}')
            return int(acct_num)
        else:
            return 1





acct1 = User('Dave Breaux', 'me@myself.com')
acct2 = User('Bill Gates', 'billy@billionaire.com')
acct1.add_account()
acct2.make_deposit(85000000000)
acct2.add_account()
acct2.make_deposit(100000)
acct1.make_deposit(1000).make_withdrawal(200)
acct2.make_transfer(acct1, 10000)

acct1.display_user_balance()
acct2.display_user_balance()
BankAccount.all_balances()


# acct1.add_account()



# account1 = BankAccount()
# account2 = BankAccount(.03, 100000)

# account1.deposit(500).deposit(600).deposit(1000).withdraw(800).yield_interest().display_account_info()

# account2.deposit(10000).deposit(33000).withdraw(1500).withdraw(1200).withdraw(23000).withdraw(5).yield_interest().display_account_info()

# BankAccount.all_balances()
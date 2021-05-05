class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"Hello, {self.name}. You have ${self.account_balance} in your account")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
dave = User("Dave Breaux", "dave.breaux@gmail.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


monty.make_deposit(3000).make_deposit(1300).make_withdrawal(500).make_withdrawal(1200).display_user_balance()

dave.make_deposit(20000).make_withdrawal(5000).make_withdrawal(200).make_withdrawal(150).display_user_balance()

monty.make_transfer(dave, 1000)

dave.display_user_balance()
monty.display_user_balance()





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
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

john=User('John Doe', 'JDoe@gmail.com')
mike=User('Mike Hart', 'MHart@gmail.com')
bill=User('Bill Williams', 'BWilliams@gmail.com')

john.make_deposit(100).make_deposit(50).make_deposit(1000).make_withdrawal(950).display_user_balance()

mike.make_deposit(500).make_deposit(500).make_withdrawal(200).make_withdrawal(50).display_user_balance()

bill.make_deposit(2000).make_withdrawal(500).make_withdrawal(100).make_withdrawal(50).display_user_balance()

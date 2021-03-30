
#  Create a file with the User class, including the __init__ and make_deposit methods  
#  Add a make_withdrawal method to the User class  
#  Add a display_user_balance method to the User class  
#  Create 3 instances of the User class  
#  Have the first user make 3 deposits and 1 withdrawal and then display their balance  
#  Have the second user make 2 deposits and 2 withdrawals and then display their balance  
#  Have the third user make 1 deposits and 3 withdrawals and then display their balance  
#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount): 
    	self.account_balance += amount	
    
    def make_withdrawal(self, amount): 
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

john=User('John Doe', 'JDoe@gmail.com')
mike=User('Mike Hart', 'MHart@gmail.com')
bill=User('Bill Williams', 'BWilliams@gmail.com')

john.make_deposit(100)
john.make_deposit(50)
john.make_deposit(1000)
john.make_withdrawal(950)
john.display_user_balance()

mike.make_deposit(500)
mike.make_deposit(500)
mike.make_withdrawal(200)
mike.make_withdrawal(50)
mike.display_user_balance()

bill.make_deposit(2000)
bill.make_withdrawal(500)
bill.make_withdrawal(100)
bill.make_withdrawal(50)
bill.display_user_balance()

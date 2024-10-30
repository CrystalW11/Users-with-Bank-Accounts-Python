class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0.0):
        self.int_rate = int_rate
        self.balance = balance  
        
        BankAccount.all_accounts.append(self) # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the user class soon
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
                # we use the static method here to evaluate 
                # if we can with draw the funds without going negative
        if  BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            self.balance -= 5 # penalty for insufficient funds
            print("Insufficient Funds")
        return self
        # static methods have no acess to any attribute
        # only to what is passed into it
        
    @staticmethod
    def can_withdraw(balance, amount):
        return balance - amount >= 0
            
    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
                
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
            #methods
    def make_deposit(self, amount):
            # call the deposit morthod of the assoicated BankAccount instance
        print(f"Name: {self.name}")
        self.account.deposit(amount)
        self.account_balance() # updated the balance after each deposit
        print(f"{self.name} made a deposit of ${amount}.")
    
    def account_balance(self):
        print(f"{self.name}'s account balance is ${self.account.balance}")
        
    def make_withdraw(self, amount):
            # we use the static method here to evaluate 
            # if we can withdraw the funds without going negative
        self.account.withdraw(amount)
        return self

user1 = User("Crystal", "crystal@gmail.com")
user1.account.display_account_info().yield_interest().display_account_info().make_deposit(3000.00).make_deposit(6000.00).make_deposit(9000.00).account_balance().make_deposit(100.00).make_withdraw(300.00)


user2 = User("Kathy", "kathy@gmail.com")
user2.account.display_account_info()
user2.make_deposit(50000.00)

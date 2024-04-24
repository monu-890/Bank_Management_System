class Account:
    def __init__(self,account_number,customer,balance=0.0):
        self.account_number=account_number
        self.customer=customer 
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount 
        return self.balance 
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount 
        else:
            print("Insufficient funds")
            return None
        
    def get_balance(self):
        return self.balance
    
    
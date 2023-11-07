class Result:
    def __init__ (self, isSuccess, message, value = None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value


class BankAccount:
    
    def __init__(self,balance = 0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def try_withdraw(self,amount):
        if(self.balance > amount):
            self.balance -= amount
            return Result(True,"Withdraw",amount)
    
        return Result(False,"Not Withdraw",amount)
            
    def __str__(self):
        return str(self.balance)

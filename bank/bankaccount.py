from result import Ok, Error 

class BankAccount:
    
    def __init__(self,balance = 0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def try_withdraw(self,amount):
        if(self.balance > amount):
            self.balance -= amount
            return Ok("Money was paid",amount)
    
        return Error("Money wasn't paid",amount)
            
    def __str__(self):
        return str(self.balance)
    
    
    
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance = 0, minimumBalance = 1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance
        
    def try_widthdraw(self,amount):
        if(self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Error("It failed, an attempt to exceed the threshold", amount)

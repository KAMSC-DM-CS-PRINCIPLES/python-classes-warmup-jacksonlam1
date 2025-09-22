# TODO create class BankAccount

    # create BankAccount below this
class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance
    def get_balance(self):
        self.balance
        return self.balance
    def deposit(self,dep):
        if dep > 0:
            self.balance+=dep
        return self.balance
    def withdraw(self,amnt):
        if amnt >= 0:
            self.balance-=amnt
            return self.balance
        else:
            return "Insufficient Funds"

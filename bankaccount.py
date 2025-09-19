# TODO create class BankAccount

    # create BankAccount below this
class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance
    def get_balance(self):
        self.balance
        return self.balance
    def deposit(self,dep):
        self.balance
        if dep < 0:
            return self.balance
        else:
            self.balance += dep
            return self.balance
    def withdraw(self ,amnt):
        self.balance
        if amnt > 0:
            return self.balance
        else:
            if self.balance-amnt<0:
                return "Insufficient Funds"
            else:
                balance -= amnt
                return self.balance

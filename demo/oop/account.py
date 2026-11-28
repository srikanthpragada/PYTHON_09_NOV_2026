class Account:
    def __init__(self, acc_num: int, cust_name: str, balance: int = 0):
        self.acc_num = acc_num
        self.cust_name = cust_name
        self.balance = balance

    def deposit(self, amount: int = 0):
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid Amount!')

    def withdraw(self, amount: int = 0):
        if amount > 0:
            if self.balance - amount >= 0:
                self.balance -= amount
            else:
                print('Insufficient Funds!')
        else:
            print('Invalid Amount!')


    def getbalance(self):
        return self.balance


    def show(self):
        print("Account Number:", self.acc_num)
        print("Customer Name:", self.cust_name)
        print("Balance:", self.balance)

    

a1 = Account(1, "Rossum", 10000)
a1.deposit(5000)
a1.withdraw(2000)
print(a1.getbalance())

class Bank(object):
    def __init__(self):
        self.amount = 100000000


    def loan(self, amount):
        self.amount -= amount
        return amount


    def recieve(self, amount):
        self.amount += amount
        return amount
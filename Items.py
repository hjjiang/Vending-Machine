class Items(object):
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def getAmount(self):
        return self.amount

    def addAmount(self, amount):
        self.amount += amount

    def setAmount(self, amount):
        self.amount = amount
        
    def getPrice(self):
        return self.price
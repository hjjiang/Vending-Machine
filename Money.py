class Money(object):
    def __init__(self, value, amount):
        self.value = value
        self.amount = amount
        self.TotalAmount = value * amount
    
    def getTotalAmount(self):
        return self.TotalAmount

    def getAmount(self):
        return self.amount

    def addAmount(self, amount):
        self.amount += amount
        self.TotalAmount = self.getValue() * self.amount

    def setAmount(self, amount):
        self.amount = amount
        self.TotalAmount = self.getValue() * self.amount

    def getValue(self):
        return self.value

class Penny(Money):
    def __init__(self, amount):
        super(Penny, self).__init__(.01,amount)

class Nickel(Money):
    def __init__(self, amount):
        super(Nickel, self).__init__(.05,amount)

class Dime(Money):
    def __init__(self, amount):
        super(Dime, self).__init__(.10,amount)

class Quarter(Money):
    def __init__(self, amount):
        super(Quarter, self).__init__(.25,amount)

class OneDollar(Money):
    def __init__(self, amount):
        super(OneDollar, self).__init__(1.00,amount)

class FiveDollars(Money):
    def __init__(self, amount):
        super(FiveDollars, self).__init__(5.00,amount)

class TenDollars(Money):
    def __init__(self, amount):
        super(TenDollars, self).__init__(10.00,amount)

class TwentyDollars(Money):
    def __init__(self, amount):
        super(TwentyDollars, self).__init__(20.00,amount)

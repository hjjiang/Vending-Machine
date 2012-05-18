import Items
import Money
import Pocket

class VendingMachine(object):
    def __init__(self):
        self.balance = Pocket.Pocket()
        self.product = {}

    def stock(self, itemName, amount, price):
        item = Items.Items(itemName, amount, price)
        self.product[itemName] = item

    def showStock(self):
        print "MENU"
        for itemName in self.product:
            print "%s, amount: %s, price: $%s" %(itemName, self.product[itemName].getAmount(), self.product[itemName].getPrice())
    
    def restock(self, itemName, amount):
        if (itemName in self.product):
            self.product[itemName].addAmount(amount) 

    def deposit(self, pocket, typeMoney, amount):
        print "Depositing Money...."
        if (pocket.getAmountOf(typeMoney) == 0):
            print "Don't have any", typeMoney
        elif (pocket.getAmountOf(typeMoney) < amount):
            print "You Don't have", amount, typeMoney, "you have", pocket.getAmountOf(typeMoney)
        else: 
            pocket.addAmountOf(typeMoney, amount*(-1))
            for x in range(0, amount):
                self.balance.addAmountOf(typeMoney, 1)
                print "Machine has: $%s" %self.balance.getGrandTotal()
            print "deposited", amount, typeMoney

    def buy(self, itemName):
        if (itemName in self.product):
            if (self.product[itemName].getAmount() != 0):
                if (self.balance.getGrandTotal() >= self.product[itemName].getPrice()):
                    self.balance.setGrandTotal(self.balance.getGrandTotal() - self.product[itemName].getPrice())
                    self.product[itemName].addAmount(-1)
                    # print self.product[itemName].getAmount()
                    print "vendingMachine spat out %s, $%s left in machine" %(itemName, self.balance.getGrandTotal())
                else:
                    print "Ipod cost: %s, need $%s more" %(self.product[itemName].price, (self.product[itemName].price - self.balance.getGrandTotal()))
            else:
                print itemName, "out of stock"
        else:
            print "no item called", itemName, "in Vending Machine"

    def returnMoney(self,pocket):
        if (self.balance.getGrandTotal()!=0):
            print "Returning Money...."
            pocket.addAmountOf("TwentyDollars", self.balance.getAmountOf("TwentyDollars"))
            pocket.addAmountOf("TenDollars", self.balance.getAmountOf("TenDollars"))
            pocket.addAmountOf("FiveDollars", self.balance.getAmountOf("FiveDollars"))
            pocket.addAmountOf("OneDollars", self.balance.getAmountOf("OneDollars")) 
            pocket.addAmountOf("Quarters", self.balance.getAmountOf("Quarters"))
            pocket.addAmountOf("Dimes", self.balance.getAmountOf("Dimes"))
            pocket.addAmountOf("Nickels", self.balance.getAmountOf("Nickels"))
            pocket.addAmountOf("Pennies", self.balance.getAmountOf("Pennies"))
            self.balance.setGrandTotal(0)
            print "...Done"



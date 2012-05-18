import Money

class Pocket(object):
    def __init__(self):
        self.Purse = {}
        self.Purse["Pennies"] = Money.Penny(0)
        self.Purse["Nickels"] = Money.Nickel(0)
        self.Purse["Dimes"] = Money.Dime(0)
        self.Purse["Quarters"]= Money.Quarter(0)
        self.Purse["OneDollars"] = Money.OneDollar(0)
        self.Purse["FiveDollars"] = Money.FiveDollars(0)
        self.Purse["TenDollars"] = Money.TenDollars(0)
        self.Purse["TwentyDollars"] = Money.TwentyDollars(0)
        self.GrandTotal = 0

    def getGrandTotal(self):
        return self.GrandTotal

    def addAmountOf(self, typeOfMoney, amount):
        self.Purse[typeOfMoney].addAmount(amount)
        self.GrandTotal += self.Purse[typeOfMoney].getValue()*amount

    def getAmountOf(self, typeOfMoney):
        return self.Purse[typeOfMoney].getAmount()

    def getValueOf(self, typeOfMoney):
        return self.Purse[typeOfMoney].getValue()

    def getTotalAmountOf(self, typeOfMoney):
        return self.Purse[typeOfMoney].getTotalAmount

    def showChange(self):
        print self.getAmountOf("Pennies"), "Pennies"
        print self.getAmountOf("Nickels"), "Nickels"
        print self.getAmountOf("Dimes"), "Dimes"
        print self.getAmountOf("Quarters"), "Quarters"
        print self.getAmountOf("OneDollars"), "OneDollars"
        print self.getAmountOf("FiveDollars"), "FiveDollars" 
        print self.getAmountOf("TenDollars"), "TenDollars"
        print self.getAmountOf("TwentyDollars"), "TwentyDollars"

    def setGrandTotal(self, gTotal):
        def setAmountOf(self, typeOfMoney, amount):
            self.Purse[typeOfMoney].setAmount(amount)
        self.GrandTotal = gTotal
        # print "gTotal:",gTotal
        if gTotal != 0:    
            if gTotal >= self.getValueOf("TwentyDollars"):
                temp = int (gTotal/self.getValueOf("TwentyDollars"))
                setAmountOf(self,"TwentyDollars", temp)
                gTotal = gTotal - (temp*self.getValueOf("TwentyDollars"))
            else:
                setAmountOf(self,"TwentyDollars", 0)
            
            if gTotal >= self.getValueOf("TenDollars"):
                temp = int (gTotal/self.getValueOf("TenDollars"))
                setAmountOf(self,"TenDollars", temp)
                gTotal = gTotal - (temp*self.getValueOf("TenDollars"))
            else:
                setAmountOf(self,"TenDollars", 0)
            
            if gTotal >= self.getValueOf("FiveDollars"):
                temp = int (gTotal/self.getValueOf("FiveDollars"))
                setAmountOf(self,"FiveDollars", temp)
                gTotal = gTotal - (temp*self.getValueOf("FiveDollars"))
            else:
                setAmountOf(self,"FiveDollars", 0)

            if gTotal >= self.getValueOf("OneDollars"):
                temp = int (gTotal/self.getValueOf("OneDollars"))
                setAmountOf(self,"OneDollars", temp)
                gTotal = gTotal - (temp*self.getValueOf("OneDollars"))
            else:
                setAmountOf(self,"OneDollars", 0)

            if gTotal >= self.getValueOf("Quarters"):
                temp = int (gTotal/self.getValueOf("Quarters"))
                setAmountOf(self,"Quarters", temp)
                gTotal = gTotal - (temp*self.getValueOf("Quarters"))
            else:
                setAmountOf(self,"Quarters", 0)

            if gTotal >= self.getValueOf("Dimes"):
                temp = int (gTotal/self.getValueOf("Dimes"))
                setAmountOf(self,"Dimes", temp)
                gTotal = gTotal - (temp*self.getValueOf("Dimes"))
            else:
                setAmountOf(self,"Dimes", 0)

            if gTotal >= self.getValueOf("Nickels"):
                temp = int (gTotal/self.getValueOf("Nickels"))
                setAmountOf(self,"Nickels", temp)
                gTotal = gTotal - (temp*self.getValueOf("Nickels"))
            else:
                setAmountOf(self,"Nickels", 0)

            if gTotal >= self.getValueOf("Pennies"):
                temp = int(round(gTotal/self.getValueOf("Pennies")))
                setAmountOf(self,"Pennies", temp)
                gTotal = gTotal - (temp*self.getValueOf("Pennies"))
            else:
                setAmountOf(self,"Pennies", 0)
        else:
            for money in self.Purse:
                setAmountOf(self,money, 0)
            # setAmountOf(self,"TwentyDollars", 0)
            # setAmountOf(self,"TenDollars", 0)
            # setAmountOf(self,"FiveDollars", 0)
            # setAmountOf(self,"OneDollars", 0)
            # setAmountOf(self,"Quarters", 0)
            # setAmountOf(self,"Dimes", 0)
            # setAmountOf(self,"Nickels", 0)
            # setAmountOf(self,"Pennies", 0)
                

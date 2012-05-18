import Machine
import Pocket

VendingMachine = Machine.VendingMachine()
VendingMachine.stock("Ipod", 0, 99.99) #(name, amount, price)
VendingMachine.stock("Pepsi", 10, 1.57)  #(name, amount, price)
VendingMachine.showStock()
print ""
Wallet = Pocket.Pocket()
Wallet.addAmountOf("TwentyDollars", 4)
# Wallet.addAmountOf("TenDollars", 3)
VendingMachine.deposit(Wallet, "TwentyDollars", 4)
VendingMachine.deposit(Wallet, "TenDollars", 3)
print ""
VendingMachine.buy("Ipod")
VendingMachine.buy("Pepsi")
VendingMachine.buy("Coke")
print ""
VendingMachine.returnMoney(Wallet)
print "Inside of Wallet:"
Wallet.showChange()
print "Wallet GrandTotal: $%s" %Wallet.getGrandTotal()
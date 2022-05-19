from DictionaryConcept import Dictionaryproduct
from Python_learning.Calculation import storecalculation
from Python_learning.Store import Store

class Billing(Store,Dictionaryproduct,storecalculation):
    def billingcalculation(self,productname,quantity):
        discount=self.Storeinformation()
        price=self.Productavailabilityexist(productname,quantity)
        #Totalamount=self.calculateTotalPrice(quantity,price,discount,tax)
        Totalamount = self.calculateTotalPrice(quantity, int(price), discount)
        print("Totalamount "+str(Totalamount))
        print("Price of the product "+str(price))
        print("quantity "+str(quantity))
        print("discount of the product "+str(discount))


obj=Billing()
obj.billingcalculation("Oreo",2)



class storecalculation():
    def calculateTotalPrice(self,quantity, price, discount):
        actualtax = self.tax(price)
        return(quantity *price) + actualtax -(discount)

    def tax(self,price):
        taxvalue =price* 0.20
        print("Tax  " + str(round(taxvalue, 2)))
        return taxvalue






class product():
    subtotal=0

    def createProduct(self,product,quantity,price):
        try:
           add_to_basket= quantity*price
           print(product+" "+str(quantity)+" "+str(price)+" "+str(add_to_basket))
           self.subtotal+=add_to_basket
        except(ZeroDivisionError,Exception,IndexError):
           print("An exception occurred")

obj=product()
obj.createProduct("laptop",12,34)







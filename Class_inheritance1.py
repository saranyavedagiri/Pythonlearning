class inheritance():
    def multiplication(self,a,b):
        mul=a*b
        print("The value of the multiplication "+str(mul))
    def addition(self,a,b):
        add=a-b
        print("The value of the addition  "+str(add))
    def allmethod(self,a,b):
        self.multiplication(a,b)
        self.addition(a,b)

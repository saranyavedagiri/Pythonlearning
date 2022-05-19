class excp():
    def divide(self,a,b):
        try:
            div=a/b
            print("divide these two values: "+str(div))
        except:
            print("An exception occurred")
    def addition(self,a,b):
        try:
            add=a+b
            print("Add these two values: "+str(add))
        except:
            pass
    def subtraction(self,a,b):
        try:
            sub=a-b
            print("Subtraction these two values: "+str(sub))
        except:
            pass

obj=excp()
obj.addition(3,5)
obj.divide(5,2)
obj.subtraction(16,4)
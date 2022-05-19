class excp():
    list=[10,20,30]
    def division(self,a,b,):
        try:
            #sum = "python" + b
            div=a/b
            val=self.list[3]
            print("The division value should  "  +str(div))
        except ZeroDivisionError:
            print("Divided by zero Exception Raised")
        except IndexError:
            print("Index is out of Range")
        except IndentationError:
            print("Indentation error is occurred")
        except:
            print("Exception Raised")
        finally:
            print("Division completed")

    def substraction(self,a,b):
        try:
            sub=a-b
            print("the substraction value is  " +str(sub))
        except:
            pass
    def addition(self,a,b):
        try:
            add=a+b
            print("Addition value is  " +str(add))
        except IndentationError:
            print("Indentation error occurred")

obj=excp()
obj.division(2,5)
obj.substraction(6,2)
obj.addition(3,7)

class rais():
    def division(self,a,b):
        try:
           div= a / b
           print("Division value "+str(div))
           if div>5:
               print("excepted value")
           else:
               # As a Python developer you can choose to throw an exception if a condition occurs.To throw (or
               # raise) an exception, use the raise keyword.

           raise ZeroDivisionError()

        except ZeroDivisionError:
            print("Divided by zero Exception Raised")
        except IndexError:
            print("Index is out of Range")
        except:
            print("Exception Raised")
        finally:
            print("Division completed")

    def addition(self,a,b):
        try:
         add=a+b
         if add>12:
            print("The value is greater than 12 : "+str(add))
         else:
             print("The value is less than 12 :" +str(add))
        except:
            pass



obj=rais()
obj.division(6,2)
obj.addition(5,8)
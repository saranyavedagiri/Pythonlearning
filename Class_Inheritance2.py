from Python_learning.Class_inheritance1 import inheritance


class inherit(inheritance):
    def division(self,a,b):
        try:
          div=a/b
          print("the value of the division is "+str(div))
        except:
            print("An exception error occurred")
        finally:("division inheritance")

    def addition(self,a,b):
        try:
            add=a+b
            print("The value of the addition is "+str(add))
        except:
            pass

obj=inherit()
obj.division(20,5)
obj.addition(3,5)
obj.allmethod(5,2)
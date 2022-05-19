class overloading():
  """""  def raise_func(self):
        i=17
        if i<18:
            raise Exception("you are not eligible")
            print("error")
        else:
            print("you are eligible")

    #overloading

    def raise_func(self,i):

        if i<18:
            raise Exception("you are not eligible")
            print("error")
        else:
            print("you are eligible")
            """
  def discount(self,product1,product2):
      dis=0.2
      print("you are eligible for "+str(dis) +"percentage discount")

  def discount(self, product1, product2,product):
      dis = 0.3
      print("you are eligible for " + str(dis) + "  percentage discount")


obj=overloading()
#obj.raise_func(14)
obj.discount("toy","car","phone")


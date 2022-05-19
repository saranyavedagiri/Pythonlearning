from Python_learning.Polymorphism_Methodoverridding1 import override


class override1(override):
    def multiply(self):
      print("This is child method")


obj=override1()
obj.multiply()

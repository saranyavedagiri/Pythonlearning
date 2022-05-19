"""
def add_product(quantity,price):
    Total_cost = quantity * price
    return(Total_cost)
add_product(4.3,13.34)
print(y)
print(round(y,2))

def add_product(quantity,price):
    Total_cost = quantity * price
    #return(Total_cost)
    return (round(Total_cost,2))
print(add_product(4.3,13.34))
#print(Total_cost)
#print(round(Total_cost,2))
"""
"""
global total,total1
total1=0.00
productn1= "Laptop"
quantity_a1= 2
price_b1= 12.34

productn2= "iphone"
quantity_a2= 2
price_b2= 23.45

productn3= "iphone1"
quantity_a3= 2
price_b3= 34.56


total=0.00
def add_product(productn, quantity_a, price_b):

    result1=quantity_a*price_b
    #print(productn  +"\t" +quantity_a+ "\t" +price_b)
    print(productn + "\t" + str(quantity_a) + "\t" + str(result1))

    total =result1
    if total>0:
        total =total+total1
    print(total)
add_product(productn1,quantity_a1,price_b1)
add_product(productn2,quantity_a2,price_b2)
add_product(productn3,quantity_a3,price_b3)

"""

global temp
temp=0.00
def addproduct(product,quantity,price):
    global temp
    result=quantity*price
    print(product+" "+str(quantity)+" "+str(result))
    temp+=result
addproduct("laptop",3,3.5)
addproduct("Iphone",4,4.5)
print(temp)



import re
#regular expression(re)
class Textfile():

    def fileread(self):
        f = open("C:\\Users\\SaranyaV\\OneDrive - Specialist Lending\\Desktop\\selenium with python\\project\\input.txt","r")
        #print(f.read())
        #print(f.read(10))
        #print(f.read(10))
        #print(f.readline())
        #print(f.readlines())
        iterate = f.readlines()
        for xc in iterate:
            x=re.split("\S",xc)
            print(x)
            print(xc)
        f.close()

obj=Textfile()
obj.fileread()
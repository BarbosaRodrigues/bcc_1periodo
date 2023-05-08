from audioop import mul
from re import I


#PROG-01

n= int(input("Numero: "))
i=0

while i<11:
    mult=n*i
    print(n, "x", i,"=", mult)
    i+=1
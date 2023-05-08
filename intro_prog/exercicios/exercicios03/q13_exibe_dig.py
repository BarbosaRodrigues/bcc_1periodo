#___________________________________________________


print("------EXIBE-DIGITOS-DE-NUMERO------")

n = int(input())
d=0

while n>0:
    d= n%10
    n= n//10
    print(n," --- ", d)

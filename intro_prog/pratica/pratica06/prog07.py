print("------WHILE------")
#WHILE VARIAVEL DEFINIDA

a=1
print("\n")

while a<=5:
    if a == 5:
        print("%d "%a, end='')
    else:
        print("%d, "%a, end='')
    a+=1

print("\nFIM\n")

#____________________________________________________

print("---WHILE-com-n---\n")
#WHILE VARIAVEL ESCANEADA

a=1
n=int(input("qtd: "))
print("\n")

while a<=n:
    if a == n:
        print("%d "%a, end='')
    else:
        print("%d, "%a, end='')
    a+=1

print("\nFIM\n")

#____________________________________________________

print("---WHILE-ATE-n---\n")
#WHILE SEM O ULTIMO NUMERO

a=1
n=int(input("qtd: "))
print("\n")

while a<n:
    print("%d, "%a, end='')
    a+=1

print("\nFIM\n")

#____________________________________________________

print("---IMPRIMIR-COM-\B---\n")
#WHILE IMPRIMIR COM \B

a=1
n=int(input("qtd: "))
print("\n")

while a<n:
    print("%d, "%a, end='')
    a+=1

print("\b\b \nFIM\n")

#____________________________________________________

print("---SOMAR-ENTRADAS---")
#SOMAR ENTRADAS

a=1
SOMA=0

print("\n")

while a!=0:
    a=int(input(" > "))
    SOMA+=a

print("\nSOMA: %d\n"%SOMA)
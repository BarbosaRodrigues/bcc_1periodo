#__________________________________________________________

from operator import contains


print("\n-----MULTIPLICACAO-USANDO-ADICAO-----\n")

n1 = int(input("dois numeros para a multiplicacao:\n"))
n2 = int(input())
soma=0
for i in range(1,n2+1):
    soma = soma+n1
print(n1, "x ", n2, "= ",soma)

#___________________________________________________________


print("\n-----DIVISAO-E-RESTO-----\n")

n1=int(input("Digite dois numeros inteiros positivos:\n"))
n2=int(input())
resultado=n1
contador=0

while resultado>=n2:
    resultado=resultado-n2
    contador+=1

print(n1, "/", n2, "=", contador," | ", n1, "%", n2, "=", resultado)

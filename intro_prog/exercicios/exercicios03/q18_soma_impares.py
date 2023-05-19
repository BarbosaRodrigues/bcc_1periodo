print("\n____Quadrado_De_Um_Numero_Natural____\n")

val1 = int(input("informe um numero: "))
quadrado=0
contador = 0
prova=0

while contador<val1:
    prova+=1
    if prova%2!=0:
        quadrado=quadrado+prova
        contador+=1
print("\n", val1,"\b² =", quadrado, end="")
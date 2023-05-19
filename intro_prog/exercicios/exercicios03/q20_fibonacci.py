
from ast import Break


print("\n____n-esimo_termo_da_serie_Fibonacci____\n")

n = int(input("qual a posicao do numeor?\n"))
termo=1
contador=0
anterior=0

while contador<n:
    if n<3:
        print("ERRO")
        Break
    else:
        if termo==1:
            soma1=termo+termo
            print(termo, "\b,", termo, ",", end="")
            anterior=termo
            termo=termo+anterior
        elif termo==2:
            print(soma1, ",", end="")
            a=anterior
            anterior=termo
            termo=termo+a
        elif termo>2:
            print(termo, ",", end="")
            a=anterior
            anterior=termo
            termo=termo+a
        contador+=1


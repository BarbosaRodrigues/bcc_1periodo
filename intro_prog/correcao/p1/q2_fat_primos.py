# >> DADO UM NUMERO INT POSITIVO, IMPRIME SEUS FATORES PRIMOS
# >> possivel solucao

n = int(input("\nnumero\n"))

if n<0:
    print("ERRO: negativo")
else:
    div=2
    while n>1:
        if n%div==0:
            n=n//div
            print(div, end="")
            print(" ", end="")
        else:
            div+=1
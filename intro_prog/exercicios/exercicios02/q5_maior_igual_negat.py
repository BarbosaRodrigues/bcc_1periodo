#____________________________________________________________________
print("\n------IMPRIME-O-MAIOR-VALOR-EXCESSOES-NEGATIVO-E-IGUAIS------\n")

valor1 = int(input("informe valor 1: "))
valor2 = int(input("informe valor 2: "))

if valor1 == valor2:
    print("\nvalores iguais")
else:
    if valor1<0 or valor2<0:
        print("Erro: numero negativo.")
    else:
        if valor1 > valor2:
            print("\nmaior: %d" % valor1)
        else:
            print("\nmaior: %d" % valor2)
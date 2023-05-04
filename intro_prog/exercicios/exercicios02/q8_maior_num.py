#____________________________________________________________________
print("\n------IMPRIME-O-MAIOR-------\n")

valor1 = float(input("informe 4 numeros: \n"))
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())

if valor1 == valor2 and valor1==valor3 and valor1==valor4:
    print("\nvalores iguais")
else:
    if valor1 >= valor2 and valor1 >= valor3 and valor1 >= valor4:
        print("\nmaior: %d" % valor1)
    else:
        if valor2 >= valor1 and valor2 >= valor3 and valor2 >= valor4:
            print("\nmaior: %d" % valor2)
        else:
            if valor3 >= valor1 and valor3 >= valor2 and valor3 >= valor4:
                print("\nmaior: %d" % valor3)
            else:
                print("\nmaior: %d" % valor4)

            
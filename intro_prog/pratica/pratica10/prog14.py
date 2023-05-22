
# >> questao 2 LISTA 5
def exibir(linhas, colunas):
    print()
    for i in range(linhas):
        for j in range(colunas):
            print("|", end="")
        print()


# >> questao 4 LISTA 5
def exibir2(linhas, colunas):
    espaco = linhas - 1
    print()
    for i in range(linhas):
        for j in range(espaco):
            print(" ", end="")
        for j in range(colunas):
            print("¨", end="")
        print()
        espaco-=1


exibir(4,10)
exibir2(6, 9)
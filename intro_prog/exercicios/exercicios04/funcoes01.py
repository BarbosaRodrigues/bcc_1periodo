import random
#_____________________________________________________
def somar(n: int):
    print("\n_____somatorio_de_numero_n_____\n")
    print("n =", n)
    soma = 0
    if n > 0:
        for i in range(n+1):
            soma = soma + i
            print(i,"+ ", end="")
        print("\b\b=",soma)
    elif n < 0:
        print("Somente para numeros positivos!")

#______________________________________________________
def somar_multiplicar(a: int, b: int):
    print("\n_____multiplicacao_somatorios_____\n")
    print("a =", a, "| b =", b)
    somaA = 0
    somaB = 0
    if a > 0:
        for i in range(a+1):
            somaA = somaA + i
    if b > 0:
        for i in range(b+1):
            somaB = somaB + i
    print("\n", somaA, "x", somaB, "=", somaA*somaB)
    if a < 0 or b < 0:
        print("Somente para numeros positivos!")

#______________________________________________________
def verificar(n: int):
    for i in range(n+1):
        resto=n%i
        if resto==0:
            divisiveis+=1
    if n==2 or n==3 or divisiveis<=2:
        return True
    else:
        return False

#______________________________________________________
def verificar2(n: int):
    cont=1
    num=2
    while cont<n:
        if verificar(num):
            print(num)
            cont+=1
        num += 1

#______________________________________________________
def somar_fatoriais(n:int):
    print("\n____SOMA_DOS_FATORIAIS_ATE_N____\n")
    print("n =", n)
    fatorial = 1
    soma = 0
    if n>0:
        for i in range(1,n+1):
            fatorial = fatorial*i
            soma = soma + fatorial
            print(i, "\b! + ", end="")
        print("\b\b=",soma)
    elif n <= 0:
        print("Somente para numeros maiores que 0!")

#______________________________________________________
def imprimir_aleatoriamente(n:int, min: int, max:int):
    random.seed(1)
    for i in range(1,n+1):
        print(random.randint(min, max), end="  ")
    print()

#______________________________________________________
def imprimir_linha(n: int, fill:str, edge:str):
    print(edge, end="")
    for i in range(n-2):
        print(fill, end="")
    print(edge)

#______________________________________________________
def imprimir_caixa(height:int, width:int, fill:str, edge:str):
    print()
    imprimir_linha(width, fill, edge)
    for i in range(height-2):
        imprimir_linha(width, "   ", "|")
    imprimir_linha(width, fill, edge)

#______________________________________________________
def imprimir_maior_menor(n: int, left: int, right: int):
    maior= left
    menor= right

    for i in range(n+1):
        sorteio = random.randint(left, right)
        if sorteio>maior:
            maior=sorteio
        elif sorteio<menor:
            menor=sorteio
    if maior==menor:
        print("os numeros precisam ser diferentes")
    else:
        print(f"min: {menor}, max: {maior}")
        
#______________________________________________________

def main():
    #somar(5)                           #   >>>questao_1
    #somar_multiplicar(3, 4)            #   >>>questao_2
    verificar(123)                      #   >>>questao_3
    #verificar2(7)                      #   >>>questao_4
    #somar_fatoriais(4)                 #   >>>questao_5/questao_6
    #imprimir_aleatoriamente(10, 74, 80)#   >>>questao_7
    #imprimir_linha(5, "=", "o")        #   >>>questao_8
    #imprimir_caixa(10, 12, " = ", "o") #   >>>questao_9
    #imprimir_maior_menor(100, -500, -32)   #   >>>questao_10
    #imprimir_pares_primmos(8, 10, 30)
main()

from math import sqrt
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
    print()

#______________________________________________________
def verificar(n):
    i=n
    divisiveis=0
    while i > 1:
        resto=n%i
        if resto==0:
            divisiveis+=1
        i-=1
    if n==1 or n==2 or divisiveis==1:
        return True
    else:
        return False

#______________________________________________________
def verificar_primeiros_primos(n: int):
    print("\nprimeiros", n, " primos:")
    for i in range(n+1):
        if verificar(i)==True:
            print(i, end="  ")


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
    print()

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
    print()

#______________________________________________________
def imprimir_caixa(height:int, width:int, fill:str, edge:str):
    imprimir_linha(width, fill, edge)
    for i in range(height-2):
        imprimir_linha(width, "   ", "|")
    imprimir_linha(width, fill, edge)
    print()

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
    print()

#______________________________________________________
def imprimir_pares_primos(n: int, left: int, right:int):
    pares=0
    primos=0
    for i in range(n+1):
        sorteio = random.randint(left, right)
        if sorteio%2==0:
            pares+=1
        verificar(sorteio)
        if verificar(sorteio) == True:
            primos+=1
    print(f"pares: {pares}, primos: {primos}")
    print()


#______________________________________________________
def main():
    somar(5)                               #   >>>questao_1
    somar_multiplicar(3, 4)                #   >>>questao_2
    print(verificar(121))                   #   >>>questao_3
    verificar_primeiros_primos(7)                          #   >>>questao_4
    somar_fatoriais(4)                     #   >>>questao_5/questao_6
    imprimir_aleatoriamente(10, 74, 80)    #   >>>questao_7
    imprimir_linha(5, "=", "o")            #   >>>questao_8
    imprimir_caixa(10, 12, " = ", "o")     #   >>>questao_9
    imprimir_maior_menor(100, -500, -32)   #   >>>questao_10
    imprimir_pares_primos(20, 10, 100)      #   >>>questao_11
main()

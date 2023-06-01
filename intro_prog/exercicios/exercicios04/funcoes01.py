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
    divisao=1
    confere=0
    while divisao<n:
        resto=n%divisao
        if resto==0:
            confere+=1
        divisao+=1
    if n==2 or n==3 or confere<2:
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


def main():
    #somar(5)                       #   >>>questao_1
    #somar_multiplicar(3, 4)        #   >>>questao_2
    print(verificar(17))                  #   >>>questao_3
    verificar2(20)                  #   >>>questao_4
main()

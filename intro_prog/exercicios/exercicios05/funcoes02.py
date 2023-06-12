#__________________________________________________________
from glob import escape
from re import I

#_____________________________________________________
def somar(n: int):
    soma = 0
    if n > 0:
        for i in range(n+1):
            soma = soma + i
        return soma
    elif n < 0:
        print("Somente para numeros positivos!")

def imprimir_tab(n):
    print("\n______Tabuada_Completa______\n")
    i=0
    while i<=10:
        print(n, "x", i, "=", n*i)
        i+=1

#__________________________________________________________
def formar_retangulo(m, n):
    print("\n________Retangulo________\n")
    for i in range(m):
        for j in range(n):
            print("[]", end="")
        print()

#__________________________________________________________
def torcer_retangulo(m, n):
    print("\n______Retangulo_Torcido______\n")
    espaco=0
    for i in range(m):
        for j in range(n):
            print("[]", end="")
        espaco+=1
        print()
        for j in range(espaco):
            print("  ", end="")
            
#__________________________________________________________
def torcer_retangulo_2(m, n):
    print("\n______Retangulo_Torcido2______\n")
    espaco= m-1
    for i in range(m):
        for j in range(espaco):
            print("  ", end="")
        for j in range(n):
            print("[]", end="")
        espaco-=1
        print()

#__________________________________________________________
def preencher_retangulo(m, n):
    print("\n______Retangulo_Preenchido______\n")
    for i in range(m):
        print("[", end="")
        for j in range(n):
            print("X", end="")
            if j<n-1:
                print("-", end="")
        print("]")

#__________________________________________________________
def formar_caixa(m,n):
    print("\n_________Caixa_________\n")
    for i in range(m):
        if i==0:
            print("+", end="")
            for j in range(n-2):
                print("-", end="")
            print("+")   

        print("|", end="")
        for j in range(n-2):
            print(" ", end="")
        print("|")

        if i==m-1:
            print("+", end="")
            for j in range(n-2):
                print("-", end="")
            print("+")  

#__________________________________________________________
def formar_triangulo_ret(m:int):
    print("\n_______Triangulo_Retangulo_______\n")
    espaco=0
    for i in range(m):
        if espaco==0:
            for j in range(m):
                print("[]", end="")
        espaco+=1
        print()
        for j in range(espaco):
            print("  ", end="")

        for j in range(m-espaco):
            print("[]", end="")
        
#__________________________________________________________
def formar_floyd(m:int):
    print("\n_______Triangulo_d_Floyd_______\n")

    espaco=m
    cont=0
    for i in range(m):
        espaco=espaco-1
        coluna= m-espaco
        for j in range(coluna):
            cont+=1
            print(cont, end=" ")
        for j in range(espaco):
            print(" ", end=" ")
        print()



#__________________________________________________________
def centralizar_triangulo(m,n):
    print("\n_______Triangulo_Centralizado_______\n")
    n=m*2
    espaco=n
    for i in range(m):
        espaco=espaco-2
        coluna=n-espaco
        for j in range(espaco//2):
            print(" ", end="")
        for j in range(coluna-(coluna//2)):
            print("[]", end="")
        for j in range(espaco//2):
            print(" ", end="")
        print()

#__________________________________________________________
def executar_menu():
    opcao=0
    a=0
    b=0
    i=0
    print("-----------------------------\n SUPREME SUM!    A: 0   B: 0 \n-----------------------------")
    print("1 - Set a\n2 - Set b\n3 - Show a + b\n4 - Show a x b\n5 - Exit")
    while opcao<=5 and i<3:
        opcao = int(input("\nOpcao: "))
        if opcao==5 or opcao<=0:
            break
        if opcao==1:
            a=int(input("\nValor para a: "))
        if opcao==2:
            b=int(input("\nValor para b: "))
        if opcao==3 and (a!=0 or b!=0):
            print("\na + b =", a+b)
        if opcao==4 and (a!=0 or b!=0):
            print("\na x b =", a*b)
        i+=1
#__________________________________________________________
def converter_binario(bin:int):
    potencia=0
    soma=0
    while bin>0:
        dig=bin%10
        bin=bin//10
        soma=soma+(dig*(2**potencia))
        potencia+=1
    print(soma)
        
#__________________________________________________________
def mover_personagem(movimentos:int):
    print("\nTeclas:  A⇦   W⇧   D⇨   S⇩   Q: Exit")
    linhas1= 5
    colunas1=10
    linhas2= 5
    colunas2=10
    i=0
    while i<linhas1+linhas2:
        if i==0:
            print("╔", end="")
            for j in range((colunas1+colunas2)-2):
                print("═", end="")
            print("╗")
            i+=1

        for j in range((linhas1-1)):
            print("║", end="")
            for m in range((colunas1+colunas2)-2):
                print(" ", end="")
            print("║")
            i+=1

        print("║", end="")
        for m in range((colunas1-1)):
            print(" ", end="")
        print("#", end="")
        for m in range((colunas2-2)):
            print(" ", end="")
        print("║")
        i+=1

        for j in range((linhas2-2)):
            print("║", end="")
            for m in range((colunas1+colunas2)-2):
                print(" ", end="")
            print("║")
            i+=1

        print("╚", end="")
        for j in range((colunas1+colunas2)-2):
            print("═", end="")
        print("╝")
        i+=1

        for a in range(movimentos):
            comando= str(input("A= esquerda\nW= cima\nD= direita\nS= baixo\nQ= Exit\nMova para uma direcao de cada vez - "))
            for b in range(len(comando)+1):
                qtdd=b
            
            for b in range(qtdd+1):
                p1="A"
                p2="W"
                p3="D"
                p4="S"

            if comando==p1:
                colunas1-=qtdd
                colunas2+=qtdd

            if comando==p2:
                linhas1-=qtdd
                linhas2+=qtdd
            if comando==p3:
                colunas1+=qtdd
                colunas2-=qtdd
            if comando==p4:
                colunas1+=qtdd
                colunas2-=qtdd

            
        
        
                







#__________________________________________________________
def main():
    #imprimir_tab(12)                       #  >>questao01
    #formar_retangulo(2, 4)                 #  >>questao02
    #torcer_retangulo(3, 4)                 #  >>questao03
    #torcer_retangulo_2(3, 4)               #  >>questao04
    #preencher_retangulo(8, 10)             #  >>questao05
    #formar_caixa(4,12)                     #  >>questao06
    #formar_triangulo_ret(8)                #  >>questao07
    #formar_floyd(7)                        #  >>questao08
    #centralizar_triangulo(20, 2)           #  >>questao09
    #executar_menu()                        #  >>questao10
    #converter_binario(1000)                #  >>questao11
    mover_personagem(2)

main()

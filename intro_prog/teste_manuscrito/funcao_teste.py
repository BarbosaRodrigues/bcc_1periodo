from audioop import mul


def somatorio(m:int):
    soma=0
    for i in range(m+1):
        soma=soma+i
        print(i, " + ", end="")
    print("\b\b=", soma)

def converter_bin(bin:int):
    expoente=0
    soma=0

    while bin>0:
        dig=bin%10
        bin=bin//10
        soma=soma+(dig*(2**expoente))
        expoente+=1
    print(soma)

def executar_menu():
    print("---------------------------\n soma e mult    a:0   b:0 \n---------------------------")
    print("1 - Ler a\n2 - Ler b\n3 - a + b\n4 - a x b\n5 - Exit")

    op=0
    a=0
    b=0


    while op<=5:
        op=int(input("\nopcao: "))

        if op==5 or op<=0:
            break
        if op==1:
            a=int(input("\nvalor para a: "))
        if op==2:
            b=int(input("\nvalor para b: "))
        if op==3:
            soma=a+b
            print("\n",a, "+", b, "=", soma)
        if op==4:
            mult=a*b
            print("\n",a, "x", b, "=", mult)
            

def main():
    somatorio(5)
    converter_bin(111)
    executar_menu()

main()
    
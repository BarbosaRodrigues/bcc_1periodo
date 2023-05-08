#___________________________________________________


print("\n-----Exibe-Primeiro-e-Ultimo-Digito-----\n")

inteiro = int(input("INTEIRO:\n"))
n=inteiro
ultimo = inteiro%10
casas=1
while True:
    if inteiro==0:
        break
    else:
        inteiro=inteiro- (inteiro%10)
        inteiro=inteiro//10
        if inteiro>0 and inteiro//10==0:
            print("PRIMEIRO >",inteiro)
print("ULTIMO >",ultimo)





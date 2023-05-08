#___________________________________________________


print("\n-----Frequencia-dos-Digitos-de-um-Numero-----\n")

num = int(input("informe o numero > "))

while num >0:
    dig=num%10
    num=num//10

    if dig>0 and dig//10==0:
        if  dig==3 or dig==4 or dig>=6 or dig>=9:
            print("FREQUENCIA DE",dig,"> 0")
        if dig==0 or dig==2:
            print("FREQUENCIA DE",dig,"> 1")
        if dig==1:
            print("FREQUENCIA DE",dig,"> 2")
        if dig==5:
            print("FREQUENCIA DE",dig,"> 3")



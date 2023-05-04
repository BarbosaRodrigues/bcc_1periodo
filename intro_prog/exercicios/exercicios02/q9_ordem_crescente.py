#________________________________________________

print("\n-----TRES-NUMEROS-ORDEM-CRESCENTE-----\n")

num1=float(input("informe primeiro numero: "))
num2=float(input("informe segundo numero: "))
num3=float(input("informe terceiro numero: "))

if num1<num2 and num2<=num3:
    print(num1, "  ", num2, "  ", num3)
elif num2<num1 and num1<=num3:
    print(num2, "  ", num1, "  ", num3)
elif num3<num2 and num2<=num1:
    print(num3, "  ", num2, "  ", num1)
elif num3<num1 and num1<=num2:
    print(num3, "  ", num1, "  ", num2)
else:
    print("ERRO!")
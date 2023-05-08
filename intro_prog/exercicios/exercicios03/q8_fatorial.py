#__________________________________________________________

print("\n-------FATORIAL-------\n")

n=int(input("Digite um numero inteiro positivo\n"))
mult=1
if n>0:
    for i in range(1,n+1):
        mult = mult*i
        print(i, "x ", end="")
    print("\b\b= ", mult)
elif n < 0:
    print("Somente para números positivos!")


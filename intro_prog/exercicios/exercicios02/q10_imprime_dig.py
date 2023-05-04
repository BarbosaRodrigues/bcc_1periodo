#________________________________________________

print("\n-----IMPRIMIR-DIGITOS-SEPARADAMENTE-----\n")

entrada=int(input("informe numero inteiro de 5 digitos: "))
u = entrada%10
d= int((entrada%100)-u)//10
c= int((entrada%1000)//100)
um= int((entrada%10000)//1000)
dm= int((entrada%100000)//10000)

print(dm, " - ", um, " - ", c, " - ", d, " - ", u)
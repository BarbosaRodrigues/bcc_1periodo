print('\nmedia aritmetica & ponderada\n')

a = int(input("valor1: "))
b = int(input("valor2: "))
c = int(input("valor3: "))

aritmetica = (a+b+c)/3
converta1 = 10//10
converta2 = 50//10
converta3 = 40//10
peso_a = a*converta1
peso_b = b*converta2
peso_c = c*converta3
ponderada = (a*10+ b*50 + c*40)/(10+50+40)

print("valor:", a ,"- peso:", peso_a,"%\nvalor:", b ,"- peso:", peso_b, "%\nvalor:", c ,"- peso:", peso_c,"%\nmedia aritmetica =", aritmetica, "\nmedia ponderada =", ponderada, "\n")
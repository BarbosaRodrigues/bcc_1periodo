#________________________________________________

from ast import If


print("\n---------CALCULADORA---------\n")

sinal = (input("digite um operador ou\n % para o resto de divisao - "))
n1 = int(input("informe dois inteiros para o calculo\n"))
n2 = int(input())

resultado = 0

if sinal != "+" and sinal != "-" and sinal != "*" and sinal != "/" and sinal != "%":
    print("ERRO, OPERADOR INCORRETO")
else:
    if sinal== "+":
        resultado= n1+n2
    elif sinal== "-":
        resultado= n1-n2
    elif sinal== "*":
        resultado= n1*n2
    elif sinal== "/":
        resultado= n1/n2
    elif sinal== "%":
        resultado= n1%n2
    
    print("__________________________\n")
    print("|   CALCULADORA SIMPLES  |\n")
    print(" ",n1,"",sinal,"",n2,"= %.2f"% resultado,"\n")
    print("__________________________\n")


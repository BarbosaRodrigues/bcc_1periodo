"""
OPERADORES RELACIONAIS
"""

a = 10
b = 3

print("\n a == b? %s", a == b)
print("a == b? %s" % a == b)

# CONDICOES

print("\n-------CONDICOES-------\n")

valor1 = int(input("informe valor 1: "))

if valor1 > 0:
    print("valor 1 - positivo")

if valor1 < 0:
    print("valor 1 - negativo")
else:   #--teste com else--
    print("valor 1 - positivo")
    
if valor1 == 0:
    print("valor 1 - zero")

print("valor 1 = %d" % valor1)

print("\n-------aninhar-------\n")

valor2 = int(input("informe valor 2: "))
valor3 = int(input("informe valor 3: "))

if valor2 == valor3:
    print("\nvalores iguais")
else:
    if valor2 > valor3:
        print("\nmaior: %d" % valor2)
    else:
        print("\nmaior: %d" % valor3)
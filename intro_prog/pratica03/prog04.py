"""
operadores &expressoes aritmeticas
"""

print("OPERADORES E EXPRESSOES")

#

print("\n----------soma------------\n")

a = int(input("digite valor para a: "))
b = int(input("digite valor para b: "))

print("\na + b =", a+b)

soma = a+b

print("\na + b =", soma) 

#

print("\n--------subtracao---------\n")

p = int(input("digite valor para p: "))
q = int(input("digite valor para q: "))

subtracao = p-q

print("\np - q =", subtracao) 

#

print("\n------multiplicacao-------\n")

c = int(input("digite valor para c: "))
k = int(input("digite valor para k: "))

multi = c*k

print("\nc * k =", multi) 

print("\n--divisao-int-real-resto--\n")

e = int(input("digite valor para e: "))
f = int(input("digite valor para f: "))

divReal = e/f
divInt = e//f
resto = e%f



print("\ne / f resultado real =", divReal, "\ne / f resultado inteiro =", divInt, "\nresto da divisao =", resto) 

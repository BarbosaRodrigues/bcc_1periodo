# >> ler 3 numeros A. MAIOR INFORMADO; B. QUANTIDADE DE PARES.

# >> possivel solucao
print()
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
maior = a
pares=0

if b>maior:
    maior = b

if c>maior:
    maior=c

if a%2==0: 
    pares+=1
if b%2==0: 
    pares+=1
if c%2==0: 
    pares+=1

print("maior: ", maior)
print("pares: ", pares)
print()


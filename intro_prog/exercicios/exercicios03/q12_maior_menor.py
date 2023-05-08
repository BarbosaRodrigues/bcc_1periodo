#___________________________________________________

print("------MAIOR-MENOR-DE-VARIOS_NUM------")

n=1
maior=0
menor=0


print("informe os numeros:")
while True:
    n = int(input("> "))

    if n==0:
        break 
    else:
        if n>maior:
            maior=n
        if menor==0:
                menor=maior
        if n<menor:
            menor=n

            

print("maior:", maior)
print("menor:", menor)
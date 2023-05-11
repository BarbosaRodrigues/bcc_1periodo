import random   #modulo

#________________________________________________________________
print("\n-----EXPLORANDO-RANDOM-----\n")

a=random.randint(1,15)   #sorteio

print(a)

#________________________________________________________________
print("\n-----REPETICAO-RANDOM-----\n")

random.seed(3)
for i in range(0,10):
    b=random.random()*5  #sorteio

    print("%.2f, " % b, end='')
print("\n")
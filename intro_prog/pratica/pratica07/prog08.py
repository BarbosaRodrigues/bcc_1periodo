#_______________________________________________________________________

#DESMONTAR INTEIROS
print("\n------DESMONTAR-INTEIROS------")

n2=0
n = int(input("\n>"))

while n>0:
    dig = n%10  #EXTRAI DIG
    n = n//10   #REMOVE 1 DIG
    #print("\n",dig)----RESTO+RESULTADO DA DIVISAO        
    print("%d"% dig, end='')

    n2 = n2*10+dig  #REMONTA O NUMERO AO CONTRARIO
  
print("\b\b")
print("INVERTIDO: %d" % n2)

#_______________________________________________________________________

#VERIFICAR SE E PRIMO
print("\n-------VERIFICAR-PRIMO-------")

valor01 = int(input("\ndigite um inteiro: "))
div = 2

while div<valor01:
    if valor01%div==0:
        break
    div += 1
if div==valor01:
    print("\neste numero e primo")
else:
    print("\nesse numero NAO e primo")

#_______________________________________________________________________

#IMPRIME N IMPARES
print("\n------IMPRIMIR-N-IMPARES------")

valor02 = int(input("\ndigite a quantidade de impares que deseja: "))
i = 1

while i<=valor02:
    if i%2!=0:
        print(i)
    i += 1

#segunda opcao 
print("\n*SEGUNDA OPCAO")
valor02 = int(input("\ndigite a quantidade de impares que deseja: "))
i = 1
IMPAR=1

while i<=valor02:
    print(IMPAR)
    i += 1
    IMPAR +=2

#utilizando for
print("\n*UTILIZANDO FOR")

valor02 = int(input("\ndigite a quantidade de impares que deseja: "))
i=1

for i in range(0,valor02):
    print(i*2+1)
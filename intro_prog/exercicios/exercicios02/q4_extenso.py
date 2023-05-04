#____________________________________________________________________
import string

print("\n------IMPRIME-POR-EXTENSO-0-A-9------\n")

num = int(input("inteiro de 0 a 9: "))
zero = "zero"
um = "um"
dois = "dois"
tres = "tres"
quatro = "quatro"
cinco = "cinco"
seis = "cinco"
sete = "sete"
oito = "oito"
nove = "nove"

if num<0 or num>9:
    print("ERRO: esse nao e um numero de 0 a 9.")
else:
    if num == 0:
        print(num,":",zero)
    if num == 1:
        print(num,":",um)
    if num == 2:
        print(num,":",dois)
    if num == 3:
        print(num,":",tres)
    if num == 4:
        print(num,":",quatro)
    if num == 5:
        print(num,":",cinco)
    if num == 6:
        print(num,":",seis)
    if num == 7:
        print(num,":",sete)
    if num == 8:
        print(num,":",oito)
    if num == 9:
        print(num,":",nove)

    

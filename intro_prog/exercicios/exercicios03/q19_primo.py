print("\n____VERIFICA_SE_E_PRIMO____\n")

valor= int(input("numero: "))
divisao=1
confere=0

while divisao<valor:
    resto=valor%divisao
    if resto!=0:
        confere+=1
    divisao+=1
if valor>=2 and valor<=3 or confere>2:
    print("Resposta: primo")
else:
    print("Resposta: NAO primo")
#___________________________________________________

print("------SOMA-MEDIA-DE-VARIOS_NUM------")

n=1
contador=0
soma=0

print("informe os numeors:")
while n!=0:
    
    n = int(input(">"))
    soma=soma +n
    contador+=1

contador-=1
print("SOMA:", soma)
print("MEDIA:", soma/contador)
def inverter_lista(vet:list):
    max= len(vet)-1
    inverte=[]
    while max>=0:
        inverte.append(vet[max])
        max-=1
    print()
    print(inverte)

def imprimir_pares(vet:list):
    print("\npares: ")
    for i in range(len(vet)):
        if vet[i]%2==0:
            print(vet[i], end="  ")

def inverter_polaridade(vet:list):
    for i in range(len(vet)):
        if vet[i]<0:
            vet[i]=vet[i]*-1
    print()
    print(vet)

def calcular_media(vet:list):
    total=0
    for i in range(len(vet)):
        total= vet[i]+total

    media=total/len(vet)
    print("\nMEDIA: ", media)


def main():
    inverter_lista([3,1,10,40])
    imprimir_pares([3,1,10,40])
    inverter_polaridade([3, -23, -4, 10, -9])
    calcular_media([9, 10, 8.5, 7.7])
main()
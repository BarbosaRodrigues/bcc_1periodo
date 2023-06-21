def verificar(n):
    i=n
    divisiveis=0
    while i > 1:
        resto=n%i
        if resto==0:
            divisiveis+=1
        i-=1
    if n==1 or n==2 or divisiveis==1:
        return True
    else:
        return False

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

def buscar_elem(vet:list, elem):
    j=0
    for i in range(len(vet)):
        if vet[i]==elem:
            print("\n",elem, "na posicao: ", i)
            j+=1
    if j==0:
        return None

def buscar_crescente(vet:list, elem):
    j=0
    for i in range(len(vet)):
        if vet[i]==elem:
            print("\n",elem, "na posicao: ", i)
            j+=1
            break
    if j==0:
        return None
    
def achar_multiplo(vet:list, value):
    print("\nMULTIPLOS DE", value, ":")
    for i in range(len(vet)):
        if vet[i]%value==0:
            print(vet[i])

def listar_com_primos(vet:list):
    print("\nPrimos da lista:\n")
    primos=[]
    a=1

    for i in range(len(vet)):
        verificar(vet[i])
        if verificar(vet[i])==True:
            primos.append(vet[i])
        

    print(primos) 

def verificar_ordem(vet:list):
    for i in range(1,len(vet)):
        if vet[i]>vet[i-1]:
            return True
        else:
            return False
            break
            
  
def main():
    inverter_lista([3,1,10,40])
    imprimir_pares([3,1,10,40])
    inverter_polaridade([3, -23, -4, 10, -9])
    calcular_media([9, 10, 8.5, 7.7])
    buscar_elem(["joao", 34, 9999, "m", "a", "h"], "m")
    buscar_crescente(["joao", 34, 9999, "m", "a", "h"], "h")
    achar_multiplo([20, 23, 45, 60, 88, 168, 169], 3)
    listar_com_primos([2,3,4,5, 10, 13])
    print(verificar_ordem([2, 3 , 10, 4, 1,6,7]))
main()
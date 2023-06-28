#___________________________________________________________________
def sequencia(vet:list):    #>>>CONTA OS REPETIDOS MAS NAO SEQUENCIA
    m=0
    soma=0
    soma2=0

    for i in range(len(vet)):
        for j in range(1, len(vet)):
            if vet[i]==vet[j]:
                soma2+=1
        if soma2>soma:
            soma=soma2
            m=vet[i]
        soma2=0
    return m


#___________________________________________________________________
def check(vet:list):   
    i=0

    if len(vet)>1 and vet[0]%2==1:
        return False
    
    else:
        while i < len(vet):
            if vet[i]%2==0:
                return True
            else:
                break
            i+=1

        while i < len(vet):
            if vet[i]%2==1:
                return True
            else:
                return False
                break
            i+=1
        if vet==[] or len(vet)==1:
            return True

def main():
    print(sequencia([1,1,2,3,9,6,8,5]))
    print(check([2,6,88,5,67]))

main()
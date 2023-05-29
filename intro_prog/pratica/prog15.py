def print_idx(v: list, elem: int):
    for i in range(len(v)):
        if v[i]== elem:
            print(i, end=" ")
    print()

def main():
    #________ACESSANDO_ELEMENTOS_DE_LISTA_________
    
    v=[10,20,80,90]
    
    print()
    print(len(v), "\n")      #4
    print( v[0])


    #________TRY_EXCEPT_________
    print()

    v2=[8, 9, 11, 55, 77, 65, 33]

    idx=8
    try:
        print(f"v2[{idx}] = {v2[idx]}")    
    except:
        print(f"Indice {idx} invalido") 

    #__________VARREDURA_REVERSA_____________
    print()

    words = ["filho", "tefefone", "tarefa", "hello", "Aparecida"]
    i = len(words)-1

    while i>=0:
        print(words[i], end="  ")
        i-=1
    print("\b\b")

    #_________INDICES_DE_UM_ELEMENTO_____________

    print()
    print_idx([10, 15, 30, 30, 30, 40], 30)   
main()  




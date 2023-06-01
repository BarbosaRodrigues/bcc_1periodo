from os import remove
import random as rand

def remover_todos(v):
    while len(v)>0:
        v.pop()    #remover

def guardar_maior_valor(v):
    if len(v)==0:
        return None
    maior= -float('inf')
    #maior=v[0]
    for e in v:
        if e > maior:
            maior=e
    return maior


def modificar():
    list1 = [1, 2, 3]
    print()
    print(list1)
    list1.append(10)
    print(list1)
    print()

    v1=[]

    for i in range(10):
        v1.append(i+1)  #adiciona
    print()
    print(v1)
    remover_todos(v1)

    for i in range(10):
        v1.insert(0, (i+1)*5)   #adiciona direcionando a um indice
    print()
    print(v1)
    remover_todos(v1)

    for i in range(10):
        v1.append(rand.randrange(1, 11))    #a ate b-1

    print()
    print(v1)

    print(guardar_maior_valor(v1))

def main():
    modificar()
main()
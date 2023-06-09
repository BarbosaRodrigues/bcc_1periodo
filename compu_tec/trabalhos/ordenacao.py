from random import randint
from timeit import repeat


REPETICOES = 3
EXECUCOES = 1


def executa_algoritmo(algoritmo, lista):
    # Prepara a chamada do algoritmo
    # importa o algoritmo, caso não for o builtin do python
    if algoritmo != "sorted":
        setup_code = f"from __main__ import {algoritmo}"
    else:
        setup_code = ""

    stmt = f"{algoritmo}({lista})"

    # executa o algoritmo um total de *EXECUCOES* vezes e  retorna o tempo de todas as execuções
    # repete o processo por REPETICOES vezes
    tempos = repeat(setup=setup_code, stmt=stmt,
                    repeat=REPETICOES, number=EXECUCOES)

    # Mostra o menor tempo de execução entre as REPETICOES
    print(f"Algoritmo: {algoritmo}. Menor tempo de execução: {min(tempos)}")


def bubble_sort(lista):

    n = len(lista)

    for i in range(n):
        ordenado = True
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # atenção nessa atribuiçao, ela faz a troca
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                ordenado = False
        if ordenado:
            break
    return lista


def insertion_sort(lista):

    for i in range(1, len(lista)):

        item_chave = lista[i]

        j = i - 1

        while j >= 0 and lista[j] > item_chave:

            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = item_chave

    return lista

def selection_sort(lista):
    if not lista:
        return lista
    for i in range(len(lista)):
        min_i = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        left = [x for x in lista[1:] if x < pivot]
        right = [x for x in lista[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

#tamanhos= [5, 10, 100, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000, 300000, 400000, 500000, 
#       600000, 700000, 800000, 900000, 1000000, 5000000, 10000000]
#for i in tamanhos:
LISTA_LENGTH = 100

if __name__ == "__main__":

    # Gera uma lista de tamanho `LISTA_LENGTH`
    # contendo inteiros aleatórios entre0 and 999
    lista = [randint(0, 1000) for i in range(LISTA_LENGTH)]

    # Chama a função pra medir desempenho usando a lista que acabados de criar e o nome do algoritmo que queremos testar
    # atenção, o algoritmo deve ser uma funcao que opera uma lista de inteiros

    # passamos lista[:] para termos uma cópia de lista e evitar que ela seja modificada

    #execucao dos algoritmos

    executa_algoritmo(algoritmo="sorted", lista=lista[:])

    executa_algoritmo(algoritmo="merge_sort", lista=lista[:])

    executa_algoritmo(algoritmo="selection_sort", lista=lista[:])

    executa_algoritmo(algoritmo="insertion_sort", lista=lista[:])

    executa_algoritmo(algoritmo="bubble_sort", lista=lista[:])

def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    # para uma versão com partição aleatória
    # descomente as próximas três linhas:
    # from random import randrange
    # rand = randrange(ini, fim)
    # a[rand], a[fim - 1] = a[fim - 1], a[rand]
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] <= pivo:
            a[i], a[ini] = a[ini], a[i]
            ini += 1

    return ini - 1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(a)
print(quick_sort(a))

executa_algoritmo(algoritmo="quick_sort", lista=lista[:])

    

    

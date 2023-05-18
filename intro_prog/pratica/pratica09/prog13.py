#____________loops__aninhados______________________________

def rotular():
    print("\n___LOOPS_ANINHADOS___\n")
    print("--------SAIDA-X-por-Y--------\n")

def desenhar_box1(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print('♂ ♀ ', end="")
        print()

rotular()
desenhar_box1(4,2)

#__________________________________________________________

def rotular2():
    print("\n-------SAIDA-CRESCENTE-------\n")

def decrescer(lins):
    for i in range(1, lins+1):
        for j in range(i):
            print("X", end='')
        print()

rotular2()
decrescer(3)
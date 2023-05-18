#____________loops__aninhados______________________________

def rotular():
    print("\n___LOOPS_ANINHADOS___\n")
    print("--------IMPRIMINDO-A-CADA-INTERACAO--------\n")

def aninhar_loops1():
    for i in range(3):
        print("for_i %d"%i)

        for j in range(4):
            print(" for_j %d"%j)


rotular()
aninhar_loops1()
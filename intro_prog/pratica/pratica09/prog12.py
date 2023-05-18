
#____________loops__aninhados______________________________

def rotular():
    print("\n___LOOPS_ANINHADOS___\n")
    print("--------SOMA-MULTIPLICACAO--------\n")

def loops1():
    count = 0
    for i in range(2):
        for j in range(5):
            count += 1
    print("Count: %d" % count)
def loops2():
    count = 0
    for i in range(2):
        for j in range(5):
            count += 1
        count *= 2
    print("Count: %d" % count)

rotular()
loops1()
loops2()
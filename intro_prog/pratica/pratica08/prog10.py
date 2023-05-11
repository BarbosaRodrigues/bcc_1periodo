#__________________________________________________________
print("\n-------PRIMEIRA-FUNCAO-------\n")

def say_hello():
    pass    #-----CONDICAO SEM CODIGO

say_hello()  #----EXECUTANDO

#__________________________________________________________
print("\n-----PRIMEIRO-CONTEUDO-NA-FUNCAO-----")

def say_hello():
    print("_____________________")
    print("_____HELLO_WORLD_____")
    print("_____________________")


say_hello() 

#__________________________________________________________
print("\n-------FUNCAO-SOMAR-------\n")

#def somar(a, b):
#    print("%d"%a, "+ ","%d"%b, end="")
#    res=a+b
#    print(" =",res, "\n")
#    return

#somar(10,13) 
#x=50
#y=2 
#somar(x, y)

def somar(a: float, b: float, c: float):
    res=a+b+c
    return res

def imprimir_soma(x, y, z):
    retorno=somar(x, y, z)
    print(f'Resultado: {retorno}')
    

def main():
    imprimir_soma(4,29,6)
    print('fim.\n')

main()

#if __name__ == "__main__":
#   main()
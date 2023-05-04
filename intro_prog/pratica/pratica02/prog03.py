'''
    tipos & variáveis
'''

print("\n\nimprimindo tipos\n\n")

print("int:", 5)
print("float:", 5.3434)
print("bool:", True)

print('tipos: ')
print(type(5))
print(type(5.3434))
print(type(True))

print("\n\ndefinindo variaveis\n\n")

num = 13
name = "talita"
total = 15.1523
check = True

print('numero:', num)
print('nome:', name)
print('total:', total)
print('check:', check)

print("\n\nvariaveis & casting\n\n")

txt = "23.11"
a = float(txt)
b = int(float(txt))

print(txt)
print(a)
print(b)

print(type(txt))
print(type(a))
print(type(b))

print("\n\nentrada de valores\n\n")

x = input('informe um valor int: ')
print('lendo:',x)

nome = input('\nnome: ')
idade = int(input('idade: '))
altura = float(input('altura: '))
print("\nlendo suas informacoes: ")
print('    nome:',nome, '\n    idade: ', idade, '\n    altura: ', altura)


nome = input('\nnome: ')
idade = int(input('idade: '))
altura = float(input('altura: '))
print("\nlendo suas informacoes: ")
print("    nome: %s, \n    idade: %d, \n    altura: %f" % (nome, idade, altura))

nome = input('\nnome: ')
idade = int(input('idade: '))
altura = float(input('altura: '))
print("\nlendo suas informacoes: ")
print(f"   nome: {nome} \n  idade: {idade} \n   altura: {altura}")

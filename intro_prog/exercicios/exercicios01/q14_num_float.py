print('\nprecisao, inteiro & decimal\n')

a = float(input("valor: "))
inteiro = int(a//1)
decimal = a-inteiro

print("\no numero com 2 casa de precisao: %.2f"%(a), "\nparte inteira:", inteiro, "\nparte decimal:", decimal,"\n")
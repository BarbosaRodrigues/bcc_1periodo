#__________________________________________________________

print("\n------SOMATORIO------\n")

n=int(input("Digite um número positivo e inteiro: "))
soma = 0
if n > 0:
  for i in range(n+1):
    soma = soma + i
    print(i,"+ ", end="")
  print("\b\b=",soma)
elif n < 0:
  print("Somente para números positivos!")

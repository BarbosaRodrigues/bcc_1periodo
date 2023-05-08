#___________________________________________________

print("\n-------SERIAL-DE-PRODUTO-------\n")

num = int(input("numero serial + verificador:\n"))
soma=0
verificador = num%10
num_serial= num-verificador
dezena = num_serial%100
ultimo = dezena//10

while num_serial>0:
    d= num_serial%10
    num_serial=num_serial//10
    soma=soma+d

resto = soma%10

if verificador>ultimo or resto<ultimo:
    print("\nultimo digito do serial e DESIGUAL ao verificador\n")
else:
    print("ultimo digito do serial e IGUAL ao verificador")

print("Soma dos numeros seriais -",soma,".Verificador -",verificador,"\n")
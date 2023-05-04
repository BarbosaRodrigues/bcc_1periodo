#____________________________________________________________________
print("\n-------ANO-BISSEXTO-------\n")

val = int(input("ANO: "))

if val%4==0 and val%100!=0:
    print(val,"= ano bissexto")
else:
    print(val,"= ano comum\n")
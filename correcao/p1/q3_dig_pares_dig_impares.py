# >> DESMONTAR NUMERO EXTRAINDO SEUS DIGITOS
# >> QTDD PARES E PERCENTTUAL EM RELACAO A QTDD DE DIGITOS
# >> QTDD IMPARES E PERCENTTUAL EM RELACAO A QTDD DE DIGITOS

p=0
imp=0
count=0
n= int(input("\ninforme inteiro positivo:\n"))

if n<0:
    print("ERRO: negativo")
else:
    while n>0 :
        d =n%10
        n = n//10
        if d!=0:
            if d%2==0:
                p+=1
            else:
                imp+=1
        count+=1
    if count==0:
        print("informe numero maior que 0")
    else:
        print("pares: ", p,"___", p/count*100)
        print("impares: ", imp,"___", imp/count*100)
        print()
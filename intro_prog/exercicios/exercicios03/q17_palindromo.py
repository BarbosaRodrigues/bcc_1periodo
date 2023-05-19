#___________________________________________________


print("\n-----Palindromo-ou-nao-----\n")

num = int(input("informe o numero > "))
reserv=num
comparacao=num
invert=0
i=0

while num >=10:
    num=num//10
    i+=1

k= reserv//10**i

while i>=1:
    dig=reserv%10
    reserv= reserv//10
    j=10**i
    invert=invert+(dig*j)
    i-=1

invert=invert+k

if invert==comparacao:
    print("\n", "voce digitou", comparacao, "Invertido fica:", invert, "\n")
    print( "PALINDROMO", "\n")
else:
    print("\n", "voce digitou", comparacao, "Invertido fica:", invert, "\n")
    print( "NAO PALINDROMO", "\n")


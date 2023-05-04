#________________________________________________

print("\n-----PASSAR-LETRA-P-MAIUSCULA-----\n")

char = str(input("digite um caracter - "))

if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
    if ord(char)>=97 and ord(char)<=122:
        print(chr(ord(char)-32))
    else:
        print(char)
else:
    print("\n", char, "- NAO letra\n")
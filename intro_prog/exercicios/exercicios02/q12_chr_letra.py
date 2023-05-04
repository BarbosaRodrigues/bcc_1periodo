#________________________________________________

print("\n-----SABER-SE-CHR-E-LETRA-----\n")

char = str(input("digite um caracter - "))

if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
    print("\n", char, "- letra\n")

else:
    print("\n", char, "- NAO letra\n")
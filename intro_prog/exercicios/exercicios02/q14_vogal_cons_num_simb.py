#________________________________________________

print("\n-----VOGAL-OR-CONSOANTE-OR-NUMERO-OR-SIMBOLO-----\n")

char = str(input("digite um caracter - "))

if ord(char)>=33 and ord(char)<=47 or ord(char)>=58 and ord(char)<=64 or ord(char)>=91 and ord(char)<=96 or ord(char)>=123 and ord(char)<=126:
    print(char,"- is a symbol\n")
elif ord(char)>=48 and ord(char)<=57:
    print(char, "- is a number\n")
else:
    if ord (char)==65 or ord (char)==65+32 or ord (char)==69 or ord (char)==69+32 or ord (char)==73 or ord (char)==73+32 or  ord (char)==79 or ord (char)==79+32 or  ord (char)==85 or  ord (char)==85+32:
        print(char, "- is a vowel")
    elif ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
        print("\n", char, "- LETTER! NOT is a vowel\n")
    else: 
        print("ERRO: not's letter, not's symbol and not's number\n")

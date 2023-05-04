from ctypes.wintypes import FLOAT

print("\n-----MEDIA-CONCEITO-DO-ALUNO-----\n")

val1 = float(input("primeira nota de 0 a 10: "))
val2 = float(input("segunda nota de 0 a 10: "))
val3 = float(input("terceira nota de 0 a 10: "))
media = float(val1+val2+val3)/3

if(media>=8.5 and media<=10): 
    print("Conceito A - media %.3f"% media)
if(media>=7.0 and media<8.5): 
    print("Conceito B - media %.3f"% media)
if(media>=5.5 and media<7.0): 
    print("Conceito C - media %.3f"% media)
if(media>=0 and media<5.5): 
    print("Conceito F - media %.3f"% media,"\n")



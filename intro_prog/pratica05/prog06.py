
print('\n----condicionais----')
print('\nDe um valor para\n')
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if a>=b and a>c:
    print("maior: %d"%a)
else:
    if b>=c:
        print("maior: %d"%b)
    else:
        print("maior: %d"%c)

#INTERVALO

print("\n----intervalos----")
print("\nvalor para z")
z=int(input("\nz:"))

#if z>=50 and z<=100:
#   print("no intervalo")

if(z>=-100 and z<=-50) or (z>=50 and z<=100):  # if false or true
    print("no intervalo")

print("\n----intervalos----")

print("\n----chr----\n")

print(ord ("A"))
print(chr (65))

print("\nano, semanas & dias\n")

dias= int(input("informe quantos dias: "))

anos = dias//365
restante_dias = dias - (365*anos)
semanas = restante_dias//7
restante_dias = restante_dias - (7*semanas)

print("\nDIAS:", dias, "=\n", anos, "ano(s)," , semanas, "semanas e", restante_dias, "dias", "\n")
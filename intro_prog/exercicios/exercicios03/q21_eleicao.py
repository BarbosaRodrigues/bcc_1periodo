
print("\n_____SEQUENCIA_DE_VOTOS_____\n")

c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0
eleitores = 15

while eleitores >0:
    if eleitores==30:
        voto=0
    else:
        voto= int(input("Vote 1 para candidato 1\nVote 2 para candidato 2\nVote 3 para candidato 3\nVote 4 para candidato 4\nVote 5 para anular\nVote 6 para votar em branco\nSEU VOTO: "))
 
        if voto==1:
            c1=c1+1
        if voto==2:
            c2=c2+1
        if voto==3:
            c3=c3+1
        if voto==4:
            c4=c4+1
        if voto==5:
            nulo=nulo+1
        if voto==6:
            branco=branco+1
    eleitores-=1

print("\nCandidato 1:", c1, "voto(s)")
print("Candidato 2:", c2, "voto(s)")
print("Candidato 3:", c3, "voto(s)")
print("Candidato 4:", c4, "voto(s)")
print("Nulos:", nulo, "voto(s)")
print("Brancos:", branco, "voto(s)\n")

if c1>c2 and c1>c3 and c1>c4:
    c1=c1+branco
    print("Mais votado candidato 1:", c1, "votos\n")

if c2>c1 and c2>c3 and c2>c4:
    c2=c2+branco
    print("Mais votado candidato 2:", c2, "votos\n")

if c3>c2 and c3>c1 and c3>c4:
    c3=c3+branco
    print("Mais votado candidato 3:", c3, "votos\n")

if c4>c2 and c4>c3 and c4>c1:
    c4=c4+branco
    print("Mais votado candidato 4:", c4, "votos\n")


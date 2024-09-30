totalNotas = 0
cont = 0
while True:
    nota = float(input("Informe uma nota: "))
    
    if nota == 0:
        break
    else:
        print(nota)
        totalNotas += nota
        cont += 1

if totalNotas == 0:
    print("Você não inseriu notas")
else:
    media = totalNotas/cont
    print(f"A média aritimética das notas inseridas é {media}")
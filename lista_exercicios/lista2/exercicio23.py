time1 = input("Informe o primeiro time: ")
gol1 = int(input(f"Informe a quantidade de gols do {time1}: "))
time2 = input("Informe o segundo time: ")
gol2 = int(input(f"Informe a quantidade de gols do {time2}: "))

if gol1>gol2:
    print(f"\n{time1} marcou {gol1} gol(s) e venceu a partida!")
elif gol2>gol1:
    print(f"\n{time2} marcou {gol2} gol(s) e venceu a partida!")
else:
    print(f"\nAs equipes empataram em {gol1} X {gol2}")
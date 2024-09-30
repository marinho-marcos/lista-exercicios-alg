cont = 0
while True:
    num = int(input("Informe um numero inteiro qualquer: "))
    if num < 0:
        break
    else:
        print(num)
        cont += 1

if cont == 0:
    print("Não foram informados numeros inteiros")
else:
    print(f"Forem digitados {cont} números inteiros")
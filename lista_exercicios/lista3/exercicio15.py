soma = 0
cont = 0
while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    elif num%3 == 0:
        print(num)
        soma += num
        cont += 1
    else:
        print(num)

if soma > 0:        
    media = soma/cont
    print(f"A média aritimética dos divisiveis por 3 inseridos é: {media}")
else:
    print("não foram inseridos divisiveis por 3")
num = int(input("Informe um numero para verificar se ele é primo: "))
ehPrimo = True

for x in range(2,num):
    if num%x == 0:
        ehPrimo = False
        print(f'{num} não é primo, pois ele também é divisivel por {x}')
        break
    else:
        ehPrimo = True
if ehPrimo:
    print(f"{num} é primo!")
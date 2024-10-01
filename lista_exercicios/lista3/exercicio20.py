ehPrimo = True
for x in range(2,121):
    if 121%x == 0:
        ehPrimo = False
        print(f'121 não é primo, pois ele também é divisivel por {x}')
        break
    else:
        ehPrimo = True
if ehPrimo:
    print("121 é primo")
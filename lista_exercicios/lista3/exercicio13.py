num = int(input("Informe um número inteiro: "))
if num > 0:
    for x in range(num, -1, -1):
        print(x)
elif num < 0:
    for x in range(num, 1, 1):
        print(x)
else:
    print(num)  
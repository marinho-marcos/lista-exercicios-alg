soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    else:
        print(num)
        soma += num

print(f"A soma dos números informados é: {soma}")
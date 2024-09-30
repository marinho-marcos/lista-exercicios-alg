frances = 0.12
doce = 1.50
qntd_fra = int(input("Digite a quantidade de pão francês vendido hoje: "))
qntd_doce = int(input("Digite a quantidade de pão doce vendido hoje: "))

total = (qntd_fra*frances) + (qntd_doce*doce)
poupanca = (total*0.10)

print(f"\nO total da venda dos pães foi de R$ {total}, e você deve guardar na poupança o valor de R$ {poupanca:.2f}.")

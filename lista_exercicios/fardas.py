p = int(input("Digite a quantidade de camisas tamanho P vendidas: "))
m = int(input("Digite a quantidade de camisas tamanho M vendidas: "))
g = int(input("Digite a quantidade de camisas tamanho G vendidas: "))

qntd_p = p*10
qntd_m = m*12
qntd_g = g*15
total = float(qntd_p + qntd_m + qntd_g)

print(f"\nO valor total arrecadado com as vendas será de R$ {total}")
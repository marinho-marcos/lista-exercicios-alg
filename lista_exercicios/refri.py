#MOD0 1: ARMAZENANDO PREVIAMENTE A CONVERSAO
produto1 = 350/1000
produto2 = 600/1000         
produto3 = 2

venda1 = int(input("Informe a quantidade de unidades do 350 ml foram compradas: "))
venda2 = int(input("Informe a quantidade de unidades do 600 ml foram compradas: "))
venda3 = int(input("Informe a quantidade de unidades do 2l foram compradas: "))

total = (venda1*produto1) + (venda2*produto2) + (venda3*produto3)

print(f"\nO comerciante comprou um total de {total} litros.")

#MODO 2: SOLICITANDO OS DADOS E REALIZANDO A CONVERSAO DEPOIS

# modelo_1 = int(input("Informe a quantidade de unidades do 350 ml foram compradas: "))
# modelo_2 = int(input("Informe a quantidade de unidades do 600 ml foram compradas: "))
# modelo_3 = int(input("Informe a quantidade de unidades do 2l foram compradas: "))

# qntd_total = (modelo_1*350/1000) + (modelo_2*600/1000) + modelo_3*2

#print(f"\nO comerciante comprou um total de {qntd_total} litros.")
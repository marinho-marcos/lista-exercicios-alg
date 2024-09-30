qntd = int(input("Informe a quantidade laranjas compradas: "))

if qntd < 12:
    total = qntd*1.30
    print(f"O toal da compra foi de R$ {total}")
else:
    total = qntd*1
    print(f"O total da compra foi de R${total}")
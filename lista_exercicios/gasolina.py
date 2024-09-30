preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor = float(input("Digite o valor que deseja colocar de gasolina: "))
compra = valor/preco_litro

print(f"\nCom o valor de R$ {valor} você vai conseguir comprar {compra:.2f} litro(s).")
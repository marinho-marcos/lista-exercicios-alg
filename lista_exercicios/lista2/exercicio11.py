idade = int(input("Informe a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria Juvenil B")
elif idade > 18 and idade <= 120:
    print("Categoria Adulto")
else:
    print("Não participa da competição")
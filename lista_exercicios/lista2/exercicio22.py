ano_atual = 2024
idade = int(input("Informe o seu ano de nascimento: "))
vota = ano_atual-idade

if vota >= 16:
    print("Você poderá votar este ano")
else:
    print("Você não poderá votar este ano")
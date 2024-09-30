salario = float(input("Digite o valor do seu salário: "))
porcentagem = salario*0.20
prest = float(input("Digite o valor da sua prestação: "))

if prest > porcentagem:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")
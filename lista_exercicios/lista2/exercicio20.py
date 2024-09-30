valor_hora = float(input("Informe o valor da sua hora: "))
horas = int(input("Agora informe quantas horas você trabalhou no mês: "))
salario_bruto = horas*valor_hora
inss = salario_bruto*0.10
fgts = salario_bruto*0.11

if salario_bruto <= 900:
    ir = 0
elif salario_bruto>900 and salario_bruto<=1500:
    ir = salario_bruto*0.05
elif salario_bruto>1500 and salario_bruto<=2500:
    ir = salario_bruto*0.10
elif salario_bruto>2500:
    ir = salario_bruto*0.20

liquido = salario_bruto-ir-inss
total_desc = ir+inss

print("\n*** FOLHA DE PAGAMENTO ***")
print("-----------------------------")
print(f"SALÁRIO BRUTO --> {salario_bruto}")
# if ir==0:
#     print(f"IR --> ISENTO")
# else:
#     print(f"IR --> {ir}")
print(f"IR --> {ir}")
print(f"INSS --> {inss}")
print(f"FGTS --> {fgts}")
print(f"TOTAL DE DESCONTOS --> {total_desc}")
print(f"SALÁRIO LIQUIDO --> {liquido}")
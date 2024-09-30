num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if (num1%1==0 and num2%1==0 and num3%1==0) and (num1>0 and num2>0 and num3>0):
    print("\nOs números são todos do tipo inteiro e positivos\n")
else:
    print("\nOs números NÃO são todos do tipo inteiro e positivos\n")

if num1%1==0 and num1>0:
    print(f"{num1} é inteiro e positivo")
else:
    print(f"{num1} não é inteiro e positivo")

if num2%1==0 and num2>0:
    print(f"{num2} é inteiro e positivo")
else:
    print(f"{num2} não é inteiro e positivo")

if num3%1==0 and num3>0:
    print(f"{num3} é inteiro e positivo")
else:
    print(f"{num3} não é inteiro e positivo")
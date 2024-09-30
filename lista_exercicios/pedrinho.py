moeda1 = int(input("Informe a quantidade de moedas de 1 centavo que você depositou: "))
moeda5 = int(input("Informe a quantidade de moedas de 5 centavo que você depositou: "))
moeda10 = int(input("Informe a quantidade de moedas de 10 centavo que você depositou: "))
moeda25 = int(input("Informe a quantidade de moedas de 25 centavo que você depositou: "))
moeda50 = int(input("Informe a quantidade de moedas de 50 centavo que você depositou: "))
moeda1real = int(input("Informe a quantidade de moedas de 1 real que você depositou: "))

total = (moeda1*0.01)+(moeda5*0.05)+(moeda10*0.10)+(moeda25*0.25)+(moeda50*0.50)+(moeda1real*1)

print(f"\nO total em reais economizados por pedrinho foi de R$ {total}")
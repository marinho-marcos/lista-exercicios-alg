peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso/(altura**2)

abaixo = "Você está abaixo do peso ideal"
normal = "Parabéns — você está em seu peso normal!"
sobrepeso = "Você está acima de seu peso (sobrepeso)"
grau1 = "Obesidade grau I"
grau2 = "Obesidade grau II"
grau3 = "Obesidade grau III"

print(f"\nO seu IMC é {imc}\n")

if imc < 18.5:
    print(abaixo)
elif imc >= 18.5 and imc <= 24.9:
    print(normal)
elif imc >= 25 and imc <= 29.9:
    print(sobrepeso)
elif imc >= 30 and imc <= 34.9:
    print(grau1)
elif imc >= 35 and imc <= 39.9:
    print(grau2)
else:
    print(grau3)
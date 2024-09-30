nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

if (nota1<=0 or nota2<=0 or nota3<=0) or (nota1>=100 or nota2>=100 or nota3>=100):
    print("\nAlguma das notas que você digitou é inválida")
else:
    media = (nota1+nota2+nota3)/3
    print(f"\nA sua média é {media:.2f}\n")

    if media < 40:
        print("REPROVADO!")
    elif media >= 40 and media <= 70:
        print("EM RECUPERAÇÃO")
    else:
        print("APROVADO!")
ano = int(input("Digite o ano a ser verificado: "))

if ano%400==0 or ano%4==0 and ano%100!=0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")
qntdOi = 0
while True:
    palavra = input("Informe uma palavra qualquer ou SAIR para encerrar: ")
    if palavra == "sair":
        break
    elif palavra == "oi":
        print(palavra)
        qntdOi += 1
    else:
        print(palavra)

print(f"\nPrograma encerrado. E a palavra Oi foi digitada {qntdOi} vezes.")
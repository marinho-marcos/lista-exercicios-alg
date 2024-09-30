palavras = []
while True:
    palavra = input("Informe uma palavra qualquer ou deixea resposta em branco para encerrar: ")
    if palavra == "":
        break
    else:
        print(palavra)
        palavras.append(palavra)

if palavras:
    menorPalavra = min(palavras, key=len)
    maiorPalavra = max(palavras, key=len)
    
    print(f"A maior palavra é: {maiorPalavra}")
    print(f"A menor palavra é: {menorPalavra}")
else:
    print("Você não inseriu palavras")
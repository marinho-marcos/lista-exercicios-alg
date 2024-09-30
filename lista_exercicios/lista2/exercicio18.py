turno = input("Informe o turno em que você estuda (digite M para matutino, V para vespertino e N para noturno): ").lower()

if turno=="m":
    print("Bom dia!")
elif turno=="v":
    print("Boa tarde!")
elif turno=="n":
    print("Boa noite!")
else:
    print("Opção inválida!")
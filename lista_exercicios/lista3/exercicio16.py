divisiveis = []
cont = 0
for x in range(1000,2000):
    if x%3==0 and x%5==0 and x%10!=0:
        print(x)
        divisiveis.append(x) 
        cont += 1
media = sum(divisiveis)/cont
print(f"A média dos números divisiveis por 3 e 5 mas não divisveis por 10 entre 1000 e 2000 é {media}")
cont = 0
num = int(input("Informe um número: "))
for x in range(1,num+1):
    if num%x == 0:
        cont += 1
print(f"a quantidade de divisores é {cont}")
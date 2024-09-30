queijo = 50.0*2
presunto = 50.0
carne = 100

qntd = int(input("Informe a quantidade de sandíchues que deseja fazer: "))
print("\nVOCÊ PRECISARÁ DE:")
print("--------------------------")
print(f"{qntd*queijo/1000} quilo(s) de queijo.")
print(f"{qntd*presunto/1000} quilo(s) de presunto.")
print(f"{qntd*carne/1000} quilo(s) de carne de hamburguer.")
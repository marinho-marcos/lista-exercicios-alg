# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para ler os números até que o usuário digite 0
while True:
    # Solicita ao usuário que informe um número
    numero = int(input("Digite um número (ou 0 para finalizar): "))
    
    # Verifica se o número é 0, se sim, encerra o loop
    if numero == 0:
        break
    
    # Adiciona o número à lista
    numeros.append(numero)

# Calcula a soma dos números na lista
soma = sum(numeros)

# Exibe o resultado da soma dos números informados
print("A soma dos números informados é:", soma)
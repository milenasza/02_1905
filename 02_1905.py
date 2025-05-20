# listas
numeros = []
separados = []
pares = []
impares = []

# ponto de partida para operações seguintes
soma_separados = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_separados = 0

# coleta de dados
for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
        quantidade_pares += 1
    
    else: 
        impares.append(num)
        quantidade_impares += 1
    
    if num >= 10 and num <= 50:
        separados.append(num)
        quantidade_separados += 1
        soma_separados += num
    
# cálculo da média dos números entre 10 a 50
if quantidade_separados > 0:
    media = soma_separados / quantidade_separados
else:
    media = 0

# maior número ímpar digitado
maior_impar = max(impares)

# saída
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"A média dos números entre 10 e 50 é de: {media}")
print(f"O maior número ímpar digitado é: {maior_impar}")
print(f"Números digitados: {sorted(numeros)}")

        

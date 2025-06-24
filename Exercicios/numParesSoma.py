# Peça ao usuário para digitar um número inteiro positivo.
# Use um for para percorrer de 1 até esse número (inclusive).
# Some apenas os números pares desse intervalo.
# Mostre a soma final na tela.

numero01 = int(input("Digite um número inteiro positivo "))

soma_pares = 0

for i in range(1, numero01, 1):
    if i % 2 == 0:
        soma_pares += i

print(f"A soma de números pares é: {soma_pares}")
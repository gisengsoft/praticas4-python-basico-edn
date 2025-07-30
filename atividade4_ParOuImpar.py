# =============================================
# Atividade 4 - Classificador Par ou Ãmpar
# Autor: Gilson Inacio
# =============================================

pares = 0
impares = 0

print("Digite nÃºmeros inteiros (0 para encerrar):")

while True:
    num = int(input("NÃºmero: "))
    if num == 0:
        break
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de Ã­mpares: {impares}")

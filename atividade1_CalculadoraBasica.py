# =============================================
# Atividade 1 - Calculadora Básica
# Autor: Gilson Inacio
# =============================================

print("Escolha a operação: +, -, *, /")
operacao = input("Operação: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}")

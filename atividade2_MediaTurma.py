# =============================================
# Atividade 2 - MÃ©dia da Turma
# Autor: Gilson Inacio
# =============================================

quantidade = int(input("Quantos alunos na turma? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Nota do aluno {i+1}: "))
    soma += nota

media = soma / quantidade
print(f"MÃ©dia da turma: {media:.2f}")

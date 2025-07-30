# =============================================
# Atividade 3 - Verificador de Senha Segura
# Autor: Gilson Inacio
# =============================================

senha = input("Digite a senha: ")

tem_numero = any(char.isdigit() for char in senha)
tamanho_minimo = len(senha) >= 8

if tem_numero and tamanho_minimo:
    print("Senha vÃ¡lida e segura!")
else:
    print("Senha invÃ¡lida. CritÃ©rios:")
    if not tamanho_minimo:
        print("- Deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- Deve conter pelo menos um nÃºmero.")
121
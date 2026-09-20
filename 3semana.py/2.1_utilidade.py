from modulo_utilidades import caixa, conversor_temperatura, ficha_aluno, validar_senha

print(f"25 graus Celsius = {conversor_temperatura(25)} graus Fahrenheit")
print(f"Senha valida: {validar_senha('Senha123')}")
print(f"Total da caixa: R$ {caixa(10, 5, 2.50):.2f}")
print(f"Ficha do aluno: {ficha_aluno(nome='Ana', idade=20, curso='Python')}")
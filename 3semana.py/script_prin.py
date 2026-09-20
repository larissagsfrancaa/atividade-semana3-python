from modulo_calculadora import dividir, multiplicar, subtrair, somar
from modulo_utilidades import caixa, conversor_temperatura, ficha_aluno, validar_senha
from lis import adicionar_item_seguro


print("Calculadora")
print(f"Soma: {somar(2, 3)}")
print(f"Subtracao: {subtrair(5, 2)}")
print(f"Multiplicacao: {multiplicar(4, 3)}")
print(f"Divisao: {dividir(10, 2)}")
print(f"Divisao por zero: {dividir(10, 0)}")

print("\nUtilidades")
print(f"25 graus Celsius = {conversor_temperatura(25)} graus Fahrenheit")
print(f"Senha valida: {validar_senha('Senha123')}")
print(f"Total da caixa: R$ {caixa(10, 5, 2.50):.2f}")
print(f"Ficha do aluno: {ficha_aluno(nome='Ana', idade=20, curso='Python')}")


def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

print("Divisão:", dividir(numero_1, numero_2))


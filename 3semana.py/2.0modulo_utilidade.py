def conversor_temperatura(celsius):
    return (celsius * 9 / 5) + 32


def validar_senha(senha):
    tem_tamanho_minimo = len(senha) >= 8
    tem_letra_maiuscula = any(caractere.isupper() for caractere in senha)
    tem_letra_minuscula = any(caractere.islower() for caractere in senha)
    tem_numero = any(caractere.isdigit() for caractere in senha)

    return (
        tem_tamanho_minimo
        and tem_letra_maiuscula
        and tem_letra_minuscula
        and tem_numero
    )


def caixa(*precos):
    return sum(precos)


def ficha_aluno(**dados):
    return dados
def contador_caracter(texto):
    """
    Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracter('luiz')
    i: 1
    l: 1
    u: 1
    z: 1

    :param texto: string a ser contada
    """

    caracteres_ordenados = sorted(texto)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contador_caracter('Banana')
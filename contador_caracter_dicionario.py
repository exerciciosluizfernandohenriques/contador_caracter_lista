def contador_caracter(nome):
    """
    Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracter('nome')
    {'i': 1, 'l': 1, 'i':1, 'z':1}
    :param texto: string a ser contada
    """


    resultado = {}

    for caracter in nome:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contador_caracter('banana'))

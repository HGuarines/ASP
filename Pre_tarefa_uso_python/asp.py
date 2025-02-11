""" Lib de Henrique para ASP 1 """


def gerar_arquivo_texto(nome_arquivo, titulo, calculos):
    """
    # Gera um arquivo de texto formatado com título, autor e cálculos fornecidos.

    Parâmetros:
    nome_arquivo (str): O nome do arquivo de saída.\n
    titulo (str): O título a ser exibido no arquivo.\n
    calculos (lista de tuplas): Uma lista onde cada tupla contém uma expressão e seu resultado.

    # Exemplo de uso:
    calculos = [
        ('a = 5 + 3', 5 + 3),
        ('b = 10 - 4', 10 - 4),
        ('c = 7 * 2', 7 * 2),
        ('d = 15 / 3', 15 / 3),
        ('e = 15 // 2', 15 // 2),
        ('g = 2 ** 3', 2 ** 3),
    ]

    gerar_arquivo_texto("saida1.txt", "Funções Matemáticas Básicas", calculos)
    """
    linha = '\n' + 45 * '*' + '\n'

    with open(nome_arquivo, 'w') as f:
        f.write(linha)
        f.write(f'{" " * 10}{titulo}{" " * 10}\n')
        f.write(f'{" " * 20}{'Henrique B Guarines'}{" " * 20}\n')
        f.write(linha)

        for expressao, resultado in calculos:
            if type(resultado) is str:
                f.write(f'{expressao:10} = {(resultado)}\n')
            else:
                f.write(f'{expressao:10} = {float(resultado):7.2f}\n')

        f.write(linha)

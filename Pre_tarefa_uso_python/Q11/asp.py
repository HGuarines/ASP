""" Lib de Henrique para ASP 1 """

import os


def gerar_arquivo_texto(nome_arquivo, titulo, calculos):
    """
    # Adiciona ou gera um arquivo de texto formatado com título, autor e cálculos fornecidos, evitando duplicações.

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
        ('g = 2 ** 3', 2 ** 3)
    ]

    gerar_arquivo_texto("exemplo.txt", "Funções Matemáticas Básicas", calculos)
    """
    linha = '\n' + 45 * '*' + '\n'
    conteudo_adicionar = []

    # Criar cabeçalho se for novo arquivo
    if not os.path.exists(nome_arquivo):
        conteudo_adicionar.append(linha)
        conteudo_adicionar.append(f'{" " * 10}{titulo}{" " * 10}\n')
        conteudo_adicionar.append(f'{" " * 10}Henrique B Guarines{" " * 20}\n')
        conteudo_adicionar.append(linha)

    # Carregar conteúdo existente para evitar duplicações
    conteudo_existente = ""
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding="utf-8") as f:
            conteudo_existente = f.read()

    # Construir as novas linhas de cálculo
    for expressao, resultado in calculos:
        linha_calculo = f'{expressao}{float(resultado) if isinstance(resultado, (int, float)) else resultado}\n'
        if linha_calculo not in conteudo_existente:
            conteudo_adicionar.append(linha_calculo)

    # Apenas escrever se houver conteúdo novo
    if conteudo_adicionar:
        with open(nome_arquivo, 'a', encoding="utf-8") as f:
            f.writelines(conteudo_adicionar)
            f.write(linha)

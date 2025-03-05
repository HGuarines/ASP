""" Lib de Henrique para ASP 1 """


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
    import os

    linha = '\n' + 45 * '*' + '\n'
    conteudo_adicionar = []

    # Criar cabeçalho se for novo arquivo
    if not os.path.exists(nome_arquivo):
        conteudo_adicionar.append(linha)
        conteudo_adicionar.append(f'{" " * 10}{titulo}{" " * 10}\n')
        conteudo_adicionar.append(f'{" " * 10}Henrique B Guarines{" " * 20}\n')
        conteudo_adicionar.append(linha)
        conteudo_adicionar.append('\n')

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


def ret2pol(cplx, unidade='r'):
    """
    # Converte um número complexo retangular para forma polar.

    Parâmetros:
    cplx (complex): O número complexo a ser convertido. (a + jb)
    unidade (str): A unidade do ângulo ('r' para radianos, 'g' para graus). Padrão é 'r'.

    Retorno:
    Uma tupla contendo o módulo e o argumento do número complexo fornecido. (r, phi)
    """
    from cmath import polar
    from numpy import degrees

    r, phi = polar(cplx)

    if unidade == 'g':
        phi = degrees(phi)  # Converter radianos para graus

    return r, phi


def pol2ret(r, phi, unidade='r'):
    """
    # Converte um número complexo polar para forma retangular.

    Parâmetros:
    r (float): O módulo do número complexo.\n
    phi (float): O argumento do número complexo.\n
    unidade (str): A unidade do ângulo ('r' para radianos, 'g' para graus). Padrão é 'r'.

    Retorno:
    O número complexo na forma retangular. (a + jb)
    """
    from cmath import rect
    from numpy import radians

    if unidade == 'g':
        phi = radians(phi)  # Converter graus para radianos

    return rect(r, phi)


def pot_comp1f(V, I):
    """
    # Calcula a potência complexa em um circuito monofásico.

    Parâmetros:\n
    V (a + jb): A tensão complexa no circuito.\n
    I (a + jb): A corrente complexa no circuito.

    Retorno:
    A potência complexa no circuito. (P + jQ)
    """
    S = V * I.conjugate()
    return S


def pot_comp3f(Va, Ia, Vb, Ib, Vc, Ic):
    """
    # Calcula a potência complexa trifásica S.

    Parâmetros:\n
    Va, Vb, Vc: Tensões de fase (números complexos)\n
    Ia, Ib, Ic: Correntes de fase (números complexos)

    Retorna:\n
    Potência complexa total S.
    """
    from numpy import conj
    Sa = Va * conj(Ia)
    Sb = Vb * conj(Ib)
    Sc = Vc * conj(Ic)

    S_total = Sa + Sb + Sc
    return S_total


def cor_carga(P, V, FP, N=3):
    """
    # Calcula a corrente de carga elétrica (I) em um sistema monofásico ou trifásico.

    **Parâmetros:**\n
    P (float): Potência ativa da carga em watts (W).\n
    V (float): Tensão de operação em volts (V).\n
    FP (float): Fator de potência (0 a 1).\n
    N (int, opcional): Número de fases (1 para monofásico, 3 para trifásico). Padrão = 3.

    **Retorno:**\n
    I (float): Corrente de carga em amperes (A).
    """
    P = float(abs(P))  # Garantir que seja um número real positivo
    V = float(abs(V))
    FP = float(FP)

    if N == 1:  # Monofásico
        I = P / (V * FP)
    elif N == 3:  # Trifásico
        from math import sqrt
        I = P / (sqrt(3) * V * FP)
    else:
        raise ValueError(
            "O número de fases deve ser 1 (monofásico) ou 3 (trifásico).")

    return I


def imp_serie(Z1, Z2):
    """
    # Calcula a impedância equivalente de dois elementos em série.

    Parâmetros:
    Z1 (a + jb): A primeira impedância.\n
    Z2 (a + jb): A segunda impedância.

    Retorno:
    A impedância equivalente dos dois elementos em série. (a + jb)
    """
    return Z1 + Z2


def imp_paral(Z1, Z2):
    """
    # Calcula a impedância equivalente de dois elementos em paralelo.

    Parâmetros:
    Z1 (a + jb): A primeira impedância.\n
    Z2 (a + jb): A segunda impedância.

    Retorno:
    A impedância equivalente dos dois elementos em paralelo. (a + jb)
    """
    return (Z1 * Z2) / (Z1 + Z2)


def oper_comp(Z1, form1, op, Z2, form2):
    """
    # Realiza operações com números complexos.

    Parâmetros:
    Z1 (complex): O primeiro número complexo.\n
    form1 (str): A forma do primeiro número complexo ("r: retangular" ou "p: polar, em radianos").\n
    op (str): O operador a ser aplicado ("+", "-", "*", "/").\n
    Z2 (complex): O segundo número complexo.\n
    form2 (str): A forma do segundo número complexo ("r: retangular" ou "p: polar", em radianos).

    Retorno:
    O resultado da operação entre os números complexos fornecidos.
    """

    if form1 == "p":
        Z1 = pol2ret(*Z1)
    if form2 == "p":
        Z2 = pol2ret(*Z2)

    if op == "+":
        return Z1 + Z2
    elif op == "-":
        return Z1 - Z2
    elif op == "*":
        return Z1 * Z2
    elif op == "/":
        return Z1 / Z2
    elif op not in ["+", "-", "*", "/"]:
        raise ValueError("Operação inválida. Use '+', '-', '*' ou '/'.")
    elif form1 not in ["r", "p"] or form2 not in ["r", "p"]:
        raise ValueError("Forma inválida. Use 'r' ou 'p'.")


def Qcor_pot(P, FPA, FPN):
    """
    # Calcula a potência reativa de correção necessária para compensar o fator de potência de um sistema.

    Parâmetros:
    P (float): A potência ativa da carga em W.\n
    FPA (float): O fator de potência antigo do sistema (0 a 1).\n
    FPN (float): O fator de potência desejado para o sistema (0 a 1).

    Retorno:
    A potência reativa de correção necessária em VAr.
    """
    from math import tan, acos

    FPA = acos(FPA)
    FPN = acos(FPN)
    Qc = P * (tan(FPA) - tan(FPN))
    return Qc


def cte_gener(Zpi, Ya, Yb):
    """
    # Calcula os parâmetros ABCD para um quadripolo obtido a partir de uma rede PI.

    Parâmetros:
    Zpi (float ou complexo): Impedância em série na rede PI.\n
    Ya (float ou complexo): Admitância shunt na entrada.\n
    Yb (float ou complexo): Admitância shunt na saída.

    Retorno:
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = 1 + Zpi * Ya
    B = Zpi
    C = Ya + Yb + Zpi * Ya * Yb
    D = 1 + Zpi * Yb

    return A, B, C, D


def format_complex(c, form='r'):
    """
    # Formata um número complexo em uma string legível.

    Parâmetros:
    c (complex): O número complexo a ser formatado.
    form (str): A forma do número complexo ('r' para retangular, 'p' para polar). Padrão é 'r'.

    Retorno:
    Uma string representando o número complexo no formato "a + bj" ou "a - bj" para retangular,
    ou "r ∠ θ°" para polar.
    """
    from math import degrees
    from cmath import polar

    if isinstance(c, tuple):  # Se já for uma tupla, não precisa chamar polar()
        r, theta = c
    elif isinstance(c, complex):  # Se for um número complexo, converta
        r, theta = polar(c)
    else:
        raise TypeError(
            "Entrada inválida: deve ser um número complexo ou uma tupla (módulo, fase).")

    if form == 'r':
        real_part = f'{c.real:.2f}' if c.real != 0 else ''
        imag_part = f'{abs(c.imag):.2f}j' if c.imag != 0 else ''
        if c.imag > 0 and c.real != 0:
            imag_part = f'+ {imag_part}'
        elif c.imag < 0:
            imag_part = f'- {imag_part}'
        if real_part and imag_part:
            return f'{real_part} {imag_part}'
        elif real_part:
            return real_part
        elif imag_part:
            return imag_part
        else:
            return '0'
    elif form == 'p':
        theta = degrees(theta)  # Converter radianos para graus
        return f'{r:.2f} ∠ {theta:.2f}°'
    else:
        raise ValueError(
            "Forma inválida. Use 'r' para retangular ou 'p' para polar.")


def quad_casc(A1, B1, C1, D1, A2, B2, C2, D2):
    """
    # Calcula os parâmetros ABCD de um quadripolo obtido pela cascata de dois quadripolos.

    Parâmetros:
    A1, B1, C1, D1: Parâmetros do primeiro quadripolo.\n
    A2, B2, C2, D2: Parâmetros do segundo quadripolo.

    Retorno:
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = A1 * A2 + B1 * C2
    B = A1 * B2 + B1 * D2
    C = C1 * A2 + D1 * C2
    D = C1 * B2 + D1 * D2

    return A, B, C, D


def quad_par(A1, B1, C1, D1, A2, B2, C2, D2):
    """
    # Calcula os parâmetros ABCD de um quadripolo obtido pela paralelo de dois quadripolos.

    Parâmetros:
    A1, B1, C1, D1: Parâmetros do primeiro quadripolo.\n
    A2, B2, C2, D2: Parâmetros do segundo quadripolo.

    Retorno:
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = A1 + A2
    B = B1 + B2
    C = C1 + C2
    D = D1 + D2

    return A, B, C, D


def cirpi(V2, I2, Z, Ya, Yb, nomearq):
    """
    # Calcula a tensão V1 e a corrente I1 no terminal transmissor de um circuito Pi,
    conhecendo a tensão V2, corrente I2, impedância Z e admitâncias Ya e Yb.

    Parâmetros:
    V2 (complex): Tensão no terminal receptor\n
    I2 (complex): Corrente no terminal receptor\n
    Z (complex): Impedância em série\n
    Ya (complex): Admitância shunt na entrada\n
    Yb (complex): Admitância shunt na saída\n
    nomearq (str): Nome do arquivo de saída contendo os resultados

    Retorno:
    (V1, I1) - Tensão e corrente no terminal transmissor
    """
    import numpy as np

    # Utilizando a função existente para calcular os parâmetros ABCD
    A, B, C, D = cte_gener(Z, Ya, Yb)

    # Resolvendo para V1 e I1 usando a equação matricial
    matriz_abcd = np.array([[A, B], [C, D]])
    vetor_v2_i2 = np.array([V2, I2])
    V1, I1 = np.dot(matriz_abcd, vetor_v2_i2)

    # Criar lista de cálculos formatados para salvar no arquivo
    calculos = [
        ('Dados de Entrada:', ''),
        ("V2 = ", format_complex(V2)),
        ("I2 = ", format_complex(I2)),
        ("Z  = ", format_complex(Z)),
        ("Ya = ", format_complex(Ya)),
        ("Yb = ", format_complex(Yb)),
        ('\nResultados:', ''),
        ("V1 = ", format_complex(V1)),
        ("I1 = ", format_complex(I1))
    ]

    # Salvar os resultados no arquivo utilizando a função existente
    gerar_arquivo_texto(nomearq, "Resultados do Circuito Pi", calculos)

    return V1, I1


def cirpir(V1, I1, Z, Ya, Yb, nomearq):
    """
    # Calcula a tensão V2 e a corrente I2 no terminal receptor de um circuito Pi,
    conhecendo a tensão V1, corrente I1, impedância Z e admitâncias Ya e Yb.

    Parâmetros:
    V1 (complex): T
    ensão no terminal transmissor\n
    I1 (complex): Corrente no terminal transmissor\n
    Z (complex): Impedância em série\n
    Ya (complex): Admitância shunt na entrada\n
    Yb (complex): Admitância shunt na saída\n
    nomearq (str): Nome do arquivo de saída contendo os resultados

    Retorno:
    (V2, I2) - Tensão e corrente no terminal receptor
    """

    import numpy as np

    # Utilizando a função existente para calcular os parâmetros ABCD
    A, B, C, D = cte_gener(Z, Ya, Yb)

    # Resolvendo para V2 e I2 usando a equação matricial
    matriz_abcd = np.array([[A, B], [C, D]])
    vetor_v1_i1 = np.array([V1, I1])
    V2, I2 = np.linalg.solve(matriz_abcd, vetor_v1_i1)

    # Criar lista de cálculos formatados para salvar no arquivo
    calculos = [
        ('Dados de Entrada:', ''),
        ("V1 = ", format_complex(V1)),
        ("I1 = ", format_complex(I1)),
        ("Z  = ", format_complex(Z)),
        ("Ya = ", format_complex(Ya)),
        ("Yb = ", format_complex(Yb)),
        ('\nResultados:', ''),
        ("V2 = ", format_complex(V2)),
        ("I2 = ", format_complex(I2))
    ]

    # Salvar os resultados no arquivo utilizando a função existente
    gerar_arquivo_texto(nomearq, "Resultados do Circuito Pi", calculos)

    return V2, I2

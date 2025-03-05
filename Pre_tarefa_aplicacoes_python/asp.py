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
        return f'{c.real:.2f} {"+" if c.imag >= 0 else "-"} {abs(c.imag):.2f}j'
    elif form == 'p':
        theta = degrees(theta)  # Converter radianos para graus
        return f'{r:.2f} ∠ {theta:.2f}°'
    else:
        raise ValueError(
            "Forma inválida. Use 'r' para retangular ou 'p' para polar.")

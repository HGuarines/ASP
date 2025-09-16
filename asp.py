""" Lib de Henrique para ASP 1 """


def gerar_arquivo_texto(nome_arquivo, titulo, calculos):
    """
    # Adiciona ou gera um arquivo de texto formatado com título, autor e cálculos fornecidos, evitando duplicações.

    **Parâmetros:**\n
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

    **Parâmetros:**\n
    cplx (complex): O número complexo a ser convertido. (a + jb)
    unidade (str): A unidade do ângulo ('r' para radianos, 'g' para graus). Padrão é 'r'.

    **Retorno:**\n
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

    **Parâmetros:**\n
    r (float): O módulo do número complexo.\n
    phi (float): O argumento do número complexo.\n
    unidade (str): A unidade do ângulo ('r' para radianos, 'g' para graus). Padrão é 'r'.

    **Retorno:**\n
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

    **Parâmetros:**\n
    V (a + jb): A tensão complexa no circuito.\n
    I (a + jb): A corrente complexa no circuito.

    **Retorno:**\n
    A potência complexa no circuito. (P + jQ)
    """
    S = V * I.conjugate()
    return S


def pot_comp3f(Va, Ia, Vb, Ib, Vc, Ic):
    """
    # Calcula a potência complexa trifásica S.

    **Parâmetros:**\n
    Va, Vb, Vc: Tensões de fase (números complexos)\n
    Ia, Ib, Ic: Correntes de fase (números complexos)

    **Retorno:**\n
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


def imp_serie(*impedancias):
    """
    # Calcula a impedância equivalente de múltiplos elementos em série.

    **Parâmetros:**\n
    *impedancias (a + jb): As impedâncias dos elementos.

    **Retorno:**\n
    A impedância equivalente dos elementos em série. (a + jb)
    """
    return sum(impedancias)


def imp_paral(*impedancias):
    """
    # Calcula a impedância equivalente de múltiplos elementos em paralelo.

    **Parâmetros:**\n
    *impedancias (a + jb): As impedâncias dos elementos.

    **Retorno:**\n
    A impedância equivalente dos elementos em paralelo. (a + jb)
    """
    from functools import reduce

    if len(impedancias) == 0:
        raise ValueError("Deve haver pelo menos uma impedância fornecida.")

    # Função auxiliar para calcular a impedância equivalente de dois elementos em paralelo
    def paralelo(Z1, Z2):
        return (Z1 * Z2) / (Z1 + Z2)

    # Reduzir a lista de impedâncias usando a função auxiliar
    return reduce(paralelo, impedancias)


def oper_comp(c1, form1, op, c2, form2):
    """
    # Realiza operações com números complexos.

    **Parâmetros:**\n
    c1 (complex): O primeiro número complexo.\n
    form1 (str): A forma do primeiro número complexo ("r: retangular" ou "p: polar, em radianos").\n
    op (str): O operador a ser aplicado ("+", "-", "*", "/").\n
    c2 (complex): O segundo número complexo.\n
    form2 (str): A forma do segundo número complexo ("r: retangular" ou "p: polar", em radianos).

    **Retorno:**\n
    O resultado da operação entre os números complexos fornecidos.
    """

    if form1 == "p":
        c1 = pol2ret(*c1)
    if form2 == "p":
        c2 = pol2ret(*c2)

    if op == "+":
        return c1 + c2
    elif op == "-":
        return c1 - c2
    elif op == "*":
        return c1 * c2
    elif op == "/":
        return c1 / c2
    elif op not in ["+", "-", "*", "/"]:
        raise ValueError("Operação inválida. Use '+', '-', '*' ou '/'.")
    elif form1 not in ["r", "p"] or form2 not in ["r", "p"]:
        raise ValueError("Forma inválida. Use 'r' ou 'p'.")


def Qcor_pot(P, FPA, FPN):
    """
    # Calcula a potência reativa de correção necessária para compensar o fator de potência de um sistema.

    **Parâmetros:**\n
    P (float): A potência ativa da carga em W.\n
    FPA (float): O fator de potência antigo do sistema (0 a 1).\n
    FPN (float): O fator de potência desejado para o sistema (0 a 1).

    **Retorno:**\n
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

    **Parâmetros:**\n
    Zpi (float ou complexo): Impedância em série na rede PI.\n
    Ya (float ou complexo): Admitância shunt na entrada.\n
    Yb (float ou complexo): Admitância shunt na saída.

    **Retorno:**\n
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = 1 + Zpi * Ya
    B = Zpi
    C = Ya + Yb + Zpi * Ya * Yb
    D = 1 + Zpi * Yb

    return A, B, C, D


def format_complex(c, form='r', precisao=2):
    """
    # Formata um número complexo em uma string legível.

    **Parâmetros:**\n
    c (complex): O número complexo a ser formatado. **imput do angulo sempre em radianos**\n
    form (str): A forma do número complexo ('r' para retangular, 'p' para polar, 'e' para exponencial). Padrão é 'r'.\n
    precisao (int): O número de casas decimais para arredondamento. Padrão é 2.\n

    **Retorno:**\n
    Uma string representando o número complexo no formato "a + bj" ou "a - bj" para retangular,
    "r ∠ θ°" para polar, ou "r * e^(jθ)" para exponencial.
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
        parte_real = f'{c.real:.{precisao}f}' if c.real != 0 else ''
        parte_imaginaria = f'{abs(c.imag):.{precisao}f}j' if c.imag != 0 else ''
        if c.imag > 0 and c.real != 0:
            parte_imaginaria = f'+ {parte_imaginaria}'
        elif c.imag < 0:
            parte_imaginaria = f'- {parte_imaginaria}'
        if parte_real and parte_imaginaria:
            return f'{parte_real} {parte_imaginaria}'
        elif parte_real:
            return parte_real
        elif parte_imaginaria:
            return parte_imaginaria
        else:
            return '0'
    elif form == 'p':
        theta = degrees(theta)  # Converter radianos para graus
        return f'{r:.{precisao}f} ∠ {theta:.{precisao}f}°'
    elif form == 'e':
        return f'{r:.{precisao}f}*e^{theta:.{precisao}f}j'
    else:
        raise ValueError(
            "Forma inválida. Use 'r' para retangular, 'p' para polar ou 'e' para exponencial.")


def quad_casc(A1, B1, C1, D1, A2, B2, C2, D2):
    """
    # Calcula os parâmetros ABCD de um quadripolo obtido pela cascata de dois quadripolos.

    **Parâmetros:**\n
    A1, B1, C1, D1: Parâmetros do primeiro quadripolo.\n
    A2, B2, C2, D2: Parâmetros do segundo quadripolo.

    **Retorno:**\n
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = A1 * A2 + B1 * C2
    B = A1 * B2 + B1 * D2
    C = C1 * A2 + D1 * C2
    D = C1 * B2 + D1 * D2

    return A, B, C, D


def quad_par(A1, B1, C1, D1, A2, B2, C, D2):
    """
    # Calcula os parâmetros ABCD de um quadripolo obtido pela paralelo de dois quadripolos.

    **Parâmetros:**\n
    A1, B1, C1, D1: Parâmetros do primeiro quadripolo.\n
    A2, B2, C2, D2: Parâmetros do segundo quadripolo.

    **Retorno:**\n
    Uma tupla contendo os parâmetros da matriz de transmissão (A, B, C, D).
    """
    A = A1 + A2
    B = B1 + B2
    C = C1 + C2
    D = D1 + D2

    return A, B, C, D


def cirpi(V2, I2, Z, Ya, Yb, nomearq=None):
    """
    # Calcula a tensão V1 e a corrente I1 no terminal transmissor de um circuito Pi, conhecendo a tensão V2, corrente I2, impedância Z e admitâncias Ya e Yb.

    **Parâmetros:**\n
    V2 (complex): Tensão no terminal receptor\n
    I2 (complex): Corrente no terminal receptor\n
    Z (complex): Impedância em série\n
    Ya (complex): Admitância shunt na entrada\n
    Yb (complex): Admitância shunt na saída\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
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
    if nomearq:
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

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(nomearq, "Resultados do Circuito Pi", calculos)

    return V1, I1


def cirpir(V1, I1, Z, Ya, Yb, nomearq=None):
    """
    # Calcula a tensão V2 e a corrente I2 no terminal receptor de um circuito Pi, conhecendo a tensão V1, corrente I1, impedância Z e admitâncias Ya e Yb.

    **Parâmetros:**\n
    V1 (complex): T\n
    ensão no terminal transmissor\n
    I1 (complex): Corrente no terminal transmissor\n
    Z (complex): Impedância em série\n
    Ya (complex): Admitância shunt na entrada\n
    Yb (complex): Admitância shunt na saída\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
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
    if nomearq:
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

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(nomearq, "Resultados do Circuito Pi", calculos)

    return V2, I2


def delta2estrela(zab, zbc, zca, nomearq=None):
    """
    # Converte um circuito delta em estrela.

    **Parâmetros:**\n
    zab, zbc, zca (complex): Impedâncias de fase do circuito delta\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    Uma tupla (za, zb, zc) com ai impedâncias de fase do circuito estrela
    """

    # Cálculo das impedâncias de fase do circuito delta
    zt = zab + zbc + zca
    za = (zab * zbc) / zt
    zb = (zbc * zca) / zt
    zc = (zca * zab) / zt

    # Criar lista de cálculos formatados para salvar no arquivo
    if nomearq:
        calculos = [
            ('Dados de Entrada: ', '(Impedancias de fase em Delta)'),
            ("Zab = ", format_complex(zab)),
            ("Zbc = ", format_complex(zbc)),
            ("Zca = ", format_complex(zca)),
            ('\nResultados: ', '(Impedancias de fase em Estrela)'),
            ("Za = ", format_complex(za)),
            ("Zb = ", format_complex(zb)),
            ("Zc = ", format_complex(zc))
        ]

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(
            nomearq, "Resultados da Conversão Delta-Estrela", calculos)

    return za, zb, zc


def estrela2delta(za, zb, zc, nomearq=None):
    """
    # Converte um circuito estrela em delta.\n

    **Parâmetros:**\n
    za, zb, zc (complex): Impedâncias de fase do circuito estrela\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    (zab, zbc, zca) - Impedâncias de fase do circuito delta
    """

    # Cálculo das impedâncias de fase do circuito estrela
    z_num = za * zb + zb * zc + zc * za
    zab = z_num / zb
    zbc = z_num / zc
    zca = z_num / za

    # Criar lista de cálculos formatados para salvar no arquivo
    if nomearq:
        calculos = [
            ('Dados de Entrada:', '(Impedancias de fase em Estrela)'),
            ("Za = ", format_complex(za)),
            ("Zb = ", format_complex(zb)),
            ("Zc = ", format_complex(zc)),
            ('\nResultados:', '(Impedancias de fase em Delta)'),
            ("Zab = ", format_complex(zab)),
            ("Zbc = ", format_complex(zbc)),
            ("Zca = ", format_complex(zca))
        ]

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(
            nomearq, "Resultados da Conversão Estrela-Delta", calculos)

    return zab, zbc, zca


def queda1f(Ic, DVc, Lc, Vfn, nomearq=None):
    """
    # Calcula a seção do condutor (Sc) para um circuito monofásico em cobre.

    **Parâmetros:**\n
    Ic (float): Corrente total do circuito em A.\n
    DVc (float): Queda de tensão máxima admitida em %.\n
    Lc (float): Comprimento total do circuito em metros.\n
    Vfn (float): Tensão fase-neutro em volts.\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    Sc (float): Seção do condutor em mm².
    """
    # Resistividade do cobre em Ω.mm²/m
    rho = 1 / 56

    # Cálculo da seção do condutor
    Sc = (200 * rho * (Lc * Ic)) / (DVc * Vfn)

    # Criar lista de cálculos formatados para salvar no arquivo
    if nomearq:
        calculos = [
            ('Dados de Entrada:', ''),
            ("Ic = ", f"{Ic} A"),
            ("DVc = ", f"{DVc} %"),
            ("Lc = ", f"{Lc} m"),
            ("Vfn = ", f"{Vfn} V"),
            ("\nSeção do condutor (Sc) = ", f"{Sc:.2f} mm²")
        ]

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(
            nomearq, "Cálculo da Queda de Tensão Monofásica", calculos)

    return Sc


def queda3f(Ic, DVc, Lc, Vfn, nomearq=None):
    """
    # Calcula a seção do condutor (Sc) para um circuito trifásico em cobre.

    **Parâmetros:**\n
    Ic (float): Corrente total do circuito em A.\n
    DVc (float): Queda de tensão máxima admitida em %.\n
    Lc (float): Comprimento total do circuito em metros.\n
    Vfn (float): Tensão fase-neutro em volts.\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    Sc (float): Seção do condutor em mm².
    """
    # Resistividade do cobre em Ω.mm²/m
    rho = 1 / 56

    # Cálculo da seção do condutor
    Sc = (173.2 * rho * (Lc * Ic)) / (DVc * Vfn)

    # Criar lista de cálculos formatados para salvar no arquivo
    if nomearq:
        calculos = [
            ('Dados de Entrada:', ''),
            ("Ic = ", f"{Ic} A"),
            ("DVc = ", f"{DVc} %"),
            ("Lc = ", f"{Lc} m"),
            ("Vfn = ", f"{Vfn} V"),
            ("\nSeção do condutor (Sc) = ", f"{Sc:.2f} mm²")
        ]

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(
            nomearq, "Cálculo da Queda de Tensão Trifásica", calculos)

    return Sc


def vfonte(Vc, Z, Sc, nomearq=None):
    """
    # Calcula a tensão na fonte e a corrente do alimentador.

    **Parâmetros:**\n
    Vc (tupla): Tensão na carga (módulo e fase, em graus).\n
    Z (tupla): Impedância do alimentador (R e X, em ohms).\n
    Sc (tupla): Potência complexa da carga (Pc e Qc, em VA).\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    (Vf, I) - Tensão na fonte e corrente do alimentador.
    """
    # Converter entrada para forma retangular
    Vc_rect = pol2ret(*Vc, unidade='g')
    Z_rect = complex(*Z)  # Impedância já está em forma retangular
    Sc_rect = complex(*Sc)  # Potência complexa

    # Calcular corrente no alimentador
    I = Sc_rect.conjugate() / Vc_rect  # I = S*/V

    # Calcular tensão na fonte
    Vf_rect = Vc_rect + I * Z_rect

    # Converter resultados para polar
    Vf_polar = ret2pol(Vf_rect, unidade='g')
    I_polar = ret2pol(I, unidade='g')

    # Se nomearq for fornecido, salvar os resultados no arquivo
    if nomearq:
        calculos = [
            ('Dados de Entrada:', ''),
            ("Vc = ", format_complex(Vc_rect, 'p')),
            ("Z = ", format_complex(Z_rect, 'r')),
            ("Sc = ", format_complex(Sc_rect, 'r')),
            ('\nResultados:', ''),
            ("Vf = ", format_complex(Vf_rect, 'p')),
            ("I = ", format_complex(I, 'p'))
        ]

        gerar_arquivo_texto(nomearq, "Cálculo da Tensão na Fonte", calculos)

    return Vf_polar, I_polar


def vfontepi(Vc, Z, Ya, Yb, Sc, nomearq=None):
    """
    # Calcula a tensão na fonte e a corrente do alimentador para um circuito Pi.

    **Parâmetros:**\n
    Vc (tupla): Tensão na carga (módulo e fase, em graus).\n
    Z (tupla): Impedância do alimentador (R e X, em ohms).\n
    Ya (tupla): Admitância no lado da fonte (G e B, em S).\n
    Yb (tupla): Admitância no lado da carga (G e B, em S).\n
    Sc (tupla): Potência complexa da carga (Pc e Qc, em VA).\n
    nomearq (str, opcional): Nome do arquivo de saída. Padrão é None.

    **Retorno:**\n
    (Vf, I) - Tensão na fonte e corrente do alimentador.
    """
    # Converter entradas para forma retangular
    Vc_ret = pol2ret(*Vc, unidade='g') if isinstance(Vc, tuple) else Vc
    Z_ret = complex(*Z) if isinstance(Z, tuple) else Z
    Ya_ret = complex(*Ya) if isinstance(Ya, tuple) else Ya
    Yb_ret = complex(*Yb) if isinstance(Yb, tuple) else Yb
    Sc_ret = complex(*Sc) if isinstance(Sc, tuple) else Sc

    # Calcular corrente no alimentador
    I = Sc_ret.conjugate() / Vc_ret  # I = S*/V

    # Determinar admitância total
    Y_total = Ya_ret + Yb_ret

    # Calcular tensão na fonte considerando a impedância do alimentador
    Vf_ret = Vc_ret + (I * Z_ret) + (I / Y_total)

    # Converter resultados para forma polar
    Vf_polar = ret2pol(Vf_ret, unidade='g')
    I_polar = ret2pol(I, unidade='g')

    # Salvar os resultados no arquivo se nomearq for fornecido
    if nomearq:
        calculos = [
            ('Dados de Entrada:', ''),
            ("Vc = ", format_complex(Vc_ret, 'p')),
            ("Z = ", format_complex(Z_ret, 'r')),
            ("Ya = ", format_complex(Ya_ret, 'r')),
            ("Yb = ", format_complex(Yb_ret, 'r')),
            ("Sc = ", format_complex(Sc_ret, 'r')),
            ('\nResultados:', ''),
            ("Vf = ", format_complex(Vf_ret, 'p')),
            ("I = ", format_complex(I, 'p'))
        ]
        gerar_arquivo_texto(
            nomearq, "Cálculo da Tensão na Fonte para Circuito Pi", calculos)

    return Vf_polar, I_polar


def impcabo(secao_bt, nomearq=None):
    """
    # Calcula a impedância do cabo de cobre com isolação de PVC em Ω/km.

    **Parâmetros:**\n
    secao_bt (float): Seção do condutor em mm².\n
    nomearq (str, opcional): Nome do arquivo para salvar os resultados. None por padrão.

    **Retorno:**\n
    A impedância do cabo de cobre em Ω/km.
    """
    # Tabela de resistência e reatância (em mΩ/m)
    tabela_cabos = {
        1: (22.1, 0.176), 1.5: (14.8, 0.168), 2.5: (8.91, 0.155),
        4: (5.57, 0.143), 6: (3.71, 0.135), 10: (2.24, 0.119),
        16: (1.41, 0.112), 25: (0.880, 0.106), 35: (0.841, 0.101),
        50: (0.473, 0.101), 70: (0.328, 0.0965), 95: (0.236, 0.0975),
        120: (0.188, 0.0939), 150: (0.153, 0.0928), 185: (0.123, 0.0908),
        240: (0.0943, 0.0902), 300: (0.0761, 0.0895), 400: (0.0607, 0.0876),
        500: (0.0496, 0.0867), 630: (0.0402, 0.0865)
    }

    # Verificar se a seção nominal está na tabela
    if secao_bt not in tabela_cabos:
        raise ValueError(
            f"Seção nominal não encontrada na tabela. Favor selecionar entre: {', '.join(map(str, tabela_cabos.keys()))} mm².")

    # Obter resistência e reatância
    resistencia, reatancia = tabela_cabos[secao_bt]
    impedancia = complex(resistencia, reatancia)  # Convertendo para Ω/km

    # Criar lista de cálculos formatados para salvar no arquivo
    if nomearq:
        calculos = [
            ("Seção do condutor (Sc) = ", f"{secao_bt} mm²"),
            ('Impedância do cabo = ',
             f"{format_complex(impedancia, 'r', 3)} Ω/km")
        ]

        # Salvar os resultados no arquivo desejado
        gerar_arquivo_texto(
            nomearq, "Cálculo da Impedância do Cabo de Cobre", calculos)

    return impedancia


def inst2fasor(amplitude, angulo, tipo='cos', unidade='g'):
    """
    # Converte uma corrente ou tensão instantânea para fasor na forma retangular e polar.

    **Parâmetros:**\n   
    amplitude (float): Amplitude da corrente.\n
    angulo (float): Ângulo de fase (em graus, se unidade='g', ou radianos, se unidade='r').\n
    tipo (str): 'cos' se for baseado no cosseno, 'sin' se for baseado no seno.\n
    unidade (str): 'g' para graus (default), 'r' para radianos.\n

    **Retorno:**\n
    tuple: Fasor na forma retangular e polar.
    """
    from cmath import rect, polar
    from math import radians, degrees

    if unidade == 'g':
        angulo = radians(angulo)  # Converte para radianos se necessário

    if tipo == 'sin':
        angulo -= radians(90)  # Converte seno para cosseno subtraindo 90°

    # Representação retangular
    fasor_ret = rect(amplitude, angulo)

    # Representação polar
    modulo, fase = polar(fasor_ret)
    if unidade == 'g':
        fase = degrees(fase)  # Converte de volta para graus

    return fasor_ret, (modulo, fase)


def plot_fasor(*fasores, nome_arquivo=None):
    """
    # Plota um diagrama fasorial e salva a imagem.

    **Parâmetros:**\n
    nome_arquivo (str): Nome do arquivo para salvar a imagem do diagrama.\n
    *fasores (tuplas): Lista de fasores no formato (valor, label).

    **Retorno:**\n
    Gera e salva um diagrama fasorial com os fasores fornecidos.
    """
    import matplotlib.pyplot as plt
    import random

    plt.figure()

    cores = ["r", "g", "b", "m", "c", "y", "k"]  # Lista de 7 cores fixas
    random.shuffle(cores)  # Embaralha as cores para garantir variedade

    for (fasor, rotulo), cor in zip(fasores, cores):
        if fasor:  # Verifica se o fasor não é vazio
            plt.arrow(0, 0, fasor.real, fasor.imag, head_width=0.5,
                      head_length=0.5, color=cor, label=rotulo)

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title("Diagrama Fasorial")
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginária")

    # Salvar a imagem se nome_arquivo for fornecido
    if nome_arquivo:
        plt.savefig(nome_arquivo)
        print(f"Diagrama fasorial salvo como {nome_arquivo}")
    plt.show()


def fator_potencia(V=None, I=None, Zeq=None, S=None, P=None, mod_S=None):
    """
    # Calcula o fator de potência a partir de diferentes combinações de parâmetros.

    **Parâmetros:**\n
    V (complex, opcional): Tensão do circuito (número complexo).\n
    I (complex, opcional): Corrente do circuito (número complexo).\n
    Zeq (complex, opcional): Impedância equivalente do circuito (número complexo).\n
    S (complex, opcional): Potência aparente (VA).\n
    P (float, opcional): Potência ativa (W).\n
    mod_S (float, opcional): Módulo da potência aparente (VA).\n
    **Retorno:**\n
    FP (float): Fator de potência (0 a 1), indicando a eficiência da utilização da potência.
    """
    if S is None:
        if V is not None and I is not None:
            S = V * I.conjugate()  # Calcula potência aparente se V e I forem fornecidos
        elif mod_S is not None:
            S = mod_S  # Usa diretamente o módulo de S, se fornecido
        else:
            raise ValueError(
                "Para calcular o fator de potência sem S, forneça V e I ou o módulo de S.")

    if P is None:
        if isinstance(S, complex):
            P = S.real  # Usa a parte real de S como potência ativa se P não for fornecido
        else:
            raise ValueError(
                "Para calcular o fator de potência sem P, forneça P ou um S complexo.")

    if abs(S) == 0:
        raise ValueError("A potência aparente não pode ser zero.")

    FP = abs(P) / abs(S)
    return FP


def calc_banco_capacitor(P, FP_inicial, FP_final, V, f):
    """
    # Calcula a capacitância necessária para correção do fator de potência.

    **Parâmetros:**\n
    P (float): Potência ativa em watts (W)\n
    FP_inicial (float): Fator de potência inicial (adimensional)\n
    FP_final (float): Fator de potência final desejado (adimensional)\n
    V (float): Tensão em volts (V)\n
    f (float): Frequência em hertz (Hz)\n

    **Retorna:**\n
    float: Capacitância necessária em microfarads (μF)
    """
    from math import pi

    # Calcula a potência reativa necessária para correção
    Qc = Qcor_pot(P, FP_inicial, FP_final)

    # Cálculo da capacitância necessária
    Xc = V**2 / Qc  # Reatância capacitiva
    C = 1 / (2 * pi * f * Xc)  # Capacitância em farads

    return C * 1e6  # Convertendo para microfarads (μF)


def mudar_base(pu_antigo, S_base_antiga, S_base_nova, V_base_antiga, V_base_nova, tipo="z"):
    """
    # Calcula a impedância ou a corrente em pu após mudança de base.

    **Parâmetros:**
    pu_antigo (float): Impedância ou corrente em pu na base antiga\n
    S_base_antiga (float): Potência base antiga em VA\n
    S_base_nova (float): Potência base nova em VA\n
    V_base_antiga (float): Tensão base antiga em V\n
    V_base_nova (float): Tensão base nova em V\n
    tipo (str): Escolhe o tipo de cálculo: "z" para impedancia ou "i" para corrente\n

    **Retorno:**\n
    float: Nova impedância ou nova corrente em pu, dependendo do tipo selecionado
    """
    # Cálculo da impedância em pu
    if tipo == "z":
        pu_novo = pu_antigo * (S_base_nova / S_base_antiga) * \
            ((V_base_antiga ** 2) / (V_base_nova ** 2))

    # Cálculo da corrente em pu
    elif tipo == "i":
        pu_novo = pu_antigo * (S_base_antiga / S_base_nova) * \
            (V_base_nova / V_base_antiga)

    else:
        raise ValueError(
            "Tipo inválido. Escolha 'z' para impedancia ou 'i' para corrente.")

    return pu_novo


def calcular_potencias(mva, fp):
    """
    Calcula a potência ativa (W) e reativa (Var) a partir de MVA e FP.

    Parâmetros:
    mva (float): Potência aparente em MVA (Mega Volt-Amperes).
    fp (float): Fator de potência (0 a 1).

    Retorna:
    tuple: Potência ativa em MW (Megawatts) e potência reativa em MVAr (Mega Volt-Amps reativos).
    """
    mw = mva * fp  # Potência ativa em MW
    mvar = mva * (1 - fp**2)**0.5  # Potência reativa em MVAr
    return mw, mvar


class SistemaEletrico:
    """
    Classe para modelagem de sistemas elétricos.

    Permite criar uma representação de um sistema elétrico com N barras e seus ramos,
    e realizar cálculos como matriz de admitância de barra (Ybus), matriz de impedância
    de barra (Zbus), e cálculo de fluxos.

    A numeração das barras segue a convenção 1-based, com a barra 0 representando
    a referência (terra) externa ao sistema.
    """

    def __init__(self, num_barras):
        """
        Inicializa um sistema elétrico com o número especificado de barras.

        Permite criar uma representação de um sistema elétrico com N barras e seus ramos,
        e realizar cálculos como matriz de admitância de barra (Ybus), matriz de impedância
        de barra (Zbus), e cálculo de fluxos.

        **Parâmetros:**\n
        num_barras (int): Número de barras do sistema, excluindo a referência.

        **Levanta:**\n
        ValueError: Se o número de barras for negativo.
        """
        self.nb = int(num_barras)
        if self.nb < 0:
            raise ValueError("Número de barras deve ser >= 0")
        self.ramos = []  # Lista para armazenar os ramos do sistema

    def adicionar_ramo(self, *args, **kwargs):
        """
        Adiciona um ramo ao sistema elétrico com interface flexível.

        **Formatos aceitos:**\n
        - adicionar_ramo(de, para, zser, ysa=0j, ysb=0j, eram=0.0, faseramo=0.0, identif="")
        - Pode passar argumentos posicionais; se o último for string, é interpretado como identificador.
        - Se passar um único argumento iterável (lista/tupla), considera como linha completa de dados.

        **Parâmetros:**\n
        de (int): Número da barra de origem (1-based, 0 = referência)
        para (int): Número da barra de destino (1-based, 0 = referência)
        zser (complex): Impedância série do ramo
        ysa (complex, opcional): Admitância shunt no início do ramo. Padrão: 0j
        ysb (complex, opcional): Admitância shunt no fim do ramo. Padrão: 0j
        eram (float, opcional): Módulo da tensão interna (fonte). Padrão: 0.0
        faseramo (float, opcional): Ângulo da tensão interna em graus. Padrão: 0.0
        identif (str, opcional): Identificador do ramo. Padrão: ""

        **Retorno:**\n
        SistemaEletrico: O próprio objeto (para permitir chamadas encadeadas)

        **Levanta:**\n
        ValueError: Se parâmetros mínimos (de, para, zser) não forem fornecidos.
        """
        # Se passou um único iterable (lista/tuple), desempacotamos
        pos = []
        if len(args) == 1 and not isinstance(args[0], (str, bytes)) and hasattr(args[0], "__iter__"):
            pos = list(args[0])
        else:
            pos = list(args)

        # Se último pos é string, interpretamos como identif
        identif = kwargs.get("identif", "")
        if len(pos) and isinstance(pos[-1], str):
            identif = pos.pop(-1)

        # Mapear posição por ordem esperada:
        # de, para, zser, ysa, ysb, eram, faseramo
        de = kwargs.get("de", None)
        para = kwargs.get("para", None)
        zser = kwargs.get("zser", None)
        ysa = kwargs.get("ysa", 0j)
        ysb = kwargs.get("ysb", 0j)
        eram = kwargs.get("eram", 0.0)
        faseramo = kwargs.get("faseramo", 0.0)
        extras = []

        # Atribuir valores a partir de argumentos posicionais
        order = ["de", "para", "zser", "ysa", "ysb", "eram", "faseramo"]
        for i, name in enumerate(order):
            if i < len(pos):
                val = pos[i]
                # Converter para o tipo apropriado
                if name in ("de", "para"):
                    val = int(val)
                elif name in ("zser", "ysa", "ysb"):
                    val = complex(val)
                else:
                    val = float(val)

                # Atualizar variáveis locais
                if name == "de":
                    de = val
                elif name == "para":
                    para = val
                elif name == "zser":
                    zser = val
                elif name == "ysa":
                    ysa = val
                elif name == "ysb":
                    ysb = val
                elif name == "eram":
                    eram = val
                elif name == "faseramo":
                    faseramo = val

        # Armazenar quaisquer argumentos posicionais extras
        if len(pos) > len(order):
            extras = pos[len(order):]

        # Verificar se parâmetros mínimos foram fornecidos
        if de is None or para is None or zser is None:
            raise ValueError(
                "Parâmetros mínimos de ramo: de, para, zser (ou passe uma sequência compatível).")

        # Criar dicionário do ramo e adicionar à lista
        ramo = {
            "de": int(de),
            "para": int(para),
            "zser": complex(zser),
            "ysa": complex(ysa),
            "ysb": complex(ysb),
            "eram": float(eram),
            "faseramo": float(faseramo),
            "identif": str(identif),
            "extras": extras
        }
        self.ramos.append(ramo)
        return self  # Retorna self para permitir chamadas encadeadas

    def calcular_matrizes_rede(self):
        """
        Calcula as matrizes de admitância nodal (Ybus) e impedância nodal (Zbus).

        Constrói a matriz Ybus com base nos parâmetros dos ramos do sistema e
        calcula a Zbus como a inversa da Ybus.

        **Retorno:**\n
        tuple: Uma tupla contendo:
            - Ybus (numpy.ndarray): Matriz de admitância de barra [nb x nb]
            - Zbus (numpy.ndarray): Matriz de impedância de barra [nb x nb]
            - Bi (numpy.ndarray): Vetor de barras de origem dos ramos [nr]
            - Bf (numpy.ndarray): Vetor de barras de destino dos ramos [nr]
            - Zser (numpy.ndarray): Vetor de impedâncias série dos ramos [nr]
            - Yser (numpy.ndarray): Vetor de admitâncias série dos ramos [nr]
            - Ysa (numpy.ndarray): Vetor de admitâncias shunt no início dos ramos [nr]
            - Ysb (numpy.ndarray): Vetor de admitâncias shunt no fim dos ramos [nr]
        """
        import numpy as np

        nb = self.nb
        nr = len(self.ramos)

        # Inicialização dos vetores
        Bi = np.zeros(nr, dtype=np.int64)
        Bf = np.zeros(nr, dtype=np.int64)
        Ysa = np.zeros(nr, dtype=complex)
        Ysb = np.zeros(nr, dtype=complex)
        Zser = np.zeros(nr, dtype=complex)
        Yser = np.zeros(nr, dtype=complex)
        Identif = [""] * nr
        Ybus = np.zeros((nb, nb), dtype=complex)

        # Preencher os arrays com os dados dos ramos
        for i, r in enumerate(self.ramos):
            Bi[i] = int(r["de"])
            Bf[i] = int(r["para"])
            Zser[i] = complex(r["zser"])
            Yser[i] = 1.0/Zser[i] if Zser[i] != 0 else 0
            Ysa[i] = complex(r.get("ysa", 0j))
            Ysb[i] = complex(r.get("ysb", 0j))
            Identif[i] = r.get("identif", "")

        # Montagem da matriz Ybus exatamente como no código original
        for j in range(nr):
            L = Bi[j]
            M = Bf[j]
            if (M != 0) and (L != 0):
                L = L - 1
                M = M - 1
                Ybus[L, L] = Ybus[L, L] + Yser[j] + Ysa[j]
                Ybus[M, M] = Ybus[M, M] + Yser[j] + Ysb[j]
                Ybus[L, M] = Ybus[L, M] - Yser[j]
                Ybus[M, L] = Ybus[M, L] - Yser[j]
            if (L == 0) and (M != 0):
                M = M - 1
                Ybus[M, M] = Ybus[M, M] + Yser[j] + Ysa[j]
            if (M == 0) and (L != 0):
                L = L - 1
                Ybus[L, L] = Ybus[L, L] + Yser[j] + Ysb[j]

        # Cálculo de Zbus
        Zbus = None
        try:
            Zbus = np.linalg.inv(Ybus)
        except np.linalg.LinAlgError:
            Zbus = None

        return Ybus, Zbus, Bi, Bf, Zser, Yser, Ysa, Ysb

    def calcular_parametros_rede(self):
        """
        Calcula os parâmetros elétricos da rede: correntes de injeção, 
        tensões nodais e correntes nos ramos.

        **Retorno:**\n
        tuple: Uma tupla contendo:
            - Isi (numpy.ndarray): Vetor de injeções de corrente nas barras [nb x 1]
            - Vsi (numpy.ndarray): Vetor de tensões nodais [nb x 1]
            - i_ramo (numpy.ndarray): Vetor de correntes nos ramos [nr x 1]
            - Eramo (numpy.ndarray): Vetor de módulos das tensões internas [nr]
            - Faseramo (numpy.ndarray): Vetor de ângulos das tensões internas em graus [nr]
            - Bi (numpy.ndarray): Vetor de barras de origem dos ramos [nr]
            - Bf (numpy.ndarray): Vetor de barras de destino dos ramos [nr]
            - Zser (numpy.ndarray): Vetor de impedâncias série dos ramos [nr]
        """
        import numpy as np
        from cmath import rect
        from math import radians

        nb = self.nb
        nr = len(self.ramos)

        Eramo = np.zeros(nr, dtype=float)
        Faseramo = np.zeros(nr, dtype=float)

        for i, r in enumerate(self.ramos):
            Eramo[i] = float(r.get("eram", 0.0))
            Faseramo[i] = float(r.get("faseramo", 0.0))

        # Obtém as matrizes da rede
        Ybus, Zbus, Bi, Bf, Zser, Yser, Ysa, Ysb = self.calcular_matrizes_rede()

        nb = self.nb
        nr = len(self.ramos)

        # Cálculo de Isi
        Isi = np.zeros((nb, 1), dtype=complex)
        for k in range(nr):
            if Bi[k] == 0:
                Isi[Bf[k]-1, 0] = rect(Eramo[k], radians(Faseramo[k]))/Zser[k]
            if Bf[k] == 0:
                Isi[Bi[k]-1, 0] = rect(Eramo[k], radians(Faseramo[k]))/Zser[k]

        # Cálculo de Vsi
        Vsi = np.zeros((nb, 1), dtype=complex)
        if Zbus is not None:
            Vsi = Zbus @ Isi

        # Cálculo das correntes nos ramos
        i_ramo = np.zeros((nr, 1), dtype=complex)
        for m in range(nr):
            a = Bf[m] - 1
            b = Bi[m] - 1
            if Bf[m] != 0 and Bi[m] != 0:
                i_ramo[m, 0] = (Vsi[b, 0] - Vsi[a, 0]) / Zser[m]
            elif Bi[m] == 0:
                i_ramo[m, 0] = (-Vsi[a, 0]) / Zser[m]
            elif Bf[m] == 0:
                i_ramo[m, 0] = Vsi[b, 0] / Zser[m]

        return Isi, Vsi, i_ramo, Eramo, Faseramo, Bi, Bf, Zser

    def obter_ramos(self):
        """
        Retorna um único dicionário consolidado com os dados de todos os ramos do sistema.

        O dicionário retornado possui como chaves os nomes dos parâmetros dos ramos 
        ('de', 'para', 'zser', etc.) e como valores listas contendo todos os valores 
        correspondentes de cada ramo, na ordem em que foram adicionados.

        **Retorno:**\n
        dict: Dicionário com as seguintes chaves, cada uma contendo uma lista de valores:
        - 'de': barras de origem
        - 'para': barras de destino
        - 'zser': impedâncias série
        - 'ysa': admitâncias shunt no início dos ramos
        - 'ysb': admitâncias shunt no fim dos ramos
        - 'eram': módulos das tensões internas (fontes)
        - 'faseramo': ângulos das tensões internas em graus
        - 'identif': identificadores dos ramos
        - 'extras': listas de valores extras fornecidos
        """
        # Inicializa o dicionário com listas vazias para cada chave
        ramos_dict = {
            'de': [], 'para': [], 'zser': [], 'ysa': [], 'ysb': [],
            'eram': [], 'faseramo': [], 'identif': [], 'extras': []
        }

        # Preenche as listas com os valores de cada ramo
        for ramo in self.ramos:
            for key in ramos_dict:
                ramos_dict[key].append(ramo[key])

        return ramos_dict

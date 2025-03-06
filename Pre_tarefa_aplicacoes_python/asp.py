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


def imp_serie(Z1, Z2):
    """
    # Calcula a impedância equivalente de dois elementos em série.

    **Parâmetros:**\n
    Z1 (a + jb): A primeira impedância.\n
    Z2 (a + jb): A segunda impedância.

    **Retorno:**\n
    A impedância equivalente dos dois elementos em série. (a + jb)
    """
    return Z1 + Z2


def imp_paral(Z1, Z2):
    """
    # Calcula a impedância equivalente de dois elementos em paralelo.

    **Parâmetros:**\n
    Z1 (a + jb): A primeira impedância.\n
    Z2 (a + jb): A segunda impedância.

    **Retorno:**\n
    A impedância equivalente dos dois elementos em paralelo. (a + jb)
    """
    return (Z1 * Z2) / (Z1 + Z2)


def oper_comp(Z1, form1, op, Z2, form2):
    """
    # Realiza operações com números complexos.

    **Parâmetros:**\n
    Z1 (complex): O primeiro número complexo.\n
    form1 (str): A forma do primeiro número complexo ("r: retangular" ou "p: polar, em radianos").\n
    op (str): O operador a ser aplicado ("+", "-", "*", "/").\n
    Z2 (complex): O segundo número complexo.\n
    form2 (str): A forma do segundo número complexo ("r: retangular" ou "p: polar", em radianos).

    **Retorno:**\n
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


def format_complex(c, form='r'):
    """
    # Formata um número complexo em uma string legível.

    **Parâmetros:**\n
    c (complex): O número complexo a ser formatado.\n
    form (str): A forma do número complexo ('r' para retangular, 'p' para polar). Padrão é 'r'.\n

    **Retorno:**\n
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
        parte_real = f'{c.real:.2f}' if c.real != 0 else ''
        parte_imaginaria = f'{abs(c.imag):.2f}j' if c.imag != 0 else ''
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
        return f'{r:.2f} ∠ {theta:.2f}°'
    else:
        raise ValueError(
            "Forma inválida. Use 'r' para retangular ou 'p' para polar.")


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

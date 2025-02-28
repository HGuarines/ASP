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


def ret2pol(cplx):
    """
    # Converte um número complexo retangular para forma polar.

    Parâmetros:
    cplx (complex): O número complexo a ser convertido. (a + jb)

    Retorno:
    Uma tupla contendo o módulo e o argumento do número complexo fornecido. (r, phi)
    """
    from cmath import polar
    return polar(cplx)


def pol2ret(r, phi):
    """
    # Converte um número complexo polar para forma retangular.

    Parâmetros:
    r (float): O módulo do número complexo.\n
    phi (float): O argumento do número complexo em graus.

    Retorno:
    O número complexo na forma retangular. (a + jb)
    """
    from cmath import rect
    from numpy import radians
    phi_rad = radians(phi)
    return rect(r, phi_rad)


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
        raise ValueError("O número de fases deve ser 1 (monofásico) ou 3 (trifásico).")

    return I

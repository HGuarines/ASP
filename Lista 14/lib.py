
# by perrier


def resistência_corrigida(r0, t0, t1):
    """
    Calcula a resistência corrigida pela temperatura para um condutor.

    Parâmetros:
    -----------
    r0 : float
        Resistência do condutor na temperatura t0 (Ω/km)
    t0 : inteiro
        Temperatura na qual se sabe a resistência do condutor (C°)
    t1 : inteiro
        Temperatura na qual se deseja saber a resistência do condutor (C°)
    Retorna:
    --------
    r1 : float
        Resistência do condutor corrigida para a temperatura t1 (Ω/km)
    """

    r1 = r0 * (228 + t1)/(228 + t0)

    return r1


def resistencia_corrigida_dict(t1, dicionario):
    """
    Versão com tratamento de erros para casos onde as chaves podem não existir.

    Parâmetros:
    -----------
    t1 : inteiro
        Temperatura na qual se deseja saber a resistência do condutor (C°)
    dicionario : dict
        Dicionário contendo as chaves 'r0' e 't0'

    Retorna:
    --------
    r1 : float ou None
        Resistência do condutor corrigida para a temperatura t1 (Ω/km)
        Retorna None se as chaves necessárias não forem encontradas
    """

    try:
        # Verifica se as chaves existem no dicionário
        if 'r0' not in dicionario or 't0' not in dicionario:
            raise KeyError(
                "Chaves 'r0' e/ou 't0' não encontradas no dicionário")

        # Verifica se as listas não estão vazias
        if not dicionario['r0'] or not dicionario['t0']:
            raise ValueError("Listas 'r0' e/ou 't0' estão vazias")

        # Extrai r0 e t0 do dicionário
        r0 = dicionario['r0'][0]
        t0 = dicionario['t0'][0]

        # Calcula a resistência corrigida
        r1 = r0 * (228 + t1) / (228 + t0)

        return r1

    except (KeyError, ValueError, IndexError) as e:
        print(f"Erro: {e}")
        return None


def calcular_impedancias_proprias_mutuas_CI(ra, rb, rc, Dab, Dac, Dbc, Ds, ha, hb, hc, f=60):
    """
    Calcula as impedâncias próprias e mútuas usando a fórmula de Carson.

    Parâmetros:
    -----------
    ra, rb, rc : float
        Resistências dos condutores das fases A, B, C (Ω/km)
    Dab, Dac, Dbc : float
        Distâncias entre fases (m)
    Ds : float
        Raio médio geométrico do condutor (m)
    ha, hb, hc : float
         Distância dos condutores das fases A, B, C ao solo (m)
    f : float
        Frequência (Hz)
    rho : float
        Resistividade do solo (Ω·m)
    mu_r : float
        Permeabilidade relativa do solo

    Retorna:
    --------
    tuple : (Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc)
    """
    import numpy as np
    mu_0 = 4 * np.pi * 1e-7 * (1/1000)

    # Termo de correção de Carson para impedância própria

    def Z_propria(r, Ds, h):
        X = 1j * f * mu_0 * np.log(2*h/Ds)
        return r + X

    # Termo de correção de Carson para impedância mútua
    def Z_mutua(dij, h):
        Dij = np.sqrt(dij**2 + h**2)
        X = 1j * f * mu_0 * np.log(Dij/dij)
        return X

    Z_aa = Z_propria(ra, Ds, ha)
    Z_bb = Z_propria(rb, Ds, hb)
    Z_cc = Z_propria(rc, Ds, hc)

    Z_ab = Z_mutua(Dab, ha)
    Z_ac = Z_mutua(Dac, hb)
    Z_bc = Z_mutua(Dbc, hc)

    return Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc


def calcular_impedancias_proprias_mutuas(ra, rb, rc, Dab, Dac, Dbc, Ds, f=60):
    """
    Calcula as impedâncias próprias e mútuas usando a fórmula de Carson.

    Parâmetros:
    -----------
    ra, rb, rc : float
        Resistências dos condutores das fases A, B, C (Ω/km)
    Dab, Dac, Dbc : float
        Distâncias entre fases (m)
    Ds : float
        Raio médio geométrico do condutor (m)
    f : float
        Frequência (Hz)
    rho : float
        Resistividade do solo (Ω·m)

    Retorna:
    --------
    tuple : (Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc)
    """

    k = 2 * 1e-7

    # Termo de correção de Carson para impedância própria

    def Z_propria(r, Ds):
        X = 1j * k * np.log(1/Ds)
        return r + X

    # Termo de correção de Carson para impedância mútua
    def Z_mutua(Dij):
        X = 1j * k * np.log(1/Dij)
        return X

    Z_aa = Z_propria(ra, Ds)
    Z_bb = Z_propria(rb, Ds)
    Z_cc = Z_propria(rc, Ds)

    Z_ab = Z_mutua(Dab)
    Z_ac = Z_mutua(Dac)
    Z_bc = Z_mutua(Dbc)

    return Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc


def impedância_fase(Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc):
    """
    Calcula a impedância de cada fase de uma LT.

    Parâmetros:
    -----------
    Z_aa, Z_bb, Z_cc : complex
        Impedâncias próprias das fases A, B e C (Ω/km)
    Z_ab, Z_ac, Z_bc : complex
        Impedâncias mútuas entre as fases (Ω/km)

    Retorna:
    --------
    Z_a, Z_b, Z_c : complex
        Impedâncias das fases (Ω/km)
    """
    Z_a = Z_aa - (Z_ab + Z_ac)/2
    Z_b = Z_bb - (Z_ab + Z_bc)/2
    Z_c = Z_cc - (Z_ac + Z_bc)/2

    return Z_a, Z_b, Z_c


def impedancia_servico_linha_trifasica(Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc):
    """
    Calcula a matriz de impedância de serviço para uma linha trifásica não transposta.

    Parâmetros:
    -----------
    Z_aa, Z_bb, Z_cc : complex
        Impedâncias próprias das fases A, B e C (Ω/km)
    Z_ab, Z_ac, Z_bc : complex
        Impedâncias mútuas entre as fases (Ω/km)

    Retorna:
    --------
    Z_servico : numpy.ndarray
        Matriz 3x3 complexa com a impedância de serviço (Ω/km)
    """

    # Construindo a matriz de impedância primitiva
    Z_primitive = np.array([
        [Z_aa, Z_ab, Z_ac],
        [Z_ab, Z_bb, Z_bc],
        [Z_ac, Z_bc, Z_cc]
    ], dtype=complex)

    # Para linhas sem cabos para-raios, a matriz de impedância de serviço
    # é igual à matriz de impedância primitiva
    Z_servico_array = Z_primitive
    Z_serviço = (Z_aa + Z_bb + Z_cc - Z_ab - Z_ac - Z_bc)/3

    return Z_servico_array, Z_serviço


def altura_efetiva_flecha(h, flecha):
    h_efetiva = h - (2/3)*flecha
    return h_efetiva


def resistencia_feixe(r, numero_de_condutores_no_feixe):
    r_efetiva = r/numero_de_condutores_no_feixe
    return r_efetiva


def RMG_feixe_resumido(RMG, numero_de_condutores_no_feixe, dis_cond_feixe):
    for i in range(numero_de_condutores_no_feixe):
        for j in range(numero_de_condutores_no_feixe):
            if i == j:
                dij = RMG
            elif i:
                dij = dis_cond_feixe

# Função alternativa que trata melhor os dados numéricos


def csv_para_dicionario_numerico(arquivo_csv, delimiter=';', encoding='utf-8'):
    """
    Versão que converte automaticamente valores numéricos para float/int.
    """
    import csv
    dados = {}

    try:
        with open(arquivo_csv, 'r', encoding=encoding) as arquivo:
            leitor = csv.reader(arquivo, delimiter=delimiter)

            for linha in leitor:
                # Remove elementos vazios da linha
                linha = [item.strip() for item in linha if item.strip()]

                if len(linha) > 0:
                    chave = linha[0]
                    valores = []

                    for item in linha[1:]:
                        # Tenta converter para número, mantém string se não for possível
                        try:
                            # Tenta converter para float
                            valor = float(item)
                            # Se for inteiro, converte para int
                            if valor.is_integer():
                                valor = int(valor)
                            valores.append(valor)
                        except ValueError:
                            valores.append(item)

                    dados[chave] = valores

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_csv}' não encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return {}

    return dados


def distancia(X1, Y1, X2, Y2):
    import numpy as np
    return np.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)


def matrix_Zlt(r, dados):
    """
    Calcula a matriz ZLT para linhas de transmissão.

    Parâmetros:
    -----------
    Xc, Yc : list
        Coordenadas dos condutores
    r : float
        Resistência
    RWG : float
        Raio do condutor
    lc : float
        Comprimento (ou constante) não especificada

    Retorna:
    --------
    ZLT : matrix
        Matriz de impedância
    """
    import numpy as np
    Xc = dados['X']
    Yc = dados['Y']
    RWG = dados['RMG'][0]

    print

    ZLT = np.zeros((3, 3), dtype=complex)

    for i in range(3):
        for j in range(3):

            if j == i:
                # Elementos da diagonal
                d = distancia(Xc[i], Yc[i], Xc[i], -Yc[i])
                ZLT[i][j] = r + 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(d / RWG)

            else:
                # Elementos fora da diagonal
                di = distancia(Xc[i], Yc[i], Xc[j], Yc[j])
                dii = distancia(Xc[i], Yc[i], Xc[j], -Yc[j])
                ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(dii / di)

    titulo = '    Matrix ZLT'
    print(titulo)

    # Imprime a matriz formatada
    for i in range(3):
        for j in range(3):
            R = np.real(ZLT[i][j])
            X = np.imag(ZLT[i][j])
            A = i + 1
            B = j + 1
            if X >= 0.0:
                print('    ZLT(%id,%id) - %8.4f + %8.4fj ' % (A, B, R, X))
            else:
                print('    ZLT(%id,%id) - %8.4f - %8.4fj ' % (A, B, R, abs(X)))

    linha = 48 * '*'
    print(linha)
    return ZLT


def matrix_Zlt_sem_CI(r, dados):
    """
    Calcula a matriz ZLT para linhas de transmissão.

    Parâmetros:
    -----------
    Xc, Yc : list
        Coordenadas dos condutores
    r : float
        Resistência
    RWG : float
        Raio do condutor
    lc : float
        Comprimento (ou constante) não especificada

    Retorna:
    --------
    ZLT : matrix
        Matriz de impedância
    """
    import numpy as np
    Xc = dados['X']
    Yc = dados['Y']
    RWG = dados['RMG'][0]

    print

    ZLT = np.zeros((3, 3), dtype=complex)

    for i in range(3):
        for j in range(3):

            if j == i:
                # Elementos da diagonal
                ZLT[i][j] = r + 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(1 / RWG)

            else:
                # Elementos fora da diagonal
                di = distancia(Xc[i], Yc[i], Xc[j], Yc[j])
                ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(1 / di)

    titulo = '    Matrix ZLT SEM CI'
    print(titulo)

    # Imprime a matriz formatada
    for i in range(3):
        for j in range(3):
            R = np.real(ZLT[i][j])
            X = np.imag(ZLT[i][j])
            A = i + 1
            B = j + 1
            if X >= 0.0:
                print('    ZLT(%id,%id) - %8.4f + %8.4fj ' % (A, B, R, X))
            else:
                print('    ZLT(%id,%id) - %8.4f - %8.4fj ' % (A, B, R, abs(X)))

    linha = 48 * '*'
    print(linha)
    return ZLT


def Zserv(ZLT):
    """
    Calcula a impedância de serviço a partir da matriz ZLT.

    Parâmetros:
    -----------
    ZLT : list
        Matriz 3x3 de impedâncias

    Retorna:
    --------
    Zs : complex
        Impedância de serviço média
    """
    # Cálculo das impedâncias de sequência
    Za = ZLT[0][0] - (1/2) * (ZLT[0][1] + ZLT[0][2])
    print(ZLT[0][0], ZLT[0][1], ZLT[0][2])
    Zb = ZLT[1][1] - (1/2) * (ZLT[1][0] + ZLT[1][2])
    print(ZLT[1][1], ZLT[1][2], ZLT[1][2])
    Zc = ZLT[2][2] - (1/2) * (ZLT[2][0] + ZLT[2][1])
    print(ZLT[2][2], ZLT[2][0], ZLT[2][1])
    # Impedância de serviço média
    Zs = (Za + Zb + Zc) / 3

    return Zs, Za, Zb, Zc

# By Guarines


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
        conteudo_adicionar.append(
            f'{" " * 10}GRUPO TAREFA 14\nHenrique B Guarines\nLucas Brito\nVitor Perrier{" " * 20}\n')
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

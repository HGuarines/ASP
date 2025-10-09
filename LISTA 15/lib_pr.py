import numpy as np
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
        r0 = dicionario['r0']
        t0 = dicionario['t0']
        r1 = np.zeros((len(r0)), dtype=float)
        # Calcula a resistência corrigida
        for i in range(len(dicionario['r0'])):
            r1[i] = r0[i] * (228 + t1) / (228 + t0[i])
        return r1

    except (KeyError, ValueError, IndexError) as e:
        print(f"Erro: {e}")
        return None


def altura_efetiva_flecha(h, flecha):
    h_efetiva = h - (2/3)*flecha
    return h_efetiva


def ajuste_altura(dicionario):
    flecha = dicionario['Flecha'][0]

    for i in range(len(dicionario['Y'])):
        h = dicionario['Y'][i]
        dicionario['Y'][i] = altura_efetiva_flecha(h, flecha)
    retorno = dicionario['Y']
    return retorno


def resistencia_feixe(dicionario, r, inicio):
    nc = dicionario['Num_cond_feixe'][inicio]
    if nc < 2:
        return r
    else:
        return r / nc


def rmg_feixe(dicionario, inicio, posicao_nc):
    """
    Calcula o Raio Médio Geométrico (RMG) de um feixe de condutores.

    Args:
        nc (int): Número de condutores no feixe.
        RMG (float): RMG de um condutor individual.
        Xc (list): Coordenadas X dos subcondutores.
        Yc (list): Coordenadas Y dos subcondutores.

    Returns:
        float: O RMG equivalente do feixe.
    """

    nc = dicionario['Num_cond_feixe'][posicao_nc]
    RMG = dicionario['RMG'][inicio]
    Xc = dicionario['X']
    Yc = dicionario['Y']

    A = RMG**nc
    for i in range(nc):
        for j in range(nc):
            if i != j:
                A = A * distancia(Xc[i+posicao_nc], Yc[i+posicao_nc],
                                  Xc[j+posicao_nc], Yc[j+posicao_nc])
    RMGF = (A*(1 / (nc*2)))

    return RMGF


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
    RWG = dados['RMG']

    ZLT = np.zeros((len(Xc), len(Xc)), dtype=complex)

    for i in range(len(Xc)):
        for j in range(len(Xc)):

            if j == i:
                # Elementos da diagonal
                d = distancia(Xc[i], Yc[i], Xc[i], -Yc[i])
                ZLT[i][j] = r[i] + 1j * 4 * np.pi * \
                    1e-4 * 60.0 * np.log(d / RWG[i])

            else:
                # Elementos fora da diagonal
                di = distancia(Xc[i], Yc[i], Xc[j], Yc[j])
                dii = distancia(Xc[i], Yc[i], Xc[j], -Yc[j])
                ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(dii / di)

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
    RWG = dados['RMG']
    print

    ZLT = np.zeros((len(Xc), len(Xc)), dtype=complex)

    for i in range(len(Xc)):
        for j in range(len(Xc)):

            if j == i:
                # Elementos da diagonal
                ZLT[i][j] = r[i] + 1j * 4 * np.pi * \
                    1e-4 * 60.0 * np.log(1 / RWG[i])

            else:
                # Elementos fora da diagonal
                di = distancia(Xc[i], Yc[i], Xc[j], Yc[j])
                ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * 60.0 * np.log(1 / di)

    titulo = '    Matrix ZLT SEM CI'
    print(titulo)

    # Imprime a matriz formatada
    for i in range(len(Xc)):
        for j in range(len(Xc)):
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


def criar_submatrizes(matriz):
    """Cria as 4 submatrizes a partir da matriz 5x5"""
    # Matriz 3x3 - 3 primeiras linhas e 3 primeiras colunas
    matriz1 = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(matriz[i][j])
        matriz1.append(linha)

    # Matriz 3x2 - 3 primeiras linhas e 2 últimas colunas
    matriz2 = []
    for i in range(3):
        linha = []
        for j in range(3, 5):  # colunas 3 e 4 (índices 3 e 4)
            linha.append(matriz[i][j])
        matriz2.append(linha)

    # Matriz 2x3 - 2 últimas linhas e 3 primeiras colunas
    matriz3 = []
    for i in range(3, 5):  # linhas 3 e 4 (índices 3 e 4)
        linha = []
        for j in range(3):
            linha.append(matriz[i][j])
        matriz3.append(linha)

    # Matriz 2x2 - 2 últimas linhas e 2 últimas colunas
    matriz4 = []
    for i in range(3, 5):  # linhas 3 e 4
        linha = []
        for j in range(3, 5):  # colunas 3 e 4
            linha.append(matriz[i][j])
        matriz4.append(linha)

    return matriz1, matriz2, matriz3, matriz4


def imprimir_matriz(matriz, nome):
    """Imprime uma matriz formatada"""
    print(f"\n{nome}:")
    for linha in matriz:
        print("[" + " ".join(f"{elem:6.4f}" for elem in linha) + "]")


def matriz_impedancia_reduzida_da_5x5(ZLT):

    Zabc, Zabcrs, Zrsabc, Zrs = criar_submatrizes(ZLT)

    Zabccp = Zabc - Zabcrs @ np.linalg.inv(Zrs) @ Zrsabc

    Zs, Za, Zb, Zc = Zserv(Zabccp)

    return Zs, Za, Zb, Zc, Zabccp


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
            f'{" " * 10}Vitor Perrier{" " * 20}\n')
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

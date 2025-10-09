import numpy as np


class ParametrosLinha:
    """
    Classe para cálculo de parâmetros de linhas de transmissão.

    Attributes:
        dados (dict): Dicionário contendo todos os parâmetros da linha
        frequencia (float): Frequência do sistema (Hz)
        mu_0 (float): Permeabilidade magnética do vácuo
        k (float): Constante de Carson simplificada
    """

    def __init__(self, dados):
        """
        Inicializa a classe com os dados da linha.

        Parameters:
            dados (dict): Dicionário contendo parâmetros da linha
        """
        self.dados = dados
        self.frequencia = dados.get('frequencia', [60])[0]
        self.mu_0 = 4 * np.pi * 1e-7 * (1/1000)  # H/km
        self.k = 2 * 1e-7  # Constante de Carson simplificada

    def resistencia_corrigida(self, r0, t0, t1):
        """
        Calcula a resistência corrigida pela temperatura para um condutor.

        Parameters:
            r0 (float): Resistência do condutor na temperatura t0 (Ω/km)
            t0 (int): Temperatura de referência (°C)
            t1 (int): Temperatura desejada (°C)

        Returns:
            float: Resistência corrigida para a temperatura t1 (Ω/km)
        """
        r1 = r0 * (228 + t1) / (228 + t0)
        return r1

    def resistencia_corrigida_dict(self, t1):
        """
        Calcula a resistência corrigida usando dados do dicionário interno.
        Agora suporta múltiplas resistências e temperaturas.

        Parameters:
            t1 (int): Temperatura desejada (°C)

        Returns:
            numpy.ndarray or None: Array com resistências corrigidas ou None em caso de erro
        """
        try:
            if 'r0' not in self.dados or 't0' not in self.dados:
                raise KeyError(
                    "Chaves 'r0' e/ou 't0' não encontradas no dicionário")

            if not self.dados['r0'] or not self.dados['t0']:
                raise ValueError("Listas 'r0' e/ou 't0' estão vazias")

            # Pega listas completas
            r0 = self.dados['r0']
            t0 = self.dados['t0']
            r1 = np.zeros((len(r0)), dtype=float)

            # Calcula a resistência corrigida para cada elemento
            for i in range(len(self.dados['r0'])):
                r1[i] = r0[i] * (228 + t1) / (228 + t0[i])

            return r1

        except (KeyError, ValueError, IndexError) as e:
            print(f"Erro: {e}")
            return None

    def altura_efetiva_flecha(self, h, flecha):
        """
        Calcula a altura efetiva considerando a flecha do condutor.

        Parameters:
            h (float): Altura do condutor (m)
            flecha (float): Flecha do condutor (m)

        Returns:
            float: Altura efetiva (m)
        """
        h_efetiva = h - (2/3) * flecha
        return h_efetiva

    def ajuste_altura(self):
        """
        Ajusta as alturas dos condutores considerando a flecha.
        Modifica o dicionário interno de dados e retorna as alturas ajustadas.

        Returns:
            list: Lista com alturas ajustadas
        """
        flecha = self.dados['Flecha'][0]
        for i in range(len(self.dados['Y'])):
            h = self.dados['Y'][i]
            self.dados['Y'][i] = self.altura_efetiva_flecha(h, flecha)
        retorno = self.dados['Y']
        return retorno

    def resistencia_feixe(self, r, inicio):
        """
        Calcula a resistência efetiva de um feixe de condutores.
        Agora com verificação se é realmente um feixe.

        Parameters:
            r (float): Resistência de um condutor (Ω/km)
            inicio (int): Índice do condutor no dicionário

        Returns:
            float: Resistência efetiva do feixe (Ω/km)
        """
        nc = self.dados['Num_cond_feixe'][inicio]
        if nc < 2:
            return r
        else:
            return r / nc

    def rmg_feixe(self, inicio, posicao_nc):
        """
        Calcula o Raio Médio Geométrico (RMG) de um feixe de condutores.

        Parameters:
            inicio (int): Índice inicial do RMG no dicionário
            posicao_nc (int): Posição do número de condutores no feixe

        Returns:
            float: RMG equivalente do feixe (m)
        """
        nc = self.dados['Num_cond_feixe'][posicao_nc]
        RMG = self.dados['RMG'][inicio]
        Xc = self.dados['X']
        Yc = self.dados['Y']

        A = RMG**nc
        for i in range(nc):
            for j in range(nc):
                if i != j:
                    A = A * self.distancia(Xc[i+posicao_nc], Yc[i+posicao_nc],
                                           Xc[j+posicao_nc], Yc[j+posicao_nc])
        RMGF = A**(1 / (nc*2))

        return RMGF

    @staticmethod
    def distancia(X1, Y1, X2, Y2):
        """
        Calcula a distância euclidiana entre dois pontos.

        Parameters:
            X1, Y1 (float): Coordenadas do ponto 1
            X2, Y2 (float): Coordenadas do ponto 2

        Returns:
            float: Distância entre os pontos
        """
        return np.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)

    def calcular_impedancias_proprias_mutuas(self, ra, rb, rc, Dab, Dac, Dbc, Ds):
        """
        Calcula impedâncias próprias e mútuas (sem condutor imagem).

        Parameters:
            ra, rb, rc (float): Resistências das fases A, B, C (Ω/km)
            Dab, Dac, Dbc (float): Distâncias entre fases (m)
            Ds (float): Raio médio geométrico do condutor (m)

        Returns:
            tuple: (Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc)
        """
        def Z_propria(r, Ds):
            X = 1j * self.k * np.log(1/Ds)
            return r + X

        def Z_mutua(Dij):
            X = 1j * self.k * np.log(1/Dij)
            return X

        Z_aa = Z_propria(ra, Ds)
        Z_bb = Z_propria(rb, Ds)
        Z_cc = Z_propria(rc, Ds)
        Z_ab = Z_mutua(Dab)
        Z_ac = Z_mutua(Dac)
        Z_bc = Z_mutua(Dbc)

        return Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc

    def calcular_impedancias_proprias_mutuas_CI(self, ra, rb, rc, Dab, Dac, Dbc,
                                                Ds, ha, hb, hc):
        """
        Calcula impedâncias próprias e mútuas com condutor imagem (Carson).

        Parameters:
            ra, rb, rc (float): Resistências das fases A, B, C (Ω/km)
            Dab, Dac, Dbc (float): Distâncias entre fases (m)
            Ds (float): Raio médio geométrico do condutor (m)
            ha, hb, hc (float): Alturas dos condutores A, B, C (m)

        Returns:
            tuple: (Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc)
        """
        def Z_propria(r, Ds, h):
            X = 1j * self.frequencia * self.mu_0 * np.log(2*h/Ds)
            return r + X

        def Z_mutua(dij, h):
            Dij = np.sqrt(dij**2 + h**2)
            X = 1j * self.frequencia * self.mu_0 * np.log(Dij/dij)
            return X

        Z_aa = Z_propria(ra, Ds, ha)
        Z_bb = Z_propria(rb, Ds, hb)
        Z_cc = Z_propria(rc, Ds, hc)
        Z_ab = Z_mutua(Dab, ha)
        Z_ac = Z_mutua(Dac, hb)
        Z_bc = Z_mutua(Dbc, hc)

        return Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc

    def matrix_Zlt(self, r, com_condutor_imagem=True):
        """
        Calcula a matriz ZLT para linhas de transmissão.
        ATUALIZADO: Agora com tamanho dinâmico e suporte a múltiplos condutores.

        Parameters:
            r (numpy.ndarray or list): Array com resistências dos condutores (Ω/km)
            com_condutor_imagem (bool): Se True, usa condutor imagem

        Returns:
            numpy.ndarray: Matriz NxN de impedâncias (N = número de condutores)
        """
        Xc = self.dados['X']
        Yc = self.dados['Y']
        RMG = self.dados['RMG']

        # Tamanho dinâmico baseado no número de condutores
        ZLT = np.zeros((len(Xc), len(Xc)), dtype=complex)

        for i in range(len(Xc)):
            for j in range(len(Xc)):
                if j == i:
                    # Elementos da diagonal
                    if com_condutor_imagem:
                        d = self.distancia(Xc[i], Yc[i], Xc[i], -Yc[i])
                        ZLT[i][j] = r[i] + 1j * 4 * np.pi * 1e-4 * \
                            self.frequencia * np.log(d / RMG[i])
                    else:
                        ZLT[i][j] = r[i] + 1j * 4 * np.pi * 1e-4 * \
                            self.frequencia * np.log(1 / RMG[i])
                else:
                    # Elementos fora da diagonal
                    di = self.distancia(Xc[i], Yc[i], Xc[j], Yc[j])
                    if com_condutor_imagem:
                        dii = self.distancia(Xc[i], Yc[i], Xc[j], -Yc[j])
                        ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * \
                            self.frequencia * np.log(dii / di)
                    else:
                        ZLT[i][j] = 1j * 4 * np.pi * 1e-4 * \
                            self.frequencia * np.log(1 / di)

        return ZLT

    def imprimir_matriz_Zlt(self, ZLT, com_condutor_imagem=True):
        """
        Imprime a matriz ZLT formatada.
        ATUALIZADO: Agora funciona com matrizes de qualquer tamanho.

        Parameters:
            ZLT (numpy.ndarray): Matriz de impedâncias
            com_condutor_imagem (bool): Indica se foi calculada com CI
        """
        titulo = 'Matrix ZLT' if com_condutor_imagem else 'Matrix ZLT SEM CI'
        print(f'    {titulo}')

        n = ZLT.shape[0]  # Tamanho dinâmico
        for i in range(n):
            for j in range(n):
                R = np.real(ZLT[i][j])
                X = np.imag(ZLT[i][j])
                A = i + 1
                B = j + 1
                if X >= 0.0:
                    print(f'    ZLT({A}d,{B}d) - {R:8.4f} + {X:8.4f}j ')
                else:
                    print(f'    ZLT({A}d,{B}d) - {R:8.4f} - {abs(X):8.4f}j ')

        print(48 * '*')

    @staticmethod
    def imprimir_matriz(matriz, nome):
        """
        Imprime uma matriz formatada com nome.

        Parameters:
            matriz (numpy.ndarray or list): Matriz a ser impressa
            nome (str): Nome da matriz
        """
        print(f"\n{nome}:")
        if isinstance(matriz, np.ndarray):
            for linha in matriz:
                print("[" + " ".join(f"{elem:6.4f}" for elem in linha) + "]")
        else:
            for linha in matriz:
                print("[" + " ".join(f"{elem:6.4f}" for elem in linha) + "]")

    @staticmethod
    def criar_submatrizes(matriz):
        """
        Cria as 4 submatrizes a partir da matriz 5x5.
        Usada para redução de Kron quando há cabos para-raios.

        Parameters:
            matriz (numpy.ndarray): Matriz 5x5 completa

        Returns:
            tuple: (matriz1, matriz2, matriz3, matriz4)
                   - matriz1: 3x3 (fases)
                   - matriz2: 3x2 (acoplamento fases-cabos)
                   - matriz3: 2x3 (acoplamento cabos-fases)
                   - matriz4: 2x2 (cabos para-raios)
        """
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

    def matriz_impedancia_reduzida_da_5x5(self, ZLT):
        """
        Aplica redução de Kron para eliminar os cabos para-raios.
        Transforma matriz 5x5 em 3x3 equivalente.

        Parameters:
            ZLT (numpy.ndarray): Matriz 5x5 completa

        Returns:
            tuple: (Zs, Za, Zb, Zc, Zabccp)
                   - Zs: Impedância de serviço média
                   - Za, Zb, Zc: Impedâncias por fase
                   - Zabccp: Matriz 3x3 reduzida
        """
        Zabc, Zabcrs, Zrsabc, Zrs = self.criar_submatrizes(ZLT)

        # Redução de Kron: Z' = Zabc - Zabcrs·Zrs⁻¹·Zrsabc
        Zabccp = np.array(
            Zabc) - np.array(Zabcrs) @ np.linalg.inv(np.array(Zrs)) @ np.array(Zrsabc)

        Zs, Za, Zb, Zc = self.Zserv(Zabccp)

        return Zs, Za, Zb, Zc, Zabccp

    def impedancia_fase(self, Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc):
        """
        Calcula a impedância de cada fase.

        Parameters:
            Z_aa, Z_bb, Z_cc (complex): Impedâncias próprias (Ω/km)
            Z_ab, Z_ac, Z_bc (complex): Impedâncias mútuas (Ω/km)

        Returns:
            tuple: (Z_a, Z_b, Z_c)
        """
        Z_a = Z_aa - (Z_ab + Z_ac) / 2
        Z_b = Z_bb - (Z_ab + Z_bc) / 2
        Z_c = Z_cc - (Z_ac + Z_bc) / 2

        return Z_a, Z_b, Z_c

    def Zserv(self, ZLT):
        """
        Calcula a impedância de serviço a partir da matriz ZLT.

        Parameters:
            ZLT (numpy.ndarray or list): Matriz 3x3 de impedâncias

        Returns:
            tuple: (Zs, Za, Zb, Zc)
                   - Zs: Impedância de serviço média
                   - Za, Zb, Zc: Impedâncias por fase
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

    def impedancia_servico_linha_trifasica(self, Z_aa, Z_bb, Z_cc, Z_ab, Z_ac, Z_bc):
        """
        Calcula a matriz de impedância de serviço para linha trifásica não transposta.

        Parameters:
            Z_aa, Z_bb, Z_cc (complex): Impedâncias próprias (Ω/km)
            Z_ab, Z_ac, Z_bc (complex): Impedâncias mútuas (Ω/km)

        Returns:
            tuple: (Z_servico_array, Z_servico) - matriz e valor médio
        """
        Z_primitive = np.array([
            [Z_aa, Z_ab, Z_ac],
            [Z_ab, Z_bb, Z_bc],
            [Z_ac, Z_bc, Z_cc]
        ], dtype=complex)

        Z_servico_array = Z_primitive
        Z_servico = (Z_aa + Z_bb + Z_cc - Z_ab - Z_ac - Z_bc) / 3

        return Z_servico_array, Z_servico


# Função auxiliar para leitura de CSV (mantida fora da classe)
def csv_para_dicionario_numerico(arquivo_csv, delimiter=';', encoding='utf-8'):
    """
    Converte arquivo CSV para dicionário com valores numéricos.

    Parameters:
        arquivo_csv (str): Caminho do arquivo CSV
        delimiter (str): Delimitador usado no CSV
        encoding (str): Codificação do arquivo

    Returns:
        dict: Dicionário com os dados do arquivo
    """
    import csv
    dados = {}

    try:
        with open(arquivo_csv, 'r', encoding=encoding) as arquivo:
            leitor = csv.reader(arquivo, delimiter=delimiter)
            for linha in leitor:
                linha = [item.strip() for item in linha if item.strip()]
                if len(linha) > 0:
                    chave = linha[0]
                    valores = []
                    for item in linha[1:]:
                        try:
                            valor = float(item)
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

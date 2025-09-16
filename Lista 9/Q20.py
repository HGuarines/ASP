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

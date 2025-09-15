# Definição da classe com adicionar_ramo flexível e cálculo de Ybus/Zbus/Isi/Vsi
import numpy as np
from cmath import rect
from math import radians


class SistemaEletrico:
    def __init__(self, num_barras):
        self.nb = int(num_barras)
        if self.nb < 0:
            raise ValueError("Número de barras deve ser >= 0")
        self.ramos = []

    def adicionar_ramo(self, *args, **kwargs):
        """
        Aceita chamadas flexíveis:
        - adicionar_ramo(de, para, zser, ysa=0j, ysb=0j, eram=0.0, faseramo=0.0, identif="")
        - ou passar muitos posicionais; se último for str considera como identif.
        - se for passado um único argumento iterável (lista/tuple) considera como a linha inteira.
        Extras posicionais (além dos esperados) são simplesmente armazenados em 'extras'.
        """
        # Se passou um único iterable (lista/tuple), desenpacotamos
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
        # assign from pos
        order = ["de", "para", "zser", "ysa", "ysb", "eram", "faseramo"]
        for i, name in enumerate(order):
            if i < len(pos):
                val = pos[i]
                if name in ("de", "para"):
                    # treat as int
                    val = int(val)
                elif name in ("zser", "ysa", "ysb"):
                    val = complex(val)
                else:
                    val = float(val)
                locals_map = locals()
                locals_map[name] = val
                # reflect back
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
        # any remaining positionals are extras
        if len(pos) > len(order):
            extras = pos[len(order):]
        # If de/para/zser missing, raise
        if de is None or para is None or zser is None:
            raise ValueError(
                "Parâmetros mínimos de ramo: de, para, zser (ou passe uma sequência compatível).")
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
        return self

    def calcular_ybus(self):
        """
        Monta Ybus e calcula Zbus. Retorna:
        (Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, i_ramo, Bi, Bf, Ysa, Ysb, Identif, Zser)
        """
        nb = self.nb
        nr = len(self.ramos)

        # Utilizar tipos de dados idênticos ao código de referência
        Bi = np.zeros(nr, dtype=np.int64)
        Bf = np.zeros(nr, dtype=np.int64)
        Ysa = np.zeros(nr, dtype=complex)
        Ysb = np.zeros(nr, dtype=complex)
        Zser = np.zeros(nr, dtype=complex)
        Yser = np.zeros(nr, dtype=complex)  # Adicionar Yser explicitamente
        Eramo = np.zeros(nr, dtype=float)
        Faseramo = np.zeros(nr, dtype=float)
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
            Eramo[i] = float(r.get("eram", 0.0))
            Faseramo[i] = float(r.get("faseramo", 0.0))
            Identif[i] = r.get("identif", "")

        # Montar Ybus exatamente como no código de referência
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

        # Calcular Isi exatamente como no código de referência
        # Usar formato (nb, 1) para manter formato de matriz coluna
        Isi = np.zeros((nb, 1), dtype=complex)
        for k in range(nr):
            if Bi[k] == 0:
                Isi[Bf[k]-1, 0] = rect(Eramo[k], radians(Faseramo[k]))/Zser[k]
            if Bf[k] == 0:
                Isi[Bi[k]-1, 0] = rect(Eramo[k], radians(Faseramo[k]))/Zser[k]

        # Cálculo de Zbus usando a mesma abordagem
        # Definir tipos de dados explicitamente e usar formato exato
        Zbus = np.zeros((nb, nb), dtype=complex)
        try:
            # Usar a mesma chamada para inverter
            Zbus = np.linalg.inv(Ybus)
        except np.linalg.LinAlgError:
            Zbus = None

        # Calcular Vsi
        Vsi = np.zeros((nb, 1), dtype=complex)
        if Zbus is not None:
            Vsi = Zbus @ Isi

        # Calcular correntes nos ramos
        i_ramo = np.zeros((nr, 1), dtype=complex)
        for m in range(nr):
            a = Bf[m] - 1
            b = Bi[m] - 1
            if Bf[m] != 0 and Bi[m] != 0:
                i_ramo[m] = (Vsi[b, 0] - Vsi[a, 0]) / Zser[m]
            elif Bi[m] == 0:
                i_ramo[m] = (-Vsi[a, 0]) / Zser[m]
            elif Bf[m] == 0:
                i_ramo[m] = Vsi[b, 0] / Zser[m]

        return Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, i_ramo, Bi, Bf, Ysa, Ysb, Identif, Zser


# Testando com os ramos fornecidos pelo usuário
sistema = SistemaEletrico(10)
# Usando exatamente as linhas de seu exemplo (aceitando formas variadas)
sistema.adicionar_ramo(0,  1,  0.8j,  0.0, 0.0, 1,     0,    "G1")
sistema.adicionar_ramo(1,  3,  0.14j, 0.0, 0.0, 0,     0,    "T1")
sistema.adicionar_ramo(3,  5,  0.2j,  0.0, 0.0, 0,     0,   "LT1")
sistema.adicionar_ramo(5,  7,  0.3j,  0.0, 0.0, 0,     0,   "LT5")
sistema.adicionar_ramo(7,  10, 0.15j, 0.0, 0.0, 0,     0,    "T3")
sistema.adicionar_ramo(10, 0,  1.0j,  0.0, 0.0, 0.98, -8,    "M1")
sistema.adicionar_ramo(3,  4,  0.3j,  0.0, 0.0, 0,     0,   "LT2")
sistema.adicionar_ramo(5,  6,  0.2j,  0.0, 0.0, 0,     0,   "LT4")
sistema.adicionar_ramo(0,  2,  0.9j,  0.0, 0.0, 1.02,  2,    "G2")
sistema.adicionar_ramo(2,  4,  0.12j, 0.0, 0.0, 0,     0,    "T2")
sistema.adicionar_ramo(4,  6,  0.4j,  0.0, 0.0, 0,     0,   "LT3")
sistema.adicionar_ramo(6,  8,  0.4j,  0.0, 0.0, 0,     0,   "LT6")
sistema.adicionar_ramo(8,  9,  0.15j, 0.0, 0.0, 0,     0,    "T4")
sistema.adicionar_ramo(9, 0,  0.9j,  0.0, 0.0, 0.95, -12,   "M2")

# Calcular
Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, i_ramo, Bi, Bf, Ysa, Ysb, Identif, Zser = sistema.calcular_ybus()

# Impressão sucinta e clara dos resultados principais
print("Número de barras (nb):", sistema.nb)
print("Número de ramos (nr):", len(sistema.ramos))
print("\nYbus (matriz admitância nodal):")
np.set_printoptions(precision=2, suppress=True)
print(Ybus)
print("\nZbus (inversa de Ybus) – shape:",
      None if Zbus is None else Zbus.shape)
if Zbus is not None:
    print(Zbus)
print("\nBi (de), Bf (para):")
print(Bi, Bf)
print("\nYsa, Ysb (shunts por ramo):")
print(Ysa, Ysb)
print("\nZser (impedâncias série por ramo):")
print(Zser)
print("\nEramo (magnitudes) e Faseramo (angulos deg):")
print(Eramo, Faseramo)
print("\nIsi (correntes por barra calculadas somando correntes de ramos 'de'):")
print(Isi)
print("\nVsi = Zbus @ Isi (se Zbus calculável):")
print(Vsi)

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
        (Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, Bi, Bf, Ysa, Ysb, Identif, Zser)
        Isi: vetor de injeções por barra construído a partir dos ramos que têm 'de' como barra (aprox.)
        Vsi: Zbus @ Isi
        Observação: barras indexadas 1-based nos dados; aceitamos '0' como barra de referência (não incluída em Ybus).
        """
        nb = self.nb
        nr = len(self.ramos)
        Bi = np.zeros(nr, dtype=int)
        Bf = np.zeros(nr, dtype=int)
        Ysa = np.zeros(nr, dtype=complex)
        Ysb = np.zeros(nr, dtype=complex)
        Zser = np.zeros(nr, dtype=complex)
        Eramo = np.zeros(nr, dtype=float)
        Faseramo = np.zeros(nr, dtype=float)
        Identif = [""] * nr
        Ybus = np.zeros((nb, nb), dtype=complex)
        # preencher
        for i, r in enumerate(self.ramos):
            Bi[i] = int(r["de"])
            Bf[i] = int(r["para"])
            Zser[i] = complex(r["zser"])
            Ysa[i] = complex(r.get("ysa", 0j))
            Ysb[i] = complex(r.get("ysb", 0j))
            Eramo[i] = float(r.get("eram", 0.0))
            Faseramo[i] = float(r.get("faseramo", 0.0))
            Identif[i] = r.get("identif", "")
            # montar Ybus (tratando barras 0 como referência externa)
            L = Bi[i]-1
            M = Bf[i]-1
            Yser = 1.0 / Zser[i] if Zser[i] != 0 else 0
            # se ambos barras >0
            if L >= 0 and M >= 0:
                Ybus[L, L] += Yser + Ysa[i]
                Ybus[M, M] += Yser + Ysb[i]
                Ybus[L, M] -= Yser
                Ybus[M, L] -= Yser
            elif L >= 0:  # referência no fim (M== -1)
                Ybus[L, L] += Yser + Ysb[i]
            elif M >= 0:  # referência no início
                Ybus[M, M] += Yser + Ysa[i]
        # inversa (Zbus) – cuidar de singularidade
        try:
            Zbus = np.linalg.inv(Ybus)
        except np.linalg.LinAlgError:
            Zbus = None
        # Calcular Isi: interpretarei Isi como vetor de correntes de fontes internas:
        # Vou construir Isi por barra somando correntes de ramos que 'de' é essa barra,
        # usando Eramo/Faseramo como tensão de referência na origem do ramo dividido por Zser.
        Isi = np.zeros(nb, dtype=complex)
        # I_branch for each ramo:
        Ibranch = np.zeros(nr, dtype=complex)
        for i in range(nr):
            # se Zser==0 evita divisão por zero
            try:
                Ibranch[i] = rect(Eramo[i], radians(
                    Faseramo[i])) / Zser[i] if Zser[i] != 0 else 0
            except Exception:
                Ibranch[i] = 0
            # adicionar contribuição na barra 'de' (se non-ref)
            idx = Bi[i]-1
            if 0 <= idx < nb:
                Isi[idx] += Ibranch[i]
            # se desejarmos, a barra 'para' receberia -Ibranch (corrente saindo),
            # mas para seguir aproximação simples descontemos isso.
        # Vsi = Zbus @ Isi (se Zbus disponível)
        Vsi = Zbus.dot(Isi) if Zbus is not None else None
        return Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, Bi, Bf, Ysa, Ysb, Identif, Zser


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
Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, Bi, Bf, Ysa, Ysb, Identif, Zser = sistema.calcular_ybus()

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

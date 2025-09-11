import numpy as np


def Ybus(file_path="dados_sep.txt"):
    """
    Função que lê um arquivo de dados de sistema elétrico e constrói a matriz de admitância Ybus.

    Parâmetros:
    file_path (str): Caminho do arquivo de dados (padrão: "dados_sep.txt")

    Retorna:
    tuple: (Ybus, Zbus, Bi, Bf, Ysa, Ysb, Zser, Identif)
        - Ybus: Matriz de admitância nodal
        - Zbus: Matriz de impedância nodal (inversa de Ybus)
        - Bi: Vetor de barras de início dos ramos
        - Bf: Vetor de barras de fim dos ramos
        - Ysa: Vetor de admitâncias shunt no início dos ramos
        - Ysb: Vetor de admitâncias shunt no fim dos ramos
        - Zser: Vetor de impedâncias série dos ramos
        - Identif: Vetor de identificação dos ramos
    """
    import numpy as np
    from cmath import rect
    from math import radians
    try:
        with open(file_path, "r") as f:
            # Lendo as linhas de comentário e cabeçalhos (3 linhas)
            for _ in range(3):
                f.readline()

            # Lendo número de barras
            nb = int(f.readline().strip())

            # Linha de comentário
            f.readline()

            # Lendo número de ramos
            nr = int(f.readline().strip())

            # Inicializando arrays
            Bi = np.zeros(nr, dtype=int)
            Bf = np.zeros(nr, dtype=int)
            Ysa = np.zeros(nr, dtype=complex)
            Ysb = np.zeros(nr, dtype=complex)
            Zser = np.zeros(nr, dtype=complex)
            Yser = np.zeros(nr, dtype=complex)
            Ybus = np.zeros((nb, nb), dtype=complex)
            Eramo = np.zeros(nr, dtype=float)
            Faseramo = np.zeros(nr, dtype=float)
            Isi = np.zeros((nb, 1), dtype=complex)
            Vsi = np.zeros((nb, 1), dtype=complex)
            Identif = [""] * nr

            # Linha de comentário
            f.readline()

            # Lendo dados dos ramos
            for i in range(nr):
                ramo = f.readline()
                dados = ramo.strip().split(",")

                Bi[i] = int(dados[0])
                Bf[i] = int(dados[1])
                Zser[i] = complex(dados[2])
                Yser[i] = 1.0 / Zser[i] if Zser[i] != 0 else 0
                Ysa[i] = complex(dados[3])
                Ysb[i] = complex(dados[4])
                Eramo[i] = float(dados[5])
                Faseramo[i] = float(dados[6])
                Identif[i] = dados[7].strip()

            # Montando a matriz Ybus
            for j in range(nr):
                L = Bi[j] - 1  # Convertendo para índice 0-based
                M = Bf[j] - 1

                if M >= 0 and L >= 0:
                    Ybus[L, L] += Yser[j] + Ysa[j]
                    Ybus[M, M] += Yser[j] + Ysb[j]
                    Ybus[L, M] -= Yser[j]
                    Ybus[M, L] -= Yser[j]
                elif L >= 0:  # M == -1 (barra 0)
                    Ybus[L, L] += Yser[j] + Ysb[j]
                elif M >= 0:  # L == -1 (barra 0)
                    Ybus[M, M] += Yser[j] + Ysa[j]

            # Montando a matriz Isi
            from cmath import rect
            for k in range(nb):
                Isi[k] = rect(Eramo[k], radians(Faseramo[k])) / \
                    Zser[k]  # Corrente de linha de referência

            # Calculando Zbus
            Zbus = np.linalg.inv(Ybus)

            # Calculando Vsi
            Vsi = Zbus @ Isi

            # Calculando corrente na LT
            i_ramo = np.zeros((nr, 1), dtype=complex)
            for m in range(nr):
                if Bi[m] == 0:
                    i_ramo[m] += -Vsi[Bf[m]-1] / Zser[m]
                if Bf[m] == 0:
                    i_ramo[m] += Vsi[Bi[m]-1] / Zser[m]
                else:
                    i_ramo[m] += (Vsi[Bf[m]-1] - Vsi[Bi[m]-1]) / Zser[m]

            return Ybus, Zbus, Eramo, Faseramo, Isi, Vsi, i_ramo, Bi, Bf, Ysa, Ysb, Identif, Zser, Isi

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado")
    except Exception as e:
        raise RuntimeError(f"Erro ao processar o arquivo: {str(e)}")


ybus, zbus, Eramo, Faseramo, Isi, Vsi, i_ramo, *_ = Ybus()

np.set_printoptions(precision=2, suppress=True)
print("Correntes nos ramos:")
print(i_ramo)

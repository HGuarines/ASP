import numpy as np
import matplotlib.pyplot as plt
from asp import pol2ret, ret2pol

# Dados do sistema
R = 0.02  # pu
X = 0.16  # pu
Z = complex(R, X)  # impedância do alimentador

# Tensão na barra 2 (fixa)
V2_mod = 1.0
V2_angulo = 0  # graus
V2 = pol2ret(V2_mod, V2_angulo, unidade='g')

# Fatores de potência e seus respectivos ângulos
fps = {
    "0.8 indutivo": np.arccos(0.8),
    "0.9 indutivo": np.arccos(0.9),
    "1.0 unitário": 0,
    "0.9 capacitivo": -np.arccos(0.9),
    "0.8 capacitivo": -np.arccos(0.8)
}

# Faixa de potência ativa (em pu)
P_cargas = np.linspace(0.01, 1.5, 200)  # evita zero para não dividir por zero

# Inicializar dicionário para armazenar resultados
resultados = {fp: [] for fp in fps}

# Cálculo da tensão na barra 1 para cada FP e P
for rotulo, angulo in fps.items():
    for P in P_cargas:
        Q = P * np.tan(angulo)
        S = complex(P, Q)
        I = np.conj(S / V2)  # corrente complexa
        V1 = V2 + I * Z
        V1_mod, _ = ret2pol(V1, unidade='g')
        resultados[rotulo].append(V1_mod)

# Plotagem dos resultados
plt.figure(figsize=(10, 6))
for rotulo, tensoes in resultados.items():
    plt.plot(P_cargas, tensoes, label=rotulo)

plt.title("Variação da tensão na barra 1 em função da carga e do fator de potência")
plt.xlabel("Potência ativa da carga (pu)")
plt.ylabel("Tensão na barra 1 (pu)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("Q79.png")
plt.show()

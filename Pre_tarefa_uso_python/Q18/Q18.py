"""18. Plote os gráficos das funções a seguir"""

import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo para t e x

t = np.linspace(-10, 10, 1000)
x = np.linspace(-2, 2, 1000)  # Intervalo diferente para a função (e)

# Definir as funções
funcoes = {
    "a": (t, 2 * np.sin(3 * t - np.deg2rad(45))),
    "b": (t, 5 * np.exp(-3 * t)),
    "c": (t[t > 0], np.log(3 * t[t > 0])),  # Evitar log(0) e valores negativos
    "d": (t, 2 / np.cos(3 * t - np.deg2rad(45)) + 1 / np.tan(4 * t)),
    "e": (x, x**7 + 6 * x**5 + np.sin(x)),
    "f": (t, 2 * np.sin(3 * t - np.deg2rad(45)) + 1.3 * np.sin(240 * t - np.deg2rad(20))),
}

# Criar subgráficos
figura, eixos = plt.subplots(2, 3, figsize=(15, 10))
eixos = eixos.flatten()

# Plotar cada função
for i, (chave, (valores_x, valores_y)) in enumerate(funcoes.items()):
    eixos[i].plot(valores_x, valores_y, label=f"Função {chave}")
    eixos[i].axhline(0, color='black', linewidth=0.5)
    eixos[i].axvline(0, color='black', linewidth=0.5)
    eixos[i].legend()
    eixos[i].grid(True)

# Ajustar layout e salvar
plt.tight_layout()
plt.savefig("Q18_graficos")
plt.show()

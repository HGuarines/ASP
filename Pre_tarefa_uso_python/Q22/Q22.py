"""22.Plote os gráficos das seguintes funções no PYTHON num mesmo gráfico o
primeiro com a cor azul, o segundo com a cor vermelha e o terceiro preto.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo para t
t = np.linspace(0, 10, 1000)

# Definir as funções
y = 2 * np.cos(3 * t - np.deg2rad(25))
w = 5 * np.sin(np.exp(-3 * t))
z = np.log10(3 * t[t > 0]) 
t_log = t[t > 0]

# Criar gráfico com todas as funções juntas
plt.figure(figsize=(8, 5))
plt.plot(t, y, label=r'$y = 2\cos(3t - 25^\circ)$', color='b')
plt.plot(t, w, label=r'$w = 5\sin(e^{-3t})$', color='r')
plt.plot(t_log, z, label=r'$z = \log_{10}(3t)$', color='k')

plt.title("Funções y, w e z no Mesmo Gráfico")
plt.legend()
plt.grid()
plt.savefig("Q22.png")
plt.show()


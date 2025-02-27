"""19. Plote o gráfico da função a seguir"""

import numpy as np
import matplotlib.pyplot as plt

# Definição do intervalo de theta
theta = np.linspace(0, 2*np.pi, 1000)  # De 0 a 2π com 1000 pontos

# Definição da função r(θ) para 16 pétalas
r = np.sin(8*theta) * np.cos(8*theta)

# Criando o gráfico polar
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, label=r'$r = \sin(8\theta) \cos(8\theta)$')

# Configuração do gráfico
ax.set_title(r'Gráfico da flor com 16 pétalas', fontsize=14)
ax.legend()
plt.savefig("Q19_grafico.png")
plt.show()

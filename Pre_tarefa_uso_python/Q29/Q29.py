"""29. Obtenha o gráfico da função"""

import numpy as np
import matplotlib.pyplot as plt

# Dados 0 < x < 8
x = np.linspace(0, 8, 1000)

# Função
y  = 6 -5*x + 3*x**2
z = 4 - 6*x

# Criar gráfico com todas as funções juntas
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = 3x^2 -5x + 6$')
plt.plot(x, z, label = r'$z = 4 -6x$')

plt.title("Funções y e z")
plt.legend()
plt.grid()
plt.savefig("Q29.png")
plt.show()


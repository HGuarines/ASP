"""30. Obtenha o gráfico da função"""

import numpy as np
import matplotlib.pyplot as plt

# Dados 0 < x < 8
x = np.linspace(0, 8, 1000)

# Função
y  = 8 -3*x + 2*x**2
z = -2 + 4*x

# Criar gráfico com todas as funções juntas
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = 3x^2 -5x + 6$')
plt.plot(x, z, label=r'$z = 4x + 2$')

plt.title("Funções y e z")
plt.legend()
plt.grid()
plt.savefig("Q30.png")
plt.show()


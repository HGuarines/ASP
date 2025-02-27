"""28. Obtenha o gráfico da função"""

import numpy as np
import matplotlib.pyplot as plt

# Dados 0 < x < 8
x = np.linspace(0, 8, 1000)

# Função
y  = 6 -5*x + x**2

# Criar gráfico com todas as funções juntas
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = x^2 -5x + 6$')

plt.title("Função y")
plt.legend()
plt.grid()
plt.savefig("Q28.png")
plt.show()


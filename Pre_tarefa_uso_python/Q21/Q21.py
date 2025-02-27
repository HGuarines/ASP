"""21.Plote os gráficos das seguintes funções isoladamente no PYTHON e depois
num mesmo gráfico."""

import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo para t
t = np.linspace(0, 10, 1000)

# Definir as funções
y = 2 * np.sin(3 * t - np.deg2rad(45))
w = 5 * np.exp(-3 * t)
z = np.log(3 * t[t > 0]) 
t_log = t[t > 0]  

# Criar gráficos individuais
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].plot(t, y, label=r'$y = 2\sin(3t - 45^\circ)$', color='b')
ax[0].set_title("Função y")
ax[0].legend()
ax[0].grid()

ax[1].plot(t, w, label=r'$w = 5e^{-3t}$', color='g')
ax[1].set_title("Função w")
ax[1].legend()
ax[1].grid()

ax[2].plot(t_log, z, label=r'$z = \ln(3t)$', color='r')
ax[2].set_title("Função z")
ax[2].legend()
ax[2].grid()

plt.tight_layout()
plt.savefig("Q21_individuais.png")
plt.show()

# Criar gráfico com todas as funções juntas
plt.figure(figsize=(8, 5))
plt.plot(t, y, label=r'$y = 2\sin(3t - 45^\circ)$', color='b')
plt.plot(t, w, label=r'$w = 5e^{-3t}$', color='g')
plt.plot(t_log, z, label=r'$z = \ln(3t)$', color='r')

plt.title("Funções y, w e z no Mesmo Gráfico")
plt.legend()
plt.grid()
plt.savefig("Q21_juntas.png")
plt.show()


"""24. Obtenha as funções x, x³, e^x no intervalo 
0 < x < 4 coordenadas retangulares, 
semi-logarítmicas (no eixo y) e log-log."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 10, 1000)

# Definindo as funções
y_x = x
y_x3 = x**3
y_exp = np.exp(x)

# Coordenadas retangulares

plt.figure(figsize=(6, 4))
plt.plot(x, y_x, label='x')
plt.plot(x, y_x3, label='x³')
plt.plot(x, y_exp, label='e^x')
plt.title('Coordenadas Retangulares')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("Q24_coordret.png")
plt.show()

# Semi-logarítmico no eixo y
plt.figure(figsize=(6, 4))
plt.semilogy(x, y_x, label='x')
plt.semilogy(x, y_x3, label='x³')
plt.semilogy(x, y_exp, label='e^x')
plt.title('Coordenadas Semi-log (eixo y)')
plt.xlabel('x')
plt.ylabel('log(y)')
plt.legend()
plt.grid(True)
plt.savefig("Q24_semilog.png")
plt.show()

# Log-log
plt.figure(figsize=(6, 4))
plt.loglog(x, y_x, label='x')
plt.loglog(x, y_x3, label='x³')
plt.loglog(x, y_exp, label='e^x')
plt.title('Coordenadas Log-log')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.legend()
plt.grid(True)
plt.savefig("Q24_loglog.png")
plt.show()

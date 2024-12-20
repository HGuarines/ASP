""" Plotar degrau dado a função de transferencia """

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Definindo denominador e numerador:
num = [5, 10, 0]
den = [1, 5, 11, 5]

# Função de transferencia:
ft = ctrl.TransferFunction(num, den)

# Vetor tempo de 0 a 10 segundos (por 500 pontos)
tempo = np.linspace(0, 12, 500)
tempo_d, resposta_d = ctrl.step_response(ft, tempo)

# Plot do grafico da resposta no degrau e no impulso
plt.figure(figsize=(8, 4))
plt.plot(tempo_d, resposta_d, label='Resposta ao Degrau')
plt.title('Resposta no tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

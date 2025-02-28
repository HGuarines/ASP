"""26. Crie um vetor x com 100 componentes e some-os"""

import numpy as np
import asp

# Definindo n
n = np.linspace(1, 100, 100)

# Calculando os 100 valores de x
x = -1*n + (1 / (2*n + 1))

# Calculando a soma dos elementos do vetor x
soma_x = np.sum(x)

rsp26 = [('\n26. ', ''),
         ('soma dos elementos do vetor x = ', f'{soma_x:.4f}')]

asp.gerar_arquivo_texto("Q26.txt", "RESPOSTAS USO PYTHON", rsp26)

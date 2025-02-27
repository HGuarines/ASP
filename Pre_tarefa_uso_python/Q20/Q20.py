"""Resolva o seguinte sistema de equação usando o PYTHON"""

import numpy as np
import asp

# Definição dos coeficientes do sistema
A = np.array([[2, 1.5, 1],
              [1, 6, -2],
              [0, 2, 4]])

# Definição dos termos independentes
b = np.array([13.2, 21.64, 26.62])

# Resolvendo o sistema de equações lineares
solucao = np.linalg.solve(A, b)

rsp20 = [('\n20.', ' '),
         ('x1 = ', f'{solucao[0]:.3f}'),
         ('x2 = ', f'{solucao[1]:.3f}'),
         ('x3 = ', f'{solucao[2]:.3f}')]

# Exibindo a solução
asp.gerar_arquivo_texto('Q20.txt',
                        'RESPOSTAS USO PYTHON', rsp20)
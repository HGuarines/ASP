"""16. Resolva o seguinte sistema de equações"""

import numpy as np
import asp

# Matrizes A*X = B

A = np.array([[1+2j, 0, -5j],
              [0, 2j, -2],
              [2j, -2, 3+5j]])

B = np.array([[1+3j],
              [0],
              [2*np.exp(1j*np.deg2rad(45))]])

rsp16 = np.linalg.solve(A,B)

rsp16 = [('\n16.', ' '),
         ('I1 = ', f'{rsp16[0].item():.2f}'),
         ('I2 = ', f'{rsp16[1].item():.2f}'),
         ('I3 = ', f'{rsp16[2].item():.2f}')]

asp.gerar_arquivo_texto('Q16.txt',
                        'RESPOSTAS USO PYTHON', rsp16)
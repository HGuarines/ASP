"""15. Realize as seguintes operações no PYTHON a partir das matrizes dadas:"""

import numpy as np
import asp

# Sabendo-se que a é o fasor com módulo igual a 1 e fase 120º.
fase_a = np.deg2rad(120)
a = np.round(np.exp(1j * fase_a), 4)  # e^j2pi/3

# Definindo matrizes

A = np.array([[2+4j, 2-4j, -2],
              [-3j, 5-2j, 2],
              [6, 3-1j, 2]])

B = np.array([[2-3j],
              [4+3j],
              [1+5j]])

C = np.array([[1, 1, 1],
              [1, a**2, a],
              [1, a, a**2]])

D = np.array([[-2+3j, 5j, 4-2j]])

# (a) A^2
rspa = A @ A

# (b) A^-1
rspb = np.linalg.inv(A)
rspb = np.round(rspb, 4)

# (c) F = A x B
rspc = A @ B

# (d) A \ B
rspd = 'como a matriz B não tem inversa, a operação A * B^-1 não é possível.'

# (e) A^T
rspe = A.T

# (f) A^-1 x B
rspf = np.linalg.inv(A) @ B
rspf = np.round(rspf, 2)

# (g) B^T x C
rspg = B.T @ C
rspg = np.round(rspg, 2)

# (h) D x B
rsph = D @ B

rsp15 = [('\n15.', ' '),
         ('(a) A^2:\n', rspa),
         ('\n(b) A^-1:\n', rspb),
         ('\n(c) F = A x B:\n', rspc),
         ('\n(d) A \ B: ', rspd),
         ('\n(e) A^T:\n', rspe),
         ('\n(f) A^-1 x B:\n', rspf),
         ('\n(g) B^T x C:\n', rspg),
         ('\n(h) D x B:\n', rsph)]

asp.gerar_arquivo_texto('Q15.txt',
                        'RESPOSTAS USO PYTHON', rsp15)

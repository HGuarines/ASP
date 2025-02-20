"""12. Calcule usando comandos do PYTHON sabendo-se que:"""

import numpy as np
import asp

# Aniversário 13/12/2000

DA = 13
MA = 12
AA = 2000

A = np.array([
    [2, -19, MA],
    [AA, 4, 6],
    [-4,-2,DA]])

B = np.array([
    [DA],
    [4],
    [-7]])

C = np.array([
    [MA, 4, -4],
    [5, 20, -2],
    [-3,-4,12]])

D = np.array([[MA, 12, 3]])

# (a) Para obter o determinante de A  
rspa = np.linalg.det(A)

# (b) Para obter a transposta de A
rspb = A.T
 
# (c) Para obter o elemento da linha 2 e coluna 3 de A  
rspc = A[1,2]

# (d) Para obter a inversa de A  
rspd = np.linalg.inv(A)

# (e) Para obter a soma entre a transposta de B e A  
rspd = B.T+A

# (f) Para obter a diferença entre a transposta de A e B  
rspf = A.T-B

# (g) Para obter o produto A x D^T
rspg = A @ D.T

# (h) Para obter a linha 2 de D^T
rsph = D.T[1,:]

# (i) Para obter a coluna 3 de D  
rspi = D[:,2]

# (j) Para obter A/C
rspj = np.round(A @ np.linalg.inv(C))

# (k) Para obter o vetor X tal que AX = B
rspk = np.round(np.linalg.inv(A) @ B,2)

# (l) O número de elementos de A  
rspl = A.size

# (m) O posto da matriz A  
rspm = np.linalg.matrix_rank(A)

# (n) A diagonal principal da matriz A
rspn = np.diag(A)

# (o) A ordem da matriz A  
rspo = A.shape

# (p) A ordem da matriz B  
rspp = B.shape

# (q) A transposta da matriz A
rspq = A.T

# (r) O elemento (1,2) da matriz A e ainda o elemento (2,1) da matriz B  
rspr1 = A[0,1]
rspr2 = B[1,0]

rsp12 = [('\n12.', ' '),
         ('(a) O determinante de A: ', int(round(rspa,3))),
         ('\n(b) A transposta de A:\n', rspb),
         ('\n(c) O elemento da linha 2 e coluna 3 de A: ', rspc),
         ('\n(d) A inversa de A:\n', rspd),
         ('\n(e) A soma entre a transposta de B e A:\n', f'Normalmanete não seria possível somar uma matriz 3x3 por uma 1x3. O python repete a linha de B.T mais duas vezes para igualar com a quantidade de linhas da matriz A\n {rspd}\n'),
         ('(f) A diferença entre a transposta de A e B:\n',f'Normalmanete não seria possível subtrair uma matriz 3x3 por uma 1x3. O python repete a linha de B.T mais duas vezes para igualar com a quantidade de linhas da matriz A\n {rspf}\n'),
         ('(g) O produto A x D^T:\n', rspg),
         ('\n(h) A linha 2 de D^T: ', rsph),
         ('\n(i) A coluna 3 de D: ', rspi),
         ('\n(j) Calcular A/C:\n', rspj),
         ('\n(k) Qual o vetor X tal que AX = B:\n', rspk),
         ('\n(l) O número de elementos de A: ', rspl),
         ('\n(m) O posto da matriz A: ', rspm),
         ('\n(n) A diagonal principal da matriz A: ', rspn),
         ('\n(o) A ordem da matriz A: ', rspo),
         ('\n(p) A ordem da matriz B: ', rspp),
         ('\n(q) A transposta da matriz A:\n', rspq),
         ('\n(r) \nO elemento (1,2) da matriz A: ', rspr1),
         ('O elemento (2,1) da matriz B: ', rspr2)
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp12)
"""3. Exemplo usando a função pot_comp1f(V, I)"""

import asp
import numpy as np

# Dados de entrada
V = asp.pol2ret(220, 0)
I = asp.pol2ret(10, 0)

# Cálculo
P = asp.pot_comp1f(V, I)
P_polar = asp.ret2pol(P)

# Resultado
rsp1 = [('3.\n', 'Dados:'),
        ('V = ', '220 ∠ 0° V'),
        ('I = ', '10 ∠ 0° A'),
        ('\nTemos que:\nP = ', f'{P_polar[0]:.1f} ∠ {np.degrees(P_polar[1]):.1f}° W')]

asp.gerar_arquivo_texto('Q3.txt', 'APLICAÇÕES PYTHON', rsp1)

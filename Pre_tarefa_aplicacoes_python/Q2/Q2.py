"""2. Exemplo usando a função pot_comp3f(Va, Ia, Vb, Ib, Vc, Ic)"""

import asp
import numpy as np

# Dados de entrada
Va = asp.pol2ret(220, 0)
Ia = asp.pol2ret(10, 0)
Vb = asp.pol2ret(220, 120, 'g')
Ib = asp.pol2ret(10, 120, 'g')
Vc = asp.pol2ret(220, 240, 'g')
Ic = asp.pol2ret(10, 240, 'g')

# Calculo pot trifasica
S3f = asp.pot_comp3f(Va, Ia, Vb, Ib, Vc, Ic)
S_polar = asp.ret2pol(S3f)

rsp2 = [('2.\n', 'Dados:'),
        ('Va = ', '220 ∠ 0° V'),
        ('Ia = ', '10 ∠ 0° A'),
        ('Vb = ', '220 ∠ 120° V'),
        ('Ib = ', '10 ∠ 120° A'),
        ('Vc = ', '220 ∠ 240° V'),
        ('Ic = ', '10 ∠ 240° A'),
        ('\nTemos que:\nS = ', f'{S_polar[0]:.1f} ∠ {np.degrees(S_polar[1]):.1f}° W')]

asp.gerar_arquivo_texto('Q2.txt', 'APLICAÇÕES PYTHON', rsp2)

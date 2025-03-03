"""3. Exemplo usando a função cor_carga(V,N,FP)"""

import asp
import numpy as np

# Dados de entrada
Va = asp.pol2ret(220, 0)
Ia = asp.pol2ret(10, 0)
Vb = asp.pol2ret(220, 120, 'g')
Ib = asp.pol2ret(10, 120, 'g')
Vc = asp.pol2ret(220, 240, 'g')
Ic = asp.pol2ret(10, 240, 'g')
FP = 0.92

# Calculo pot mono
S1f = asp.pot_comp1f(Va, Ia)
S1f_polar = asp.ret2pol(S1f)

# Calculo pot trifasica
S3f = asp.pot_comp3f(Va, Ia, Vb, Ib, Vc, Ic)
S3f_polar = asp.ret2pol(S3f)

# Calculo corrente mono
I1f = asp.cor_carga(S1f, Va, FP, 1)
I1f_polar = asp.ret2pol(I1f)

# Calculo corrente trifasica
I3f = asp.cor_carga(S3f, Va, FP)
I3f_polar = asp.ret2pol(I3f)

rsp3 = [('3.\n', 'Dados:'),
        ('Va = ', '220 ∠ 0° V'),
        ('Ia = ', '10 ∠ 0° A'),
        ('Vb = ', '220 ∠ 120° V'),
        ('Ib = ', '10 ∠ 120° A'),
        ('Vc = ', '220 ∠ 240° V'),
        ('Ic = ', '10 ∠ 240° A'),
        ('\nTemos que \nA potencia aparente monofásica é:\nSa = ',
         f'{S1f_polar[0]:.1f} ∠ {np.degrees(S1f_polar[1]):.1f}° W'),
        ('\nA corrente de carga monofásica é:\nI1f = ',
         f'{I1f_polar[0]:.1f} ∠ {np.degrees(I1f_polar[1]):.1f}° A'),
        ('\nE a potencia aparente trifásica é:\nS3f = ',
         f'{S3f_polar[0]:.1f} ∠ {np.degrees(S3f_polar[1]):.1f}° W'),
        ('\nE a corrente de carga trifásica é:\nI3f = ', f'{I3f_polar[0]:.1f} ∠ {np.degrees(I3f_polar[1]):.1f}° A')]

asp.gerar_arquivo_texto('Q3.txt', 'APLICAÇÕES PYTHON', rsp3)

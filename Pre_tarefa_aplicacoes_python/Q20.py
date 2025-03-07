"""Resoluçao da questão 20"""

import asp
from math import sqrt

# Dados 2.1:
A1 = (6, 30)  # polar em graus
A2 = 3 + 5j

# (a) Converter A1 para forma retangular:
A1_ret = asp.pol2ret(*A1)
print(f'(a) A1 = {asp.format_complex(A1_ret, "r")}')

# (b) Converter A2 para forma polar e exponencial:
A2_pol = asp.ret2pol(A2)
print(f'\n(b) A2 = {asp.format_complex(A2_pol, 'p')}')
A2_exp = asp.format_complex(A2_pol, 'e')
print(f'(b) A2 = {A2_exp}')

# (c) Calcular A3 = A1 + A2, em forma polar:
A3 = A1_ret + A2
A3_pol = asp.ret2pol(A3)
rspc = asp.format_complex(A3, 'p')
print(f'\n(c) A3 = {rspc}')

# (d) Calcular A4 = A1 * A2, em forma retangular:
A4 = A1_ret * A2
rspc = asp.format_complex(A4, 'r')
print(f'\n(d) A4 = {rspc}')

# (e) Calcular A5 = A1 / A2*, em forma exponencial:
A5 = A1_ret / A2.conjugate()
A5_exp = asp.format_complex(A5, 'e')
print(f'\n(e) A5 = {A5_exp}')

# Dados 2.2:
# (a) i(t) = 500√2 cos(ωt + 30°)

ia, _ = asp.inst2fasor(500 * sqrt(2), 30)
rspa2 = asp.format_complex(ia, 'p')
print(f'\n(a) i(t) = {rspa2} A')

# (b) i(t) = 4sin(ωt + 30°)
ib, _ = asp.inst2fasor(4, 30, tipo='sin')
rspb2 = asp.format_complex(ib, 'p')
print(f'\n(b) i(t) = {rspb2} A')

# (c) i(t) = 5cos(ωt + 15°) + 10√2 cos(ωt + 30°)
ic1, _ = asp.inst2fasor(5, 15)
ic2, _ = asp.inst2fasor(10 * sqrt(2), 30)
ic = ic1 + ic2
rspc2 = asp.format_complex(ic, 'p')
print(f'\n(c) i(t) = {rspc2} A')

rsp20 = [('20.', ''),
         ('2.1:', ''),
         ('a) A1 = ', f'{asp.format_complex(A1_ret, "r")}'),
         ('b) A2 = ', f'{asp.format_complex(A2_pol, "p")}'),
         ('   A2 = ', f'{A2_exp}'),
         ('c) A3 = ', f'{rspc}'),
         ('d) A4 = ', f'{rspc}'),
         ('e) A5 = ', f'{A5_exp}'),
         ('\n2.2:', ''),
         ('a) i(t) = ', f'{rspa2} A'),
         ('b) i(t) = ', f'{rspb2} A'),
         ('c) i(t) = ', f'{rspc2} A')]

asp.gerar_arquivo_texto('Q20.txt', 'APLICAÇÕES PYTHON', rsp20)

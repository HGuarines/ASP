"""Resolução da questão 23"""

import math
import asp

# Questão 2.26
# Dados do problema
P = 120e3  # Potência ativa (W)
FP = 0.85  # Fator de potência (atrasado)
Vc = asp.pol2ret(480, 0, unidade='g')  # Tensão na carga (V)
Xl = 0.5 * 2  # Reatância da linha (Ω/km * 2 km)

# Impedância da linha (somente reatância)
Zl = complex(0, Xl)

# (a) Método da Potência Complexa
Ic = asp.cor_carga(P, abs(Vc), FP, N=1)  # Corrente da carga
# Ângulo da corrente (atrasa em relação à tensão)
phi_ic = -math.acos(FP)
# Corrente em forma retangular
Ic = asp.pol2ret(Ic, phi_ic, unidade='r')

# Cálculo da tensão no ponto de envio (lado da fonte)
Vf = Vc + Ic * Zl  # Tensão na fonte considerando a queda na linha
FPf = asp.fator_potencia(V=Vf, I=Ic)

# (b) Método da Análise de Circuito usando modelo PI
Vf_pi, If_pi = asp.cirpi(Vc, Ic, Zl, 0, 0)
FPf_pi = asp.fator_potencia(V=Vf_pi, I=If_pi)

# Questão 2.27
# Dados do problema
P = 50e3  # Potência ativa em W
FP_inicial = 0.8  # Fator de potência inicial
FP_final = 0.95  # Fator de potência desejado
V = 220  # Tensão em volts
f = 60  # Frequência em Hz

# Cálculo do banco de capacitor
dep_capacitancia = asp.calc_banco_capacitor(P, FP_inicial, FP_final, V, f)

# Questão 2.28
# Dados
V = 240  # V

# Potências das cargas
S1 = complex(15e3, 6667)
S2 = 3000 * (0.96 - 1j * math.sqrt(1 - 0.96**2))
S3 = complex(15e3, 0)

# Impedancias
Z1 = V**2 / S1
Z2 = V**2 / S2
Z3 = V**2 / S3

Zt = asp.imp_paral(Z1, Z2, Z3)
R = Zt.real
X = Zt.imag

# (a) Combinação em série de R e X
Zs = asp.imp_serie(R, X)

# (b) Combinação em paralelo R e X
Zp = asp.imp_paral(R, X)

rsp23 = [('23.', ''),
         ('2.26:', '\n(a) Método da Potência Complexa:'),
         ('Vf = ', f'{asp.format_complex(Vf, form='p')} V'),
         ('FP na fonte = ', f'{FP:.2f}'),
         ('\n(b) Método da Análise de Circuito:', ''),
         ('Vf = ', f"{asp.format_complex(Vf_pi, form='p')} V"),
         ('FP na fonte = ', f"{FPf_pi:.2f}"),
         ('\n2.27:', ''),
         ('Capacitância necessária: ', f"{dep_capacitancia:.2f} µF"),
         ('\n2.28:', ''),
         ('Impedancia total: ', f'{asp.format_complex(Zt)} Ω'),
         ('(a) Combinação em série de R e X: ', f'{Zs:.2f} Ω'),
         ('(b) Combinação em paralelo R e X: ', f'{Zp:.2f} Ω')]

asp.gerar_arquivo_texto('Q23.txt', 'APLICAÇÕES PYTHON', rsp23)

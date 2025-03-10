"""Resolução da questão 22"""

import asp
import schemdraw
import schemdraw.elements as elm
from math import sqrt

# 2.7
# Criando o diagrama do circuito fechado
with schemdraw.Drawing() as d:
    fonte = d.add(elm.SourceSin().label('100V'))
    d.add(elm.Line().right().length(1))
    r = d.add(elm.Resistor().label('3Ω'))
    l = d.add(elm.Inductor().label('8H'))
    c = d.add(elm.Capacitor().label('4F'))
    d.add(elm.Line().down().length(3))
    d.add(elm.Line().left().to(fonte.start))  # Fecha o circuito

    d.save('Q22_circuito.jpg')  # Salva corretamente usando schemdraw
    d.draw()

# Dados
V = 100
Zr = 3
Zl = 8j
Zc = complex(0, -1/4)  # -j/(ωC)

# Impedância equivalente
Zeq = asp.imp_serie(Zr, Zl, Zc)

# (c) Corrente total e fator de potência

I = V / Zeq

cos_phi = asp.fator_potencia(V, I, Zeq)

# 2.8
# dados
omega = 377  # rad/s
Rt = 5.76e-3  # Ω
Lt = 30.6e-6  # H
Rl = 5  # Ω
Ll = 5e-3  # H
C = 921e-6  # F

# Cálculo das impedâncias
Z_LT = complex(0, omega * Lt)  # jωL
Z_L = complex(0, omega * Ll)  # jωL
Z_C = complex(0, -1 / (omega * C))  # -j/(ωC)
Z_rt = complex(Rt, 0)
Z_rl = complex(Rl, 0)

# Fonte de tensão no domínio fasorial utilizando inst2fasor
V_fasorial, V_polar = asp.inst2fasor(120*sqrt(2), -30, tipo='cos', unidade='g')

rsp22 = [('22.\n', ''),
         ('2.7:', ''),
         ('Zeq = ', f'{asp.format_complex(Zeq, "r")} Ω'),
         ('I = ', f'{asp.format_complex(I, "p")} A'),
         ('Como o angulo entre V e I é -68.84°: ',
          '\nA corrente está atrasada em relação à tensão e o FP é indutivo.'),
         ('Fator de potência = ', f'{round(cos_phi, 2)}'),
         ('\n2.8:', ''),
         ('Z_Lt = ', f'{asp.format_complex(Z_LT, "p")} Ω'),
         ('Z_Ll = ', f'{asp.format_complex(Z_L, "p")} Ω'),
         ('Z_C = ', f'{asp.format_complex(Z_C, "p")} Ω'),
         ('V = ', f'{asp.format_complex(V_fasorial, "p")} V'),
         ('Zrt = ', f'{asp.format_complex(Z_rt, 'p')} Ω'),
         ('Zrl = ', f'{asp.format_complex(Z_rl, 'p')} Ω')]

asp.gerar_arquivo_texto('Q22.txt', 'APLICAÇÕES PYTHON', rsp22)

"""6. Exemplo usando a função oper_comp(Z1, form1, op, Z2, form2)"""

import asp
import numpy as np

# Dados de entrada
Z1 = 1 + 2j
Z2 = 3 + 4j
Z1_pol = asp.ret2pol(Z1)  # Z3
Z2_pol = asp.ret2pol(Z2)  # Z4

# Calculo da impedancia equivalente
Zeq_som = asp.oper_comp(Z1, 'r', '+', Z2, 'r')
Zeq_sub = asp.ret2pol(asp.oper_comp(Z1_pol, 'p', '-', Z2_pol, 'p'))
Zeq_mult = asp.oper_comp(Z1, 'r', '*', Z2_pol, 'p')
Zeq_div = asp.oper_comp(Z2, "r", "/", Z1_pol, "p")

rsp6 = [('6.\n', 'Dados:'),
        ('Z1 = ', asp.format_complex(Z1, 'r')),
        ('Z2 = ', asp.format_complex(Z2, 'r')),
        ('Z3 = ', asp.format_complex(Z1_pol, 'p')),
        ('Z4 = ', asp.format_complex(Z2_pol, 'p')),
        ('\nA soma dos números complexos em retangular é:\nZeq = Z1 + Z2 = ',
         asp.format_complex(Zeq_som, 'r')),
        ('\nA subtração dos números complexos em polar é:\nZeq = Z3 - Z4 = ',
         asp.format_complex(Zeq_sub, 'p')),
        ('\nA multiplicaçào de um número complexo em retangular e outro em polar é:\nZeq = Z1 * Z4 = ',
         asp.format_complex(Zeq_mult, 'r')),
        ('\nE a divisão dos números complexos em retangular e outro em polar é:\nZeq = Z2 / Z3 = ', asp.format_complex(Zeq_div, 'r'))]


asp.gerar_arquivo_texto('Q6.txt', 'APLICAÇÕES PYTHON', rsp6)

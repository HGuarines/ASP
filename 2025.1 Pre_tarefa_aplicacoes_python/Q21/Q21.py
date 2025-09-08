"""Resolução da questão 21"""

import asp

# Dados
I = asp.pol2ret(10, 0, 'g')
Z1 = 8 + 6j
Z2 = -6j

# Impedância equivalente
Zeq = asp.imp_paral(Z1, Z2)

# Calculo tensão V
V = I * Zeq

# Calculo das correntes
I1 = V / Z1
I2 = V / Z2

rsp21 = [('21.', ''),
         ('a) V = ', f'{asp.format_complex(V, "r")}'),
         ('   I1 = ', f'{asp.format_complex(I1, "r")}'),
         ('   I2 = ', f'{asp.format_complex(I2, "r")}')]

asp.gerar_arquivo_texto('Q21.txt', 'APLICAÇÕES PYTHON', rsp21)

asp.plot_fasor((I, "I"), (I1, "I1"), (I2, "I2"),
               (V, "V"), nome_arquivo='Q21_fasores.png')

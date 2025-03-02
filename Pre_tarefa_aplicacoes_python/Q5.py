"""5. Exemplo usando a função imp_paral(Z1,Z2)"""

import asp
import numpy as np

# Dados de entrada
Z1 = 1 + 2j
Z2 = 3 + 4j

# Calculo da impedancia equivalente
Zeq = asp.imp_paral(Z1, Z2)

rsp5 = [('5.\n', 'Dados:'),
        ('Z1 = ', f'{Z1} Ω'),
        ('Z2 = ', f'{Z2} Ω'),
        ('\nA impedância equivalente em paralelo é:\nZeq = ', f'{np.round(Zeq, 2)} Ω')]

asp.gerar_arquivo_texto('Q5.txt', 'APLICAÇÕES PYTHON', rsp5)

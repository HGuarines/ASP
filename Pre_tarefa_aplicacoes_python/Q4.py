"""4. Exemplo usando a função imp_series(Z1,Z2)"""

import asp

# Dados de entrada
Z1 = 1 + 2j
Z2 = 3 + 4j

# Calculo da impedancia equivalente
Zeq = asp.imp_serie(Z1, Z2)

rsp4 = [('4.\n', 'Dados:'),
        ('Z1 = ', f'{Z1} Ω'),
        ('Z2 = ', f'{Z2} Ω'),
        ('\nA impedância equivalente em série é:\nZeq = ', f'{Zeq} Ω')]

asp.gerar_arquivo_texto('Q4.txt', 'APLICAÇÕES PYTHON', rsp4)

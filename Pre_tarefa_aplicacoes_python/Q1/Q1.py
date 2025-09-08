"""1. Exemplo usando a função imp_series(Z1,Z2)"""

import asp

# Dados de entrada
Z1 = 1 + 2j
Z2 = 3 + 4j

# Calculo da impedancia equivalente
Zeq = asp.imp_serie(Z1, Z2)

rsp4 = [('1.\n', 'Dados:'),
        ('Z1 = ', f'{asp.format_complex(Z1)} Ω'),
        ('Z2 = ', f'{asp.format_complex(Z2)} Ω'),
        ('\nA impedância equivalente em série é:\nZeq = ', f'{asp.format_complex(Zeq)} Ω')]

asp.gerar_arquivo_texto('Q1.txt', 'APLICAÇÕES PYTHON', rsp4)

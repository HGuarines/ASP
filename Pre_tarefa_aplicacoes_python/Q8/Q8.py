"""8. Exemplo usando a função cte_gener(Zpi, Ya, Yb)"""

import asp

# Dados de entrada
Zpi = 10 + 5j  # Ω
Ya = 0.02 - 0.01j  # S
Yb = 0.01 + 0.02j  # S

# Calculo dos parâmetros ABCD
ABCD = asp.cte_gener(Zpi, Ya, Yb)

rsp8 = [('8.\n', 'Dados:'),
        ('Zpi = ', f'{asp.format_complex(Zpi)} Ω'),
        ('Ya = ', f'{asp.format_complex(Ya)} S'),
        ('Yb = ', f'{asp.format_complex(Yb)} S'),
        ('\nOs parâmetros ABCD do quadripolo são:\nA = ',
         f'{asp.format_complex(ABCD[0])}'),
        ('B = ', f'{asp.format_complex(ABCD[1])}'),
        ('C = ', f'{asp.format_complex(ABCD[2])}'),
        ('D = ', f'{asp.format_complex(ABCD[3])}')]

asp.gerar_arquivo_texto('Q8.txt', 'APLICAÇÕES PYTHON', rsp8)

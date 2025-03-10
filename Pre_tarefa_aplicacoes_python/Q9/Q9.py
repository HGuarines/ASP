"""9. Exemplo usando a funçao quad_casc(A1, B1, C1, D1, A2, B2, C2, D2)"""

import asp

# Dados de entrada
A1 = 1.0 + 1.0j
B1 = 2.0 + 0.5j
C1 = 0.5 + 0.25j
D1 = 1.0 + 0.75j
A2 = 1.5 + 1.5j
B2 = 1.0 + 0.5j
C2 = 0.75 + 0.25j
D2 = 1.5 + 1.0j

# Calculo dos parâmetros ABCD
ABCD = asp.quad_casc(A1, B1, C1, D1, A2, B2, C2, D2)

rsp9 = [('9.\n', 'Dados:'),
        ('A1 = ', asp.format_complex(A1)),
        ('B1 = ', asp.format_complex(B1)),
        ('C1 = ', asp.format_complex(C1)),
        ('D1 = ', asp.format_complex(D1)),
        ('A2 = ', asp.format_complex(A2)),
        ('B2 = ', asp.format_complex(B2)),
        ('C2 = ', asp.format_complex(C2)),
        ('D2 = ', asp.format_complex(D2)),
        ('\nOs parâmetros ABCD do quadripolo são:\nA = ',
         asp.format_complex(ABCD[0])),
        ('B = ', asp.format_complex(ABCD[1])),
        ('C = ', asp.format_complex(ABCD[2])),
        ('D = ', asp.format_complex(ABCD[3]))]

asp.gerar_arquivo_texto('Q9.txt', 'APLICAÇÕES PYTHON', rsp9)

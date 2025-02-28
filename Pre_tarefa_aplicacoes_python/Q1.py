"""1. Exemplo usando a função pot_comp1f(V, I)"""

import asp

# Dados de entrada
V = asp.pol2ret(220, 0)
I = asp.pol2ret(10, 0)

# Cálculo
P = asp.pot_comp1f(V, I)

# Resultado
rsp1 = [('1. ', 'Dados:'),
        ('V = ', '220 ∠ 0° V'),
        ('I = ', '10 ∠ 0° A'),
        ('Temos que:\nP = ', '2200 ∠ 0° W')]

asp.gerar_arquivo_texto('Q1.txt', 'APLICAÇÕES PYTHON', rsp1)

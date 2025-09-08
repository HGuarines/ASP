"""19. Exemplo usando a função impcabo(secao_bt, nomearq=None)"""

import asp

# Dados de entrada
secoes_bt = [1.5, 2.5, 4, 6, 10, 16, 25, 35,
             50, 70, 95, 120, 150, 185, 240]  # mm²

for secao_bt in secoes_bt:
    Z = asp.impcabo(secao_bt, 'Q19.txt')

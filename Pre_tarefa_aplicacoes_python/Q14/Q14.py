"""14. Exemplo usando a função estrela2delta(za, zb, zc, nomearq)"""

import asp

# Dados de entrada
za = 5 + 2j
zb = 3 + 1j
zc = 4 + 3j

zab, zbc, zca = asp.estrela2delta(za, zb, zc, "Q14.txt")

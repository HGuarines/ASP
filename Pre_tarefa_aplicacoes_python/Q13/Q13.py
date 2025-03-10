"""13. Exemplo usando a função delta2estrela(zab, zbc, zca, nomearq)"""

import asp

# Dados de entrada
zab = 5 + 2j
zbc = 3 + 1j
zca = 4 + 3j

za, zb, zc = asp.delta2estrela(zab, zbc, zca, "Q13.txt")

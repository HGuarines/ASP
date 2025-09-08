"""11. Exemplo usando a função cirpi(V2, I2, Z, Ya, Yb, nomearq)"""

import asp

# Dados de entrada
V2 = 10 + 5j
I2 = 2 - 1j
Z = 5 + 2j
Ya = 0.1j
Yb = 0.2j

nome_arquivo = "Q11.txt"
V1, I1 = asp.cirpi(V2, I2, Z, Ya, Yb, nome_arquivo)

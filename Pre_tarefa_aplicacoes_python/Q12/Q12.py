"""12. Exemplo usando a função cirpir(V1, I1, Z, Ya, Yb, nomearq)"""

import asp

# Dados de entrada
V1 = 10 + 5j
I1 = 2 - 1j
Z = 5 + 2j
Ya = 0.1j
Yb = 0.2j

nome_arquivo = "Q12.txt"
V2, I2 = asp.cirpir(V1, I1, Z, Ya, Yb, nome_arquivo)

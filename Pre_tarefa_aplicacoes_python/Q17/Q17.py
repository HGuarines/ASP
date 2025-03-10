"""17. Exemplo usando a função vfonte(Vc, Z, Sc, nomearq=None)"""

import asp

# Dados de entrada
Vc = (220, -30)  # V
Z = (5, 2)  # Ω
Sc = (5000, 2000)  # VA


# Chamada da função
Vf, If = asp.vfonte(Vc, Z, Sc, nomearq='Q17.txt')

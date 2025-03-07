"""18. Exemplo usando a função vfontepi(Vc, Z, Ya, Yb, Sc, nomearq=None)"""

import asp

# Dados de entrada
Vc = (220, 30)  # V
Z = (0.5, 0.1)  # Ω
Ya = (0.02, 0.005)  # S
Yb = (0.01, 0.002)  # S
Sc = 5000 + 3000j  # VA

Vf, If = asp.vfontepi(Vc, Z, Ya, Yb, Sc, 'Q18.txt')

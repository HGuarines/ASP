"""15. Exemplo usando a função queda1f(Ic, DVc, Lc, Vfn, nomearq=None)"""

import asp

# Dados de entrada
Ic = 10  # A
DVc = 5  # %
Lc = 0.1  # m
Vfn = 100  # V

Sc = asp.queda1f(Ic, DVc, Lc, Vfn, nomearq='Q15.txt')

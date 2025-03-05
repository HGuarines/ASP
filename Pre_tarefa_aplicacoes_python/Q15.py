"""15. Exemplo unsado a função queda1f(Ic, DVc, Lc, Vfn, nomearq=None)"""

import asp

# Dados de entrada
Ic = 10  # A
DVc = 2  # V
Lc = 0.1  # H
Vfn = 100  # V

Sc = asp.queda1f(Ic, DVc, Lc, Vfn, nomearq='Q15.txt')

"""16. Exemplo usando a função queda3f(Ic, DVc, Lc, Vfn, nomearq=None)"""

import asp


# Dados de entrada
Ic = 10  # A
DVc = 5  # %
Lc = 0.1  # m
Vfn = 220  # V

Sc = asp.queda3f(Ic, DVc, Lc, Vfn, nomearq='Q16.txt')

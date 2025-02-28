"""3. Exemplo usando a função cor_carga(V,N,FP)"""

import asp

# Dados de entrada
Va = asp.pol2ret(220, 0)
Ia = asp.pol2ret(10, 0)
Vb = asp.pol2ret(220, 120)
Ib = asp.pol2ret(10, 120)
Vc = asp.pol2ret(220, 240)
Ic = asp.pol2ret(10, 240)
FP = 0.92

# Calculo pot mono
S1f = asp.pot_comp1f(Va,Ia)
S1f_polar = asp.ret2pol(S1f)

# Calculo pot trifasica
S3f = asp.pot_comp3f(Va, Ia, Vb, Ib,Vc, Ic)
S3f_polar = asp.ret2pol(S3f)

# Calculo corrente mono
I1f = asp.cor_carga(S1f, Va, FP, 1)

# Calculo corrente trifasica
I3f = asp.cor_carga(S3f, Va, FP)
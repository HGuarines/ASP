"""11. Calcule os seguintes valores no PYTHON:"""

import asp
import math
import cmath
import mpmath as mp

# Dados:
# Data de nascimento 13/12/2000
DA = 13
MA = 12
AA = 2000

# a) cos²(DA⁰) + sen(2π/3)
rspa = (math.cos(math.radians(DA ** 0)) ** 2) + math.sin(math.pi*2/3)

# b) arcseno(MA/100) + arctang(DA) + tanh(AA/3000)
rspb = math.asin(MA/100) + math.atan(DA) + math.tanh(AA/3000)

# c) log_10(MA) + ln(DA) + log_2(AA)
rspc = math.log10(MA) + math.log(DA) + math.log2(AA)

# d) 2526 + e^(-DA) + 34 × 10^AA
rspd = 2526 + mp.exp(-DA) + mp.power(10, AA) * 34

# e) Log_AA(MA) → Logaritmo de MA na base AA
rspe = math.log(MA, AA)

# f) senh(AA + i3)
zf = AA + 3j
rspf = mp.sinh(zf)

# g) arcoseno(MA/100)
rspg = math.acos(MA / 100)

# h) senh(DA)
rsph = math.sinh(DA)

# i) cosh(MA) + tangente(DA)
rspi = math.cosh(MA) + math.tan(DA)

# j) arcocosseno(DA/100)
rspj = math.acos(DA / 100)

# k) round(35.34) e round(DA.38)
rspk1 = round(35.34)
rspk2 = round(DA+0.38)

# l) floor(MA.3) e floor(8.8)
rspl1 = math.floor(MA+0.3)
rspl2 = math.floor(8.8)

# m) ceil(2.3) e ceil(DA.8)
rspm1 = math.ceil(2.3)
rspm2 = math.ceil(DA+0.8)

# n) fix(MA.3) e fix(32.8) → Equivalente ao truncamento em Python
rspn1 = math.trunc(MA+0.3)
rspn2 = math.trunc(32.8)

# o) divisão inteira de MA por 4 e DA por 3
rspo1 = MA//4
rspo2 = DA//3

# p) abs(-MA)
rspp = abs(-MA)

# q) angle(DA - 3i) → Ângulo de um número complexo
rspq = cmath.phase(complex(DA, -3))

# r) real(MA - 4i) → Parte real do número complexo
zr = MA - 4j
rspr = zr.real

# s) log(MA)
rsps = math.log10(MA)

# t) e^π
rspt = math.exp(math.pi)

rsp11 = [
    ('\n11.', ' (arrendondados a 3 casas decimais)'),
    ('(a) cos²(DA⁰) + sen(2π/3) = ', round(rspa, 3)),
    ('(b) arcseno(MA/100) + arctang(DA) + tanh(AA/3000) = ', round(rspb, 3)),
    ('(c) log_10(MA) + ln(DA) + log_2(AA) = ', round(rspc, 3)),
    ('(d) 2526 + e^(-DA) + 34 × 10^AA = ', rspd),
    ('(e) Log_AA(MA) = ', round(rspe, 3)),
    ('(f) senh(AA + i3) = ', rspf),
    ('(g) arcoseno(MA/100) = ', round(rspg, 3)),
    ('(h) senh(DA)', round(rsph, 3)),
    ('(i) cosh(MA) + tangente(DA) = ', round(rspi, 3)),
    ('(j) arcocosseno(DA/100) = ', round(rspj, 3)),
    ('(k) round(35.34) e round(DA.38) = ', f'{rspk1} e {rspk2}'),
    ('(l) floor(MA.3) e floor(8.8) = ', f'{rspl1} e {rspl2}'),
    ('(m) ceil(2.3) e ceil(DA.8) = ', f'{rspm1} e {rspm2}'),
    ('(n) fix(MA.3) e fix(32.8) (truncar) = ', f'{rspn1} e {rspn2}'),
    ('(o) divisão inteira de MA por 4 e DA por 3 = ', f'{rspo1} e {rspo2}'),
    ('(p) abs(-MA) = ', rspp),
    ('(q) angle(DA - 3i) (fase) = ', round(rspq, 3)),
    ('(r) real(MA - 4i) = ', rspr),
    ('(s) log(MA) = ', round(rsps, 3)),
    ('(t) e^π = ', round(rspt, 3))
]

asp.gerar_arquivo_texto('Q11.txt',
                        'RESPOSTAS USO PYTHON', rsp11)

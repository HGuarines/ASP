"""14. Calcule usando comandos do python"""

import cmath
import asp

mod_a = 1
fase_a = cmath.pi*2/3
j = complex(0,1)

a = cmath.rect(mod_a, fase_a)
a = complex(round(a.real,4), round(a.imag,4))

# (a) (2 + 3i)^2
rspa = (2 + 3j) ** 2

# (b) 1 + a + a^2
rspb = 1 + a + a**2
rspb = complex(round(rspb.real,4),rspb.imag)

# (c) 1 - a
rspc = 1 - a

# (d) j^47 + 3j + 8
rspd = 8 + 3j + j**47

# (e) (2 - 5i)^-34
rspe = (2-5j)**-34
rspe = complex(round(rspe.real,4), round(rspe.imag,4))

# (f) a - a^2
rspf = a - a**2
rspf = complex(round(rspf.real,4), round(rspf.imag,4))

# (g) a^25
rspg = a**25
rspg = complex(round(rspg.real,4), round(rspg.imag,3))

# (h) a^143
rsph = a**143
rsph = complex(round(rsph.real,2), round(rsph.imag,3))

# (i) j + a + a^4
rspi = j + a + a**4
rspi = complex(round(rspi.real,4), round(rspi.imag,3))

rsp14 = [('\n14.',' '),
         ('(a) (2 + 3i)^2: ',rspa),
         ('(b) 1 + a + a^2: ', f'({rspb.real} + {rspb.imag}j)'),
         ('(c) 1 - a: ', rspc),
         ('(d) j^47 + 3j + 8: ', rspd),
         ('(e) (2 - 5i)^-34: ', rspe),
         ('(f) a - a^2: ', rspf),
         ('(g) a^25: ', rspg),
         ('(h) a^143: ', rsph),
         ('(i) j + a + a^4: ', rspi)]

asp.gerar_arquivo_texto('Q14.txt',
                        'RESPOSTAS USO PYTHON', rsp14)
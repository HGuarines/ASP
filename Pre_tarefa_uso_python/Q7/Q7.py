""" 7. Explique como introduzimos um número complexo no PYTHON na forma polar e na forma retangular. """

import asp
import cmath

z = 1 + 1j
rsp7 = [
    ('\n7.', '\nA biblioteca cmath tem as funções:'),
    (' \ncmath.rect(modulo, angulo) que devolve a forma retangular',
     '\ncmath.phase(z) onde z é um número complexo e devolve o seu angulo.'),
    ('\nPara z = 1 + 1j temos:', ' '),
    (f'cmath.phase(z) = {cmath.phase(z)}\n',
     f'módulo de z = abs(z) = {abs(z)}'),
    ('\nPara módulo = 1 ', 'e theta = pi/2, temos:'),
    ('cmath.rect(1, pi/2) = ', cmath.rect(1, cmath.pi/2))

]

asp.gerar_arquivo_texto('Q7.txt',
                        'RESPOSTAS USO PYTHON', rsp7)

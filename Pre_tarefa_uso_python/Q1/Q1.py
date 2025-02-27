""" 1. Como são introduzidos os números no formato 1,62x10^-4? E o número PI? E e^2? """

import math
import asp

a = 1.62e-4

rsp1 = [
    ('\n1.', ' '),
    (f'(a)\nO número {a} deve ser escrito da segunte maneira no script: ', '1.62e-4'),
    (f'(b)\nO número Pi ({math.pi}) deve ser importado de math da segunte maneira: ', 'math.pi'),
    (f'(c)\nO número de Euler (e) também deve ser importado de math. Para elevar x por y devemos fazer a operação x**y. ',
     f'e**2 = {math.e ** 2}')
]

asp.gerar_arquivo_texto('Q1.txt',
                        'RESPOSTAS USO PYTHON', rsp1)

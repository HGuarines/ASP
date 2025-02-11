"""Pre Tarefa 1 - USO DO PYTHON"""
import math
import asp

# 1. Como são introduzidos os números no formato 1,62x10^-4? E o número PI? E e^2?\

a = 1.62e-4

calculos = [
    (f'1.\n(a)\nO número {a} deve ser escrito da segunte maneira no script: ', '1.62e-4'),
    (f'(b)\nO número Pi ({math.pi}) deve ser importado de math da segunte maneira: ', 'math.pi'),
    (f'(c)\nO número de Euler (e) também deve ser importado de math. Para elevar x por y devemos fazer a operação x**y. ',
     f'e**2 = {math.e ** 2}'),
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', calculos)

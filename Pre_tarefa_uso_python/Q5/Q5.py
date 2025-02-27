""" 5. Explique como introduzimos uma matriz no PYTHON. Dê um exemplo. """

import numpy as np
import asp

matriz = np.array([[2, 3], [4, 5]])

rsp5 = [
    ('\n5.', ' '),
    ('Há diversas maneiras de se criar uma matriz no python. No entanto, a biblioteca NumPy tem a função array\n',
     f'Após "import Numpy as np" fazemos np.array([]) e inserimos valores ou listas de valores dentro do array. \n{matriz}')
]

asp.gerar_arquivo_texto('Q5.txt',
                        'RESPOSTAS USO PYTHON', rsp5)

""" 6. Explique o que é a biblioteca cmath e como usar esta biblioteca nos programas. """

import asp
import cmath

rsp6 = [
    ('\n6.', ' '),
    ('A biblioteca cmath foi criada para facilitar e otimizar operações com números complexos',
     '\nPara utiliza-la basta traze-la ao programa com "import cmath" e será possivel trabalhar com números complexos.'),
    ('Ex: cmath.sqrt(-1) = ', cmath.sqrt(-1))
]

asp.gerar_arquivo_texto('Q6.txt',
                        'RESPOSTAS USO PYTHON', rsp6)

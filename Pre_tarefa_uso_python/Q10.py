""" 10.Explique como introduzimos estes números no PYTHON: 6,242^-46,4 e 1,2 x 10^-4 """

import asp

rsp10 = [
    ('\n10.', ' '),
    ('1,2 x 10^-4 --> ', '1.2e-4'),
    ('6,242^-46,4 --> ', '6.242 ** -46.4')
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp10)

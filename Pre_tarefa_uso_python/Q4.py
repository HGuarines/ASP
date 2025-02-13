""" 4. Explique o que é a biblioteca math e como usar esta biblioteca nos programas. """

import asp
import math

rsp4 = [
    ('\n4.', ' '),
    ('A biblioteca math é um módulo embutido na linguagem Python que fornece funções matemáticas para cálculos mais complexos.\n',
     f'Para utilizar essa biblioteca precisamos primeiro importa-la utilizando "import math" e podemos fazer calculos como o cosseno de pi math.cos(math.pi) = {math.cos(math.pi)}')
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp4)

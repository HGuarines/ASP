"""Pre Tarefa 1 - USO DO PYTHON"""

import numpy as np
import math
import asp

respostas = []

# 1. Como são introduzidos os números no formato 1,62x10^-4? E o número PI? E e^2?\


a = 1.62e-4

rsp1 = [
    ('\n1.', ' '),
    (f'(a)\nO número {a} deve ser escrito da segunte maneira no script: ', '1.62e-4'),
    (f'(b)\nO número Pi ({math.pi}) deve ser importado de math da segunte maneira: ', 'math.pi'),
    (f'(c)\nO número de Euler (e) também deve ser importado de math. Para elevar x por y devemos fazer a operação x**y. ',
     f'e**2 = {math.e ** 2}')
]

# 2. Explique os comandos usados no programa da Figura 3.

rsp2 = [
    ('\n2.', ' '),
    ('Linha 33: ', 'Foi definido o nome do arquivo'),
    ('Linha 34: ', 'Comando open para criar arquivo txt como escrita (w)'),
    ('Linha 35: ', 'Pula uma linha e cria uma linha com 45 (*)'),
    ('Linha 36: ', 'Cria uma linha com 45 (*) e pula uma linha'),
    ('Linha 37 a 46: ', 'Comando write() escreve o que estiver dento dos parenteses'),
    ('Linha 47: ', 'Comando close() finaliza o processo de escrever dentro do txt')
]

# 3. Explique como são feitas as principais operações aritméticas no Python.
# Mostre exemplos de cada um deles.

rsp3 = [
    ('\n3.', ' '),
    ('Soma: ', f'Utiliza-se o sinal + para somar. Ex: 2 + 3 = {2+3}'),
    ('Subtração: ', f'Utiliza-se o sinal - para subtrair. Ex: 2 - 3 = {2-3}'),
    ('Divisão: ', f'Utiliza-se o sinal / para dividir. Ex: 2/3 = {2/3:.3f}'),
    ('Multiplicação: ',
     f'Utiliza-se o sinal * para multiplicar. Ex: 2 * 3 = {2*3}')
]

# 4. Explique o que é a biblioteca math e como usar esta biblioteca nos programas.

rsp4 = [
    ('\n4.', ' '),
    ('AA biblioteca math é um módulo embutido na linguagem Python que fornece funções matemáticas para cálculos mais complexos.\n',
     f'Para utilizar essa biblioteca precisamos primeiro importa-la utilizando "import math" e podemos fazer calculos como o cosseno de pi math.cos(math.pi) = {math.cos(math.pi)}')
]

# 5. Explique como introduzimos uma matriz no PYTHON. Dê um exemplo.


matriz = np.array([[2, 3], [4, 5]])

rsp5 = [
    ('\n5.', ' '),
    ('Há diversas maneiras de se criar uma matriz no python. No entanto, a biblioteca NumPy tem a função array\n',
     f'Após "import Numpy as np" fazemos np.array([]) e inserimos valores ou listas de valores dentro do array. \n{matriz}')
]

# 6. Explique o que é a biblioteca cmath e como usar esta biblioteca nos programas.

rsp6 = [
    ('\n6.', 0)
]
# 7. Explique como introduzimos um número complexo no PYTHON na forma polar e na forma retangular.

# 8. Explique como os gráficos podem ser feitos no PYTHON. Apresente um arquivo que produza este gráfico.


respostas = respostas + rsp1 + rsp2 + rsp3 + rsp4 + rsp5

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', respostas)

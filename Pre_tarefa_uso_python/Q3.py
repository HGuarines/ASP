""" 3. Explique como são feitas as principais operações aritméticas no Python.
Mostre exemplos de cada um deles. """

import asp

rsp3 = [
    ('\n3.', ' '),
    ('Soma: ', f'Utiliza-se o sinal + para somar. Ex: 2 + 3 = {2+3}'),
    ('Subtração: ', f'Utiliza-se o sinal - para subtrair. Ex: 2 - 3 = {2-3}'),
    ('Divisão: ', f'Utiliza-se o sinal / para dividir. Ex: 2/3 = {2/3:.3f}'),
    ('Multiplicação: ',
     f'Utiliza-se o sinal * para multiplicar. Ex: 2 * 3 = {2*3}')
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp3)

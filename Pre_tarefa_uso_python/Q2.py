""" 2. Explique os comandos usados no programa da Figura 3. """

import asp

rsp2 = [
    ('\n2.', ' '),
    ('Linha 33: ', 'Foi definido o nome do arquivo'),
    ('Linha 34: ', 'Comando open para criar arquivo txt como escrita (w)'),
    ('Linha 35: ', 'Pula uma linha e cria uma linha com 45 (*)'),
    ('Linha 36: ', 'Cria uma linha com 45 (*) e pula uma linha'),
    ('Linha 37 a 46: ', 'Comando write() escreve o que estiver dento dos parenteses'),
    ('Linha 47: ', 'Comando close() finaliza o processo de escrever dentro do txt')
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp2)

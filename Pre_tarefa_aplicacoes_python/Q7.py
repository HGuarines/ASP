"""7. Exemplo usando a função Qcor_pot(P, FPA, FPN)"""

import asp

# Dados de entrada
P = 8172  # W
FPA = 0.75
FPN = 0.92

# Calculo da potência reativa de correção
Qcor = asp.Qcor_pot(P, FPA, FPN)
Qcor_kVAr = Qcor / 1000

rsp7 = [('7.\n', 'Dados:'),
        ('P = ', f'{P} W'),
        ('FPA = ', f'{FPA}'),
        ('FPN = ', f'{FPN}'),
        ('\nA potência reativa de correção necessária para compensar o fator de potência do sistema é:\nQcor = ',
         f'{Qcor_kVAr:.2f} kVAr')]

asp.gerar_arquivo_texto('Q7.txt', 'APLICAÇÕES PYTHON', rsp7)

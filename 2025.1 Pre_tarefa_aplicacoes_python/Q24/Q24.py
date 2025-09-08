"""Resolução da questão 24"""

import asp

# Dados da fonte
Vf = 1000  # Tensão RMS da fonte em volts
f = 60  # Frequência em Hz

# Dados das cargas
# Carga 1: Indutiva, 125 kVA, FP = 0.28 atrasado
S1_mod = 125e3
FP1 = 0.28
P1 = S1_mod * FP1
Q1 = (S1_mod**2 - P1**2)**0.5
S1 = complex(P1, Q1)

# Carga 2: Capacitiva, 10 kW, 40 kvar
S2 = complex(10e3, -40e3)

# Carga 3: Resistiva, 15 kW
S3 = complex(15e3, 0)

# (a) Cálculo das potências totais
St = S1 + S2 + S3
Pt = St.real
Qt = St.imag
FPt = Pt / abs(St)

# (b) Cálculo da correção do fator de potência para 0.8 atrasado
FP_desejado = 0.8
Qt_corrigido = Pt * ((1 - FP_desejado**2)**0.5 / FP_desejado)
Q_corrigido = Qt - Qt_corrigido

# Cálculo da capacitância necessária
C_necessario = asp.calc_banco_capacitor(Pt, FPt, FP_desejado, Vf, f)

# Corrente antes e depois da correção
I_antes = abs(St) / Vf
St_corrigido = complex(Pt, Qt_corrigido)
I_depois = abs(St_corrigido) / Vf

# Exibição dos resultados
rsp24 = [('24.', ''),
         ('2.30:', ''),
         ('(a) Determine Pt, Qt, St e FP', ''),
         ('Pt = ', f'{Pt / 1e3} kW'),
         ('Qt = ', f'{Qt / 1e3} kVAr'),
         ('St = ', f'{abs(St) / 1e3} kVA'),
         ('FP = ', f'{round(FPt, 2)}'),
         ('\n(b) Encontre o banco de capacitor para FP = 0.8', ''),
         ('Novo Q necessário para correção = ',
          f'{round(Q_corrigido / 1e3, 2)} kVAr'),
         ('C = ', f'{round(C_necessario, 2)} μF'),
         ('I antes da correção: ', I_antes),
         ('I depois da correção: ', I_depois)]

asp.gerar_arquivo_texto('Q24.txt', 'APLICAÇÕES PYTHON', rsp24)

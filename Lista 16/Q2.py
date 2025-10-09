import lib as asp
import numpy as np

# Dicionário contendo os dados sobre os condutores
dados = {'frequencia': [60],
         'cabo': ['VALERIAN'],
         'raio_1': [''],
         'raio': [14.55/2, 14.55/2, 14.55/2],
         'Num_cond_feixe': [0],
         'X_feixe': [0],
         'Y_feixe': [0],
         'X': [0, 2.8, 2.8],
         'Y': [8.5, 8.9, 9.7],
         'r0': [0.278, 0.278, 0.278],
         't0': [75, 75, 75],
         'RMG': [0.00552],
         'Flecha': [1.35, 1.35, 1.35]}

# Resistência do condutor a 50 graus
r_50_condutor = asp.resistencia_corrigida_dict(50, dados)

# Parâmetros
RMG = dados['RMG'][0]
raio1 = dados['raio_1'][0]
raio = dados['raio'][0]
r_75_condutor = dados['r0'][0]

# Ajusta as alturas em relação as flechas
dados['Y'] = asp.ajuste_altura(dados)

# Matriz A dos coeficientes de campo
A_CI = asp.matrix_Alt(dados['raio'], dados)

# Matriz das capacitâncias da linha
Clt_CI = np.linalg.inv(A_CI)

# Capacitâncias de serviço e por fases da linha
Cs_CI, Ca_CI, Cb_CI, Cc_CI = asp.Cserv(Clt_CI)

# Matriz A dos coeficientes de campo sem considerar condutor imagem
A = asp.matrix_Alt_sem_CI(dados['raio'], dados)

# Matriz das capacitâncias da linha sem considerar condutor imagem
Clt = np.linalg.inv(A)

# Capacitâncias de serviço e por fases da linha sem considerar condutor imagem
Cs, Ca, Cb, Cc = asp.Cserv(Clt)

respostas = [("Respostas Imagem 2", "\n1. Dados dos condutores: "),
             ("Raio do condutor (mm): ", raio),
             ("Raio Médio Geométrico (m): ", RMG),
             ("Resistência das fases a 75°C (ohm/km): ", np.round(r_75_condutor, 4)),
             ("Resistência das fases a 50°C (ohm/km): ", np.round(r_50_condutor[0], 4)),
             ("\n2. Matriz 3x3 da capacitância da linha\n", Clt_CI),
             ("\n3. Matriz 3x3 da capacitância da linha sem o condutor imagem\n", Clt),
             ("\n4. Capacitância aparente por fase da linha (nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca_CI*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb_CI*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc_CI*10**9, precisao=4)),
             ("\n5. Capacitância aparente por fase da linha sem condutor imagem (nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc*10**9, precisao=4)),
             ("\n6. Capacitância de serviço da linha (nF): ", asp.format_complex(Cs_CI*10**9)),
             ("\n7. Capacitância de serviço da linha sem condutor imagem (nF): ", asp.format_complex(Cs*10**9)),
             ]

asp.gerar_arquivo_texto('Q2.txt', "TAREFA 16 Q2", respostas)
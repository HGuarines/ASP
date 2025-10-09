""" RESOLUÇÃO DA QUESTÃO 2"""

import lib as asp
import numpy as np

# Dicionário contendo os dados sobre os condutores
dados = {'frequencia': [60],
         'cabo': ['PIGEON'],
         'raio_1': [3],
         'raio': [12.75/2],
         'Num_cond_feixe': [0],
         'X_feixe': [0, 0],
         'Y_feixe': [0, 0],
         'X': [0, 2.8, 2.8],
         'Y': [8.5, 8.9, 9.7],
         'r0': [0.474],
         't0': [75],
         'RMG': [0.00489],
         'Flecha': [1, 35]}

# Resistência do condutor a 50 graus
r_50 = asp.resistencia_corrigida_dict(50, dados)

# Parâmetros
RMG = dados['RMG'][0]
raio1 = dados['raio_1'][0]
raio = dados['raio'][0]
r_75 = dados['r0'][0]

# Ajustando alturas efetivas ao solo
flecha = dados['Flecha'][0]

for i in range(len(dados['Y'])):
    h = dados['Y'][i]
    dados['Y'][i] = asp.altura_efetiva_flecha(h, flecha)

# Matriz impedância com condutor imagem
Zlt_CI = asp.matrix_Zlt(r_50, dados)

# Matriz impedância sem condutor imagem
Zlt = asp.matrix_Zlt_sem_CI(r_50, dados)

# Impedância aparente por fase e impedância de serviço com condutor imagem
Zserv_CIs, Zserv_CIa, Zserv_CIb, Zserv_CIc = asp.Zserv(Zlt_CI)

# Impedância aparente por fase e impedância de serviço sem condutor imagem
Zservs, Zserva, Zservb, Zservc = asp.Zserv(Zlt)

resultados = [
    ("FIGURA 2", ""),
    ("\n1. ", ""),
    ("Tipo do condutor: ", dados['cabo'][0]),
    ("AWG: ", int(dados['raio_1'][0])),
    ("Raio do condutor (mm): ", raio),
    ("Raio Medio Geométrico (mm): ", RMG),
    ("Resistência a 75°C (ohm/km): ", np.round(r_75, 4)),
    ("Resistência a 50°C (ohm/km): ", np.round(r_50, 4)),
    ("\n2. ", ""),
    ("Matriz de impedância por unidade de comprimento com condutor imagem (ohm/km): \n", Zlt_CI),
    ("\n3. ", ""),
    ("Matriz de impedância por unidade de comprimento sem condutor imagem (ohm/km): \n", Zlt),
    ("\n4. ", ""),
    ("Impedância aparente por fase com condutor imagem (ohm/km): ", ""),
    ("Fase A: ", asp.format_complex(Zserv_CIa, precisao=4)),
    ("Fase B: ", asp.format_complex(Zserv_CIb, precisao=4)),
    ("Fase C: ", asp.format_complex(Zserv_CIc, precisao=4)),
    ("\n5. ", ""),
    ("Impedância aparente por fase sem condutor imagem (ohm/km): ", ""),
    ("Fase A: ", asp.format_complex(Zserva, precisao=4)),
    ("Fase B: ", asp.format_complex(Zservb, precisao=4)),
    ("Fase C: ", asp.format_complex(Zservc, precisao=4)),
    ("\n6. ", ""),
    ("Impedância de serviço da linha com condutor imagem (ohm): ",
     asp.format_complex(Zserv_CIs)),
    ("\n7. ", ""),
    ("Impedância de serviço da linha sem condutor imagem (ohm): ",
     asp.format_complex(Zservs))

]

np.set_printoptions(precision=4, suppress=True)
asp.gerar_arquivo_texto("Q2.txt", "FIGURA 2", resultados)

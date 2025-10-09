import lib as asp
import numpy as np

# Dicionário contendo os dados sobre os condutores
dados = {'frequencia': [60],
         'cabo': ['GROSBEAK'],
         'raio_1': ['636 Kcmil'],
         'raio': [25.15/2, 25.15/2, 25.15/2, (15.4/2)/1000, (15.4/2)/1000],
         'Num_cond_feixe': [2],
         'X_feixe': [0, 0.4],
         'Y_feixe': [0, 0],
         'X': [0, 10, 20, 10-4.8, 10+4.8],
         'Y': [19.4, 19.4, 19.4, 29.4, 29.4],
         'r0': [0.108, 0.108, 0.108, 0.497, 0.497],
         't0': [75, 75, 75, 75, 75],
         'RMG': [0.01021, 0.01021, 0.01021, (15.4/2)/1000, (15.4/2)/1000],
         'Flecha': [0, 0, 0]}

m_transposicao_3x3 = np.array([[0, 1, 0],
                               [0, 0, 1],
                               [1, 0, 0]])

m_transposicao_5x5 = np.array([[0, 1, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1]])

# Resistência do condutor a 50 graus
r_50_condutor = asp.resistencia_corrigida_dict(50, dados)

# Parâmetros
RMG = dados['RMG'][0]
raio1 = dados['raio_1'][0]
raio = dados['raio'][0]
r_75_condutor = dados['r0'][0]
r_75_pararaio = dados['r0'][-1]

# Ajusta as alturas em relação as flechas
dados['Y'] = asp.ajuste_altura(dados)

# Resistência dos condutores pela resistência do feixe
inicio = 0
for i in range(3):
    dados['r0'][i] = asp.resistencia_feixe(dados, dados['r0'][i], inicio)

# RMG do feixe de condutores
inicio = 0
for i in range(3):
    dados['RMG'][i] = asp.rmg_feixe(dados, i, 0)

r_50_feixe = asp.resistencia_corrigida_dict(50, dados)

# Matriz A do trecho 1
A_CI_1 = asp.matrix_Alt(dados['raio'], dados)
Clt_CI_1 = np.linalg.inv(A_CI_1)
Cs_CI_1, Ca_CI_1, Cb_CI_1, Cc_CI_1, Cltcp_CI_1 = asp.matriz_impedancia_reduzida(
    Clt_CI_1)

# Matriz A do trecho 2
Clt_CI_2 = m_transposicao_5x5.T @ Clt_CI_1 @ m_transposicao_5x5
Cs_CI_2, Ca_CI_2, Cb_CI_2, Cc_CI_2, Cltcp_CI_2 = asp.matriz_impedancia_reduzida(
    Clt_CI_2)

# Matriz A do trecho 3
Clt_CI_3 = m_transposicao_5x5.T @ Clt_CI_2 @ m_transposicao_5x5
Cs_CI_3, Ca_CI_3, Cb_CI_3, Cc_CI_3, Cltcp_CI_3 = asp.matriz_impedancia_reduzida(
    Clt_CI_3)

# Matriz A do trecho 1 sem CI
A_1 = asp.matrix_Alt_sem_CI(dados['raio'], dados)
Clt_1 = np.linalg.inv(A_1)
Cs_1, Ca_1, Cb_1, Cc_1, Cltcp_1 = asp.matriz_impedancia_reduzida(Clt_1)

# Matriz A do trecho 2 sem CI
Clt_2 = m_transposicao_5x5.T @ Clt_1 @ m_transposicao_5x5
Cs_2, Ca_2, Cb_2, Cc_2, Cltcp_2 = asp.matriz_impedancia_reduzida(Clt_2)

# Matriz A do trecho 3 sem CI
Clt_3 = m_transposicao_5x5.T @ Clt_2 @ m_transposicao_5x5
Cs_3, Ca_3, Cb_3, Cc_3, Cltcp_3 = asp.matriz_impedancia_reduzida(Clt_3)

# Matriz transposta
Clt_CI_T = (Clt_CI_1*1/3 + Clt_CI_2*1/3 + Clt_CI_3*1/3)
Cs_CI_T, Ca_CI_T, Cb_CI_T, Cc_CI_T, Cabccp_CI_T = asp.matriz_impedancia_reduzida(
    Clt_CI_T)

# Matriz transposta sem CI
Clt_T = (Clt_1*1/3 + Clt_2*1/3 + Clt_3*1/3)
Cs_T, Ca_T, Cb_T, Cc_T, Cabccp_T = asp.matriz_impedancia_reduzida(Clt_T)

respostas = [("Respostas Imagem 3", "\n1. Dados dos subcondutores: "),
             ("Raio do condutor (mm): ", raio),
             ("Raio Médio Geométrico (m): ", RMG),
             ("Resistência das fases a 75°C (ohm/km): ", np.round(r_75_condutor, 4)),
             ("Resistência dos cabos para raios a 75°C (ohm/km): ",
              np.round(r_75_pararaio, 4)),
             ("Resistência das fases a 50°C (nF/km): ",
              np.round(r_50_condutor[0], 4)),
             ("Resistência dos cabos para raios a 50°C (ohm/km): ",
              np.round(r_50_condutor[-1], 4)),
             ("\n2. Dados do feixe", ""),
             ("Raio Médio Geométrico (mm): ", np.round(dados['RMG'][0], 5)),
             ("Resistência das fases a 75°C (ohm/km): ",
              np.round(dados['r0'][0], 4)),
             ("Resistência das fases a 50°C (ohm/km): ",
              np.round(r_50_feixe[0], 4)),
             ("\n3. Matriz capacitância da linha 5x5\n", Clt_CI_1),
             ("\n4. Matriz capacitância da linha 5x5 - sem CI\n", Clt_1),
             ("\n5. Matriz capacitância da linha reduzida 3x3\n", Cltcp_CI_1),
             ("\n6. Matriz capacitância da linha reduzida 3x3 - sem CI\n", Cltcp_1),
             ("\n7. Capacitância aparente por fase da linha no primeiro trecho(nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca_CI_1*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb_CI_1*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc_CI_1*10**9, precisao=4)),
             ("\n8. Capacitância aparente por fase da linha no primeiro trecho sem CI(nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca_1*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb_1*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc_1*10**9, precisao=4)),
             ("\n9. Capacitância de serviço do primeiro trecho da linha (nF): ",
              asp.format_complex(Cs_CI_1*10**9, precisao=4)),
             ("\n10. Capacitância de serviço do primeiro trecho da linha sem CI (nF): ",
              asp.format_complex(Cs_1*10**9, precisao=4)),
             ("\n11. Matriz capacitância da linha 5x5 transposta\n", Clt_CI_T),
             ("\n12. Matriz capacitância da linha 5x5 transposta - sem CI\n", Clt_T),
             ("\n13. Matriz capacitância da linha reduzida 3x3 transposta\n", Cabccp_CI_T),
             ("\n14. Matriz capacitância da linha reduzida 3x3 transposta - sem CI\n", Cabccp_T),
             ("\n15. Capacitância aparente por fase da linha no primeiro trecho(nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca_CI_T*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb_CI_T*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc_CI_T*10**9, precisao=4)),
             ("\n16. Capacitância aparente por fase da linha no primeiro trecho sem CI(nF/km):", ""),
             ("Fase A: ", asp.format_complex(Ca_T*10**9, precisao=4)),
             ("Fase B: ", asp.format_complex(Cb_T*10**9, precisao=4)),
             ("Fase C: ", asp.format_complex(Cc_T*10**9, precisao=4)),
             ("\n17. Capacitância de serviço do primeiro trecho da linha (nF): ",
              asp.format_complex(Cs_CI_T*10**9, precisao=4)),
             ("\n18. Capacitância de serviço do primeiro trecho da linha sem CI (nF): ",
              asp.format_complex(Cs_T*10**9, precisao=4)),
             ]

asp.gerar_arquivo_texto('Q3.txt', "TAREFA 16 Q3", respostas)

import lib_pr as asp
import numpy as np

np.set_printoptions(precision=4, suppress=True)

# Dicionário contendo os dados sobre os condutores
dados = {'frequencia': [60],
         'cabo': ['KINGBIRD'],
         'raio_1': ['636 Kcmil'],
         'raio': [23.89/2],
         'Num_cond_feixe': [2],
         'X_feixe': [0, 0.35],
         'Y_feixe': [0, 0],
         'X': [0, 10, 20, 10-4.8, 10+4.8],
         'Y': [19.4, 19.4, 19.4, 29.4, 29.4],
         'r0': [0.106, 0.106, 0.106, 0.497, 0.497],
         't0': [75, 75, 75, 75, 75],
         'RMG': [0.00927, 0.00927, 0.00927, (15.4/2)/1000, (15.4/2)/1000],
         'Flecha': [0, 0, 0, 0, 0]}

m_transposicao_3x3 = np.array([[0, 1, 0],
                               [0, 0, 1],
                               [1, 0, 0]])

m_transposicao_5x5 = np.array([[0, 1, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1]])

# Resistência do condutor a 50 graus
r_50 = asp.resistencia_corrigida_dict(50, dados)

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

# Resistência dos cabos para raio para 75 graus
r_75 = asp.resistencia_corrigida_dict(75, dados)


# RMG do feixe de condutores
inicio = 0
for i in range(3):
    dados['RMG'][i] = asp.rmg_feixe(dados, i, 0)


# Matriz ZLT
ZLT_CI = asp.matrix_Zlt(r_75, dados)
Zservs, Zserva, Zservb, Zservc, Zabccp_CI = asp.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI)

# Matriz ZLT trecho 2
ZLT_CI_2 = m_transposicao_5x5.T @ ZLT_CI @ m_transposicao_5x5
Zservs_2, Zserva_2, Zservb_2, Zservc_2, Zabccp_CI_2 = asp.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI_2)

# Matriz ZLT trecho 3
ZLT_CI_3 = m_transposicao_5x5.T @ ZLT_CI_2 @ m_transposicao_5x5
Zservs_3, Zserva_3, Zservb_3, Zservc_3, Zabccp_CI_3 = asp.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI_3)

asp.imprimir_matriz(Zabccp_CI_3, 'Zabc_3')

respostas = [("Respostas Imagem 1", "\n1. Dados dos subcondutores: "),
             ("Raio do condutor (mm): ", raio),
             ("Raio Medio Geométrico (mm): ", RMG),
             ("Resistência das fases a 75°C (ohm/km): ", np.round(r_75_condutor, 4)),
             ("Resistência dos pararaios a 75°C (ohm/km): ",
              np.round(r_75_pararaio, 4)),
             ("Resistência das dases a 50°C (ohm/km): ", np.round(r_50[0], 4)),
             ("Resistência dos pararaios a 50°C (ohm/km): ",
              np.round(r_50[-1], 4)),
             ("\n2. Dados do feixe", ""),
             ("Raio Medio Geométrico (mm): ", np.round(dados['RMG'][0], 5)),
             ("Resistência das fases a 75°C (ohm/km): ",
              np.round(dados['r0'][0], 4)),
             ("Resistência das dases a 50°C (ohm/km): ", np.round(r_50[0], 4)),
             ("\n3. Matriz impedancia da linha 5x5\n", ZLT_CI),
             ("\n4. Matriz impedancia da linha reduzida 3x3\n", Zabccp_CI),
             ("\n5. Impedancia aparente por fase (ohm/km): ", ""),
             ("Fase A: ", asp.format_complex(Zserva, precisao=4)),
             ("Fase B: ", asp.format_complex(Zservb, precisao=4)),
             ("Fase C: ", asp.format_complex(Zservc, precisao=4)),
             ("\n6. Impedancia de serviço da linha no trecho 1 (ohm): ",
              asp.format_complex(Zservs)),
             ("\n7. Matriz impedancia da linha 5x5 - trecho 2\n", ZLT_CI_2),
             ("\n8. Matriz impedancia da linha reduzida 3x3 - trecho 2\n", Zabccp_CI_2),
             ("\n9. Matriz impedancia da linha 5x5 - trecho 3\n", ZLT_CI_3),
             ("\n10. Matriz impedancia da linha reduzida 3x3 - trecho 3\n", Zabccp_CI_3),
             ("\n11. Matriz impedancia da linha 5x5 - trecho 4\n", ZLT_CI),
             ("\n12. Matriz impedancia da linha reduzida 3x3 - trecho 4\n", Zabccp_CI),
             ("\n13. Matriz impedancia da linha transposta 5x5\n", ZLT_CI_2),
             ("\n14. Matriz impedancia da linha transposta reduzida 3x3\n", Zabccp_CI_2),
             ("\n15. Impedancia aparente por fase da linha transposta (ohm/km):", ""),
             ("Fase A: ", asp.format_complex(Zserva_2, precisao=4)),
             ("Fase B: ", asp.format_complex(Zservb_2, precisao=4)),
             ("Fase C: ", asp.format_complex(Zservc_2, precisao=4)),
             ("\n16. Impedancia de serviço da linha transposta (ohm): ",
              asp.format_complex(Zservs_2))
             ]

asp.gerar_arquivo_texto('Q1_TAREFA15.txt', "Figura 1", respostas)

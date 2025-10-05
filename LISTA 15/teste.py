import asp

# Dicionário de dados
dados = {
    'frequencia': [60],
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
    'Flecha': [1, 35]
}

# Cria instância da classe
linha = asp.ParametrosLinha(dados)

# Calcula resistência a 50°C
r_50 = linha.resistencia_corrigida_dict(50)
print(f"Resistência a 50°C: {r_50:.6f} Ω/km")

# Ajusta alturas considerando flecha
linha.ajustar_alturas_flecha()

# Calcula matriz com condutor imagem
print("\n=== COM CONDUTOR IMAGEM ===")
Zlt_CI = linha.matrix_Zlt(r_50, com_condutor_imagem=True)
# linha.imprimir_matriz_Zlt(Zlt_CI, com_condutor_imagem=True)
Zserv_CIs, Zserv_CIa, Zserv_CIb, Zserv_CIc = linha.Zserv(Zlt_CI)
print(f"\nImpedância de serviço: {Zserv_CIs}")

# Calcula matriz sem condutor imagem
print("\n=== SEM CONDUTOR IMAGEM ===")
Zlt = linha.matrix_Zlt(r_50, com_condutor_imagem=False)
# linha.imprimir_matriz_Zlt(Zlt, com_condutor_imagem=False)
Zservs, Zserva, Zservb, Zservc = linha.Zserv(Zlt)
print(f"\nImpedância de serviço: {asp.format_complex(Zservs)}")

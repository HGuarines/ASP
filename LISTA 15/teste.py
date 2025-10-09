import numpy as np
from lib import ParametrosLinha

np.set_printoptions(precision=3, suppress=True)

# Dicionário contendo os dados sobre os condutores
dados = {
    'frequencia': [60],
    'cabo': ['KINGBIRD'],
    'raio_1': ['636 Kcmil'],
    'raio': [23.89/2],
    # 2 condutores por fase, 0 para cabos para-raios
    'Num_cond_feixe': [2, 2, 2, 0, 0],
    'X_feixe': [0, 0.35],
    'Y_feixe': [0, 0],
    'X': [0, 10, 20, 10-4.8, 10+4.8],  # 3 fases + 2 cabos para-raios
    'Y': [19.4, 19.4, 19.4, 29.4, 29.4],
    'r0': [0.106, 0.106, 0.106, 0.497, 0.497],
    't0': [75, 75, 75, 75, 75],
    'RMG': [0.00927, 0.00927, 0.00927, (15.4/2)/1000, (15.4/2)/1000],
    'Flecha': [0, 0, 0, 0, 0]
}

# Matrizes de transposição
m_transposicao_3x3 = np.array([[0, 1, 0],
                               [0, 0, 1],
                               [1, 0, 0]])

m_transposicao_5x5 = np.array([[0, 1, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1]])

# ==============================================================================
# USANDO A CLASSE ParametrosLinha
# ==============================================================================

# Cria instância da classe
linha = ParametrosLinha(dados)

print("="*70)
print("ANÁLISE DE LINHA DE TRANSMISSÃO COM FEIXES E CABOS PARA-RAIOS")
print("="*70)

# 1. Ajusta as alturas em relação às flechas
print("\n[1] Ajustando alturas com flecha...")
alturas_ajustadas = linha.ajuste_altura()
print(f"Alturas ajustadas: {alturas_ajustadas}")

# 2. Calcula resistência dos condutores do feixe
print("\n[2] Calculando resistência dos feixes...")
for i in range(3):
    r_original = linha.dados['r0'][i]
    linha.dados['r0'][i] = linha.resistencia_feixe(r_original, i)
    print(
        f"Fase {i}: {r_original:.4f} Ω/km -> {linha.dados['r0'][i]:.4f} Ω/km (feixe)")

# 3. Calcula resistências para 75°C
print("\n[3] Calculando resistências a 75°C...")
r_75 = linha.resistencia_corrigida_dict(75)
print(f"Resistências a 75°C: {r_75}")

# 4. Calcula RMG do feixe de condutores
print("\n[4] Calculando RMG dos feixes...")
# Nota: Para calcular RMG do feixe, precisamos das coordenadas dos subcondutores
# Vamos criar coordenadas expandidas para os subcondutores

# Backup dos dados originais
X_original = linha.dados['X'].copy()
Y_original = linha.dados['Y'].copy()

# Expande coordenadas para incluir subcondutores do feixe
X_expandido = []
Y_expandido = []

for i in range(3):  # Para cada fase (feixe de 2 condutores)
    X_expandido.append(X_original[i] + dados['X_feixe'][0])
    Y_expandido.append(Y_original[i] + dados['Y_feixe'][0])
    X_expandido.append(X_original[i] + dados['X_feixe'][1])
    Y_expandido.append(Y_original[i] + dados['Y_feixe'][1])

# Adiciona cabos para-raios
X_expandido.extend(X_original[3:5])
Y_expandido.extend(Y_original[3:5])

# Atualiza temporariamente para calcular RMG
linha.dados['X'] = X_expandido
linha.dados['Y'] = Y_expandido

# Calcula RMG para cada feixe
RMG_feixes = []
for i in range(3):
    posicao_nc = i * 2  # Cada feixe tem 2 condutores
    rmg_calculado = linha.rmg_feixe(i, 0)
    RMG_feixes.append(rmg_calculado)
    print(f"RMG do feixe {i}: {rmg_calculado:.6f} m")

# Restaura coordenadas originais e atualiza RMG
linha.dados['X'] = X_original
linha.dados['Y'] = Y_original

# Atualiza RMG dos feixes
for i in range(3):
    linha.dados['RMG'][i] = RMG_feixes[i]

print(f"\nRMG atualizado: {linha.dados['RMG']}")

# ==============================================================================
# CÁLCULO DAS MATRIZES DE IMPEDÂNCIA COM TRANSPOSIÇÃO
# ==============================================================================

print("\n" + "="*70)
print("CÁLCULO DAS IMPEDÂNCIAS COM TRANSPOSIÇÃO")
print("="*70)

# TRECHO 1: Configuração original
print("\n--- TRECHO 1: Configuração Original ---")
ZLT_CI = linha.matrix_Zlt(r_75, com_condutor_imagem=True)
linha.imprimir_matriz_Zlt(ZLT_CI, com_condutor_imagem=True)

Zservs, Zserva, Zservb, Zservc, Zabccp_CI = linha.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI)

print(f"\nImpedância de serviço (Trecho 1): {Zservs}")
print(f"Za = {Zserva}")
print(f"Zb = {Zservb}")
print(f"Zc = {Zservc}")

linha.imprimir_matriz(Zabccp_CI, 'Zabc Trecho 1')

# TRECHO 2: Primeira transposição
print("\n--- TRECHO 2: Primeira Transposição ---")
ZLT_CI_2 = m_transposicao_5x5.T @ ZLT_CI @ m_transposicao_5x5
linha.imprimir_matriz_Zlt(ZLT_CI_2, com_condutor_imagem=True)

Zservs_2, Zserva_2, Zservb_2, Zservc_2, Zabccp_CI_2 = linha.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI_2)

print(f"\nImpedância de serviço (Trecho 2): {Zservs_2}")
print(f"Za = {Zserva_2}")
print(f"Zb = {Zservb_2}")
print(f"Zc = {Zservc_2}")

linha.imprimir_matriz(Zabccp_CI_2, 'Zabc Trecho 2')

# TRECHO 3: Segunda transposição
print("\n--- TRECHO 3: Segunda Transposição ---")
ZLT_CI_3 = m_transposicao_5x5.T @ ZLT_CI_2 @ m_transposicao_5x5
linha.imprimir_matriz_Zlt(ZLT_CI_3, com_condutor_imagem=True)

Zservs_3, Zserva_3, Zservb_3, Zservc_3, Zabccp_CI_3 = linha.matriz_impedancia_reduzida_da_5x5(
    ZLT_CI_3)

print(f"\nImpedância de serviço (Trecho 3): {Zservs_3}")
print(f"Za = {Zserva_3}")
print(f"Zb = {Zservb_3}")
print(f"Zc = {Zservc_3}")

linha.imprimir_matriz(Zabccp_CI_3, 'Zabc Trecho 3 (Final)')

# ==============================================================================
# IMPEDÂNCIA EQUIVALENTE TRANSPOSTA
# ==============================================================================

print("\n" + "="*70)
print("IMPEDÂNCIA EQUIVALENTE COM TRANSPOSIÇÃO COMPLETA")
print("="*70)

# Impedância média dos 3 trechos
Zabccp_media = (Zabccp_CI + Zabccp_CI_2 + Zabccp_CI_3) / 3

linha.imprimir_matriz(Zabccp_media, 'Zabc Média (Transposição Completa)')

# Calcula impedância de serviço média
Zservs_media, Zserva_media, Zservb_media, Zservc_media = linha.Zserv(
    Zabccp_media)

print(f"\nImpedância de serviço média: {Zservs_media}")
print(f"Za média = {Zserva_media}")
print(f"Zb média = {Zservb_media}")
print(f"Zc média = {Zservc_media}")

# ==============================================================================
# COMPARAÇÃO: COM E SEM TRANSPOSIÇÃO
# ==============================================================================

print("\n" + "="*70)
print("COMPARAÇÃO: COM E SEM TRANSPOSIÇÃO")
print("="*70)

print("\nSEM TRANSPOSIÇÃO (apenas Trecho 1):")
print(f"  Zs = {Zservs}")
print(f"  Za = {Zserva}")
print(f"  Zb = {Zservb}")
print(f"  Zc = {Zservc}")

print("\nCOM TRANSPOSIÇÃO COMPLETA (média dos 3 trechos):")
print(f"  Zs = {Zservs_media}")
print(f"  Za = {Zserva_media}")
print(f"  Zb = {Zservb_media}")
print(f"  Zc = {Zservc_media}")

# Verifica desbalanceamento
desbalanceamento_sem = np.std([Zserva, Zservb, Zservc])
desbalanceamento_com = np.std([Zserva_media, Zservb_media, Zservc_media])

print(
    f"\nDesbalanceamento sem transposição: {abs(desbalanceamento_sem):.6f} Ω/km")
print(
    f"Desbalanceamento com transposição: {abs(desbalanceamento_com):.6f} Ω/km")
print(
    f"Redução do desbalanceamento: {(1 - abs(desbalanceamento_com)/abs(desbalanceamento_sem))*100:.2f}%")

# ==============================================================================
# RESUMO DOS DADOS DA LINHA
# ==============================================================================

print("\n" + "="*70)
print("RESUMO DOS DADOS DA LINHA")
print("="*70)

print(f"\nCabo: {linha.dados['cabo'][0]}")
print(f"Configuração: {linha.dados['raio_1'][0]}")
print(f"Frequência: {linha.frequencia} Hz")
print(f"Número de condutores por feixe: {linha.dados['Num_cond_feixe'][0]}")
print(f"Espaçamento entre subcondutores: {linha.dados['X_feixe'][1]} m")

print(f"\nCoordenadas das fases:")
for i in range(3):
    print(
        f"  Fase {i+1}: X = {X_original[i]:.2f} m, Y = {Y_original[i]:.2f} m")

print(f"\nCoordenadas dos cabos para-raios:")
for i in range(3, 5):
    print(
        f"  Cabo {i-2}: X = {X_original[i]:.2f} m, Y = {Y_original[i]:.2f} m")

print(f"\nResistências originais a 75°C:")
for i, r in enumerate(dados['r0']):
    tipo = "Fase" if i < 3 else "Para-raios"
    print(f"  {tipo} {i+1 if i < 3 else i-2}: {r:.4f} Ω/km")

print(f"\nResistências dos feixes:")
for i in range(3):
    print(f"  Feixe {i+1}: {linha.dados['r0'][i]:.4f} Ω/km")

print(f"\nRMG dos feixes:")
for i in range(3):
    print(f"  Feixe {i+1}: {linha.dados['RMG'][i]:.6f} m")

print("\n" + "="*70)

"""Resolução da questão 6
Mostrar que num sistema elétrico trifásico a potência reativa instantânea é nula."""

import numpy as np
from asp import gerar_arquivo_texto

# Frequência e parâmetros
frequencia = 60  # Hz
omega = 2 * np.pi * frequencia
tempo = np.linspace(0, 1/frequencia, 1000)  # 1 ciclo completo

# Tensões e correntes de pico (sistema equilibrado)
tensao_pico = 220 * np.sqrt(2)
corrente_pico = 10 * np.sqrt(2)

# Defasagens das fases (120° = 2*pi/3 rad)
defasagens = [0, -2 * np.pi / 3, 2 * np.pi / 3]

# Correntes com defasagem de 90° (corrente atrasada -> carga puramente indutiva)
phi = np.pi / 2

# Calcular potência reativa instantânea total por somatório
pot_reativa_total = np.zeros_like(tempo)

for fase in defasagens:
    v = tensao_pico * np.sin(omega * tempo + fase)
    i_q = corrente_pico * np.sin(omega * tempo + fase + phi)
    pot_reativa_total += v * i_q

# Verificar se a potência reativa total é aproximadamente nula (erro numérico admissível)
pot_media = np.mean(pot_reativa_total)
pot_maxima = np.max(np.abs(pot_reativa_total))

# Gerar relatório com os resultados
calculos = [
    ("6.\n", "Sistema trifásico equilibrado:"),
    ("- Tensões senoidais com defasagem de 120°.", ""),
    ("- Correntes com mesma defasagem e atraso de 90° (carga puramente indutiva).", ""),
    ("\nResultados dos cálculos numéricos:", ""),
    ("Potência reativa média (esperado ≈ 0): ", f"{pot_media:.2e} Var"),
    ("Máximo valor absoluto encontrado: ", f"{pot_maxima:.2e} Var"),
    ("\nConclusão:", ""),
    ("- A potência reativa instantânea total em sistema trifásico equilibrado é nula.", ""),
    ("- Os valores encontrados são desprezíveis e atribuídos à precisão numérica.", "")
]

gerar_arquivo_texto(
    "Q6.txt", "Demonstração da Potência Reativa Nula", calculos)

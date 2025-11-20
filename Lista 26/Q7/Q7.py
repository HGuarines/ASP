import pandas as pd
import asp

tabela = r'Tabela_fluxo7.xlsx'

# importar dados do excel
try:
    df_fluxo = pd.read_excel(tabela, sheet_name='fluxo_carga').fillna(0.0)
    df_ybus = pd.read_excel(tabela, sheet_name='Ybus').fillna(0.0)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
    exit()

# chamando a função matriz ybus e imprimindo a matriz Ybus
Ybus = asp.matriz_ybus(df_ybus)
print(Ybus)

fluxo = asp.fluxo_newton_raphson(df_fluxo, Ybus, iteracoes=4)
display(fluxo)

df_matriz_ybus = pd.DataFrame(Ybus)

# Define o nome do arquivo de saída
nome_arquivo = 'resultado_fluxo.xlsx'

# Cria um "escritor" de Excel
# O 'engine='openpyxl'' é recomendado para arquivos .xlsx
with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:

    # Salva o primeiro DataFrame na primeira aba
    fluxo.to_excel(writer, sheet_name='fluxo_carga_resultado')

    # Salva o segundo DataFrame na segunda aba
    df_matriz_ybus.to_excel(writer, sheet_name='matriz_ybus_resultado')

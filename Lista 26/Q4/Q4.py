import pandas as pd
import asp

tabela = r'Tabela_fluxo4.xlsx'

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

fluxo = asp.fluxo_newton_raphson(df_fluxo, Ybus, iteracoes=3)
display(fluxo)

pd.DataFrame.to_excel(fluxo, 'resultado_fluxo.xlsx',
                      sheet_name='fluxo_carga_resultado')

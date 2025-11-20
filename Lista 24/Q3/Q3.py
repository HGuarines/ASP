# import numpy para operações com matrizes e complexos
import numpy as np
# importar pandas para manipulação de dados em excel
import pandas as pd

# importar dados do excel
try:
    df_fluxo = pd.read_excel(r'Tabela_fluxo3.xlsx',
                             sheet_name='fluxo_carga').fillna(0.0)
    df_ybus = pd.read_excel(r'Tabela_fluxo3.xlsx',
                            sheet_name='Ybus').fillna(0.0)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
    exit()

# função para montar a matriz Ybus a partir do dataframe


def matriz_ybus(df_ybus):
    try:
        # Encontra o número de barras corretamente
        n_barras = int(max(df_ybus['de_barra'].max(),
                       df_ybus['para_barra'].max()))

        # Inicializa Ybus
        Ybus = np.zeros((n_barras, n_barras), dtype=complex)

        # Admissão série (y_ij) e shunt (y_sh)
        z_lt = df_ybus['r_lt'] + 1j * df_ybus['x_lt']
        y_lt_serie = 1.0 / z_lt
        # y_lt no seu dado parece ser o b_shunt
        y_lt_shunt = 1j * df_ybus['y_lt']

        # Itera UMA VEZ sobre as linhas de transmissão
        for idx in range(len(df_ybus)):
            # Índices base 0
            i = int(df_ybus.loc[idx, 'de_barra']) - 1
            j = int(df_ybus.loc[idx, 'para_barra']) - 1

            y_serie = y_lt_serie[idx]
            y_shunt_half = y_lt_shunt[idx] / 2.0  # Modelo PI

            # Elementos Fora-Diagonal (Y_ij e Y_ji)
            Ybus[i, j] = Ybus[i, j] - y_serie
            Ybus[j, i] = Ybus[i, j]  # Matriz é simétrica

            # Elementos Diagonais (Y_ii e Y_jj)
            Ybus[i, i] = Ybus[i, i] + y_serie + y_shunt_half
            Ybus[j, j] = Ybus[j, j] + y_serie + y_shunt_half

        return Ybus
    except Exception as e:
        print(f"Ocorreu um erro ao montar a matriz Ybus: {e}")
        exit()


# chamando a função matriz ybus e imprimindo a matriz Ybus
Ybus = matriz_ybus(df_ybus)
print(Ybus)

# função para calcular o fluxo de carga


def fluxo_gauss_seidel(df_fluxo, Ybus, iteracoes=3):
    try:
        # número de barras
        n_barras = df_fluxo['n_barra'].max()
        # tipo de barra
        tipo = np.zeros(n_barras, dtype=str)
        tipo = df_fluxo['tipo_barra'].to_numpy()

        # inicializando matrizes de potência ativa e reativa calculadas
        Pi = np.zeros(n_barras)
        Qi = np.zeros(n_barras)
        # potência resultante em cada barra na iteração 0
        Pi = df_fluxo['Pgi'].to_numpy() - df_fluxo['Pci'].to_numpy()
        Qi = df_fluxo['Qgi'].to_numpy() - df_fluxo['Qci'].to_numpy()

        Pim = np.zeros((iteracoes + 1, n_barras))
        Pim[0] = Pi.copy()

        Qim = np.zeros((iteracoes + 1, n_barras), dtype=complex)
        Qim[0] = Qi.copy()

        # inicializando matrizes de magnitude e ângulo de tensão
        E = np.zeros((iteracoes, n_barras))
        E[0] = df_fluxo['Ei'].to_numpy()
        # inicializando matriz de ângulo de tensão
        sigma = np.zeros((iteracoes, n_barras))
        sigma[0] = df_fluxo['Fi'].to_numpy()
        # inicializando matriz de tensão complexa
        Vim = np.zeros((iteracoes+1, n_barras), dtype=complex)
        Vi = np.zeros((n_barras), dtype=complex)
        # calculando a tensão complexa inicial
        Vi = E[0] * np.exp(1j * sigma[0])
        for i in range(n_barras):
            if Vi[i] == 0j:
                Vi[i] = 1 + 0*1j  # barra swing com tensão 1∠0° inicial
        Vim[0] = Vi.copy()

        for i in range(iteracoes):

            for j in range(n_barras):

                if tipo[j] == 'PV':
                    somaYV = 0 + 0j
                    for k in range(n_barras):
                        somaYV = somaYV + Ybus[j][k] * Vi[k]
                    Qi[j] = -(somaYV * Vi[j].conj()).imag

                if tipo[j] != 'swing':

                    somaYV = 0 + 0j
                    for k in range(n_barras):
                        if j != k:
                            somaYV = somaYV + Ybus[j][k] * Vi[k]
                    Vi[j] = (1 / Ybus[j, j]) * \
                        (((Pi[j] - 1j * Qi[j]) / Vi[j].conj()) - somaYV)

                if tipo[j] == 'PV':

                    # Ei[j] é o array que armazena a magnitude fixa (ex: 1.05)
                    mag_fixa = E[0][j]
                    # Pega o ângulo do Vi[j] recém-calculado
                    angulo_novo = np.angle(Vi[j])
                    # Recria a tensão com a magnitude correta e o ângulo novo
                    Vi[j] = mag_fixa * \
                        (np.cos(angulo_novo) + 1j * np.sin(angulo_novo))

            for j in range(n_barras):
                if tipo[j] == 'swing':
                    somaYV = 0 + 0j
                    for k in range(n_barras):
                        somaYV = somaYV + Ybus[j][k] * Vi[k]
                    S_swing = (somaYV)*Vi[j].conj()
                    Pi[j] = S_swing.real
                    Qi[j] = -S_swing.imag

            Pim[i+1] = Pi.copy()
            Qim[i+1] = Qi.copy()
            Vim[i+1] = Vi.copy()

        Vi

        mag = np.abs(Vim)            # shape (z, n_barras)
        # ângulo em radianos, shape (z, n_barras)
        phasor = np.degrees(np.angle(Vim))
        potReativa = Qim
        Pswing = np.zeros((iteracoes + 1, n_barras))
        for b in range(n_barras):
            Pswing[iteracoes][b] = Pi[b] if tipo[b] == 'swing' else 0

        z = mag.shape[0]

        # 1. Crie os nomes das colunas com a condição 'if'
        mag_cols = [f'E_bar{b+1}' for b in range(n_barras) if tipo[b] == 'PQ']
        phasor_cols = [
            f'phi_bar{b+1}' for b in range(n_barras) if tipo[b] != 'swing']
        potReativa_cols = [
            f'Q_bar{b+1}' for b in range(n_barras) if tipo[b] != 'PQ']
        potAtiva_cols = [
            f'P_bar{b+1}' for b in range(n_barras) if tipo[b] == 'swing']

        # 2. Crie "máscaras" booleanas a partir das condições
        # (É crucial usar a mesma lógica dos 'ifs' acima)
        mask_mag = [tipo[b] == 'PQ' for b in range(n_barras)]
        mask_phasor = [tipo[b] != 'swing' for b in range(n_barras)]
        mask_potReativa = [tipo[b] != 'PQ' for b in range(n_barras)]
        mask_potAtiva = [tipo[b] == 'swing' for b in range(n_barras)]

        # 3. Filtre os DADOS (arrays numpy) usando as máscaras
        # O slicing ':, mask_...' seleciona TODAS as linhas (:)
        # e apenas as COLUNAS onde a máscara é True.
        mag_filtrado = mag[:, mask_mag]
        phasor_filtrado = phasor[:, mask_phasor]
        potReativa_filtrada = potReativa[:, mask_potReativa]
        potAtiva_filtrada = Pswing[:, mask_potAtiva]

        # 4. Agora sim, junte os nomes e os dados filtrados
        cols = mag_cols + phasor_cols + potReativa_cols + potAtiva_cols
        dados_filtrados = np.hstack(
            [mag_filtrado, phasor_filtrado, potReativa_filtrada, potAtiva_filtrada])

        # 5. Crie o DataFrame
        df_vim = pd.DataFrame(dados_filtrados, columns=cols, index=[
                              f'it_{i}' for i in range(z)])

        # exibe o DataFrame resultante
        df_vim

        # adiciona após cada coluna uma coluna com a diferença entre o valor atual e o da linha anterior
        # para a linha 0 a diferença é 0
        df = df_vim.copy()  # trabalhar numa cópia para reorganizar depois
        nova_ordem = []

        for col in df.columns:
            diff = df[col] - df[col].shift(1)
            diff.iloc[0] = 0  # primeira linha = 0
            diff_col = f"{col}_diff"
            df[diff_col] = diff
            nova_ordem.append(col)
            nova_ordem.append(diff_col)

        # atualiza df_vim com as colunas intercaladas (original, diferença)
        df_vim = df[nova_ordem]
        df_vim

        return df_vim

    except Exception as e:
        print(f"Ocorreu um erro durante o cálculo do fluxo de carga: {e}")
        exit()


fluxo = fluxo_gauss_seidel(df_fluxo, Ybus)
print(fluxo)

pd.DataFrame.to_excel(fluxo, 'resultado_fluxo3.xlsx',
                      sheet_name='fluxo_carga_resultado')

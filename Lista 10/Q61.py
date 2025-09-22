import asp


def fluxocarga(V1, z, yshunt, S, Kp=1.0, Ki=0.0, Kz=0.0):
    """
    Calcula a tensão na barra 2 (receptora) em um sistema de duas barras
    com linha de transmissão no modelo π e carga do tipo ZIP (constante potência,
    constante corrente e constante impedância).

    Parâmetros:
        V1     : tensão na barra transmissora (pu, número complexo)
        z      : impedância série da linha (pu, número complexo)
        yshunt : admitância shunt total da linha (pu, número complexo)
        S      : potência aparente da carga a 1 pu de tensão (P+jQ) (pu, número complexo)
        Kp     : fração da carga de potência constante   (0 ≤ Kp ≤ 1)
        Ki     : fração da carga de corrente constante   (0 ≤ Ki ≤ 1)
        Kz     : fração da carga de impedância constante (0 ≤ Kz ≤ 1)
                (Kp + Ki + Kz = 1)
    Retorno:
        V2     : tensão complexa na barra receptora (pu, número complexo)
    """

    import numpy as np
    from scipy.optimize import fsolve

    # Admitância série da linha
    Yserie = 1 / z

    # Admitância shunt é dividida entre as duas extremidades da linha (modelo π)
    Ysh_metade = yshunt / 2

    # Montagem da matriz Ybus do sistema de duas barras
    Ybus = np.array([[Yserie + Ysh_metade,           -Yserie],
                     [-Yserie,             Yserie + Ysh_metade]])

    # Função das equações não lineares (aplicada em fsolve)
    def equacoes(variaveis):
        Vr, Vi = variaveis  # componente real e imaginária de V2
        V2 = Vr + 1j*Vi     # tensão complexa na barra 2

        # Corrente fornecida pela rede ao nó 2
        I_rede = Ybus[1, 0]*V1 + Ybus[1, 1]*V2

        # Potência da carga conforme modelo ZIP
        Scarga = Kp * S
        Scarga += Ki * S * abs(V2)
        Scarga += Kz * S * (abs(V2)**2)

        # Corrente da carga (Icarga = conj(Scarga / V2))
        I_carga = np.conj(Scarga / V2)

        # Equação de balanço de corrente na barra 2
        # Corrente da rede + Corrente da carga = 0
        Ibal = I_rede + I_carga

        return [np.real(Ibal), np.imag(Ibal)]

    # Valor inicial (chute) para o fsolve: tensão próxima de 1 pu
    V2_inicial = [1.0, 0.0]
    sol = fsolve(equacoes, V2_inicial)

    return sol[0] + 1j*sol[1]


# Dados do sistema
V1 = 1.00 + 0j        # Tensão na Barra 1 (pu)
z = 0.01 + 0.1j       # Impedância série da linha (pu)
yshunt = 0 + 0.05j    # Admitância shunt total da linha (pu)
S = 1 + 0.5j          # Potência nominal da carga (pu) a 1 pu de tensão

# Fatores do modelo ZIP
Kp, Ki, Kz = 0.5, 0.3, 0.2

# Cálculo da tensão na Barra 2
V2 = fluxocarga(V1, z, yshunt, S, Kp, Ki, Kz)

# Preparação da resposta para arquivo texto
resposta = [('Q61', ''),
            ("\nDados do sistema:\n", ''),
            ("Tensão na Barra 1 (V1) = ", asp.format_complex(V1, 'p')),
            ("Impedância série da linha (z) = ", asp.format_complex(z, 'r')),
            ("Admitância shunt total da linha (yshunt) = ",
             asp.format_complex(yshunt, 'r')),
            ("Potência nominal da carga (S) = ", asp.format_complex(S, 'r')),
            ("Fatores do modelo ZIP: \nKp = {:.2f}; \nKi = {:.2f}; \nKz = {:.2f}".format(
                Kp, Ki, Kz), ''),
            ("\nResultado", ''),
            ("Tensão V2 = ", asp.format_complex(V2, 'p'))
            ]

asp.gerar_arquivo_texto(
    'Q61.txt', "Resultado circuito PI apresentado", resposta)

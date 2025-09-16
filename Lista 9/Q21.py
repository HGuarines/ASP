import asp
import numpy as np
import cmath

np.set_printoptions(precision=2, suppress=True)

# Testando com os ramos fornecidos pelo usuário
sistema = asp.SistemaEletrico(10)
# Usando exatamente as linhas de seu exemplo (aceitando formas variadas)
sistema.adicionar_ramo(0,  1,  0.8j,  0.0, 0.0, 1,     0,    "G1")
sistema.adicionar_ramo(1,  3,  0.14j, 0.0, 0.0, 0,     0,    "T1")
sistema.adicionar_ramo(3,  5,  0.2j,  0.0, 0.0, 0,     0,   "LT1")
sistema.adicionar_ramo(5,  7,  0.3j,  0.0, 0.0, 0,     0,   "LT5")
sistema.adicionar_ramo(7,  10, 0.15j, 0.0, 0.0, 0,     0,    "T3")
sistema.adicionar_ramo(10, 0,  1.0j,  0.0, 0.0, 0.98, -8,    "M1")
sistema.adicionar_ramo(3,  4,  0.3j,  0.0, 0.0, 0,     0,   "LT2")
sistema.adicionar_ramo(5,  6,  0.2j,  0.0, 0.0, 0,     0,   "LT4")
sistema.adicionar_ramo(0,  2,  0.9j,  0.0, 0.0, 1.02,  2,    "G2")
sistema.adicionar_ramo(2,  4,  0.12j, 0.0, 0.0, 0,     0,    "T2")
sistema.adicionar_ramo(4,  6,  0.4j,  0.0, 0.0, 0,     0,   "LT3")
sistema.adicionar_ramo(6,  8,  0.4j,  0.0, 0.0, 0,     0,   "LT6")
sistema.adicionar_ramo(8,  9,  0.15j, 0.0, 0.0, 0,     0,    "T4")
sistema.adicionar_ramo(9, 0,  0.9j,  0.0, 0.0, 0.95, -12,   "M2")

# Encontrando as matrizes Zbus e Ybus
Ybus, Zbus, *_ = sistema.calcular_matrizes_rede()

# Calculando os parâmetros da rede
i_ramo = sistema.calcular_parametros_rede()[2]
Vsi = sistema.calcular_parametros_rede()[1]

# Cálculo da corrente no delta de T3
a = cmath.rect(1, np.radians(120))
Iab = i_ramo[4][0]/(a - 1)   # Corrente no delta de T3

# Calculando tensão de T1 na baixa
Vt1 = Vsi[1][0]

# Gerar relatório com os resultados
calculos = [
    ("21.\n", ""),
    ("Matriz Ybus\n", Ybus),
    ("\nMatriz Zbus\n", Zbus),
    ("\nCorrente na LT1 (I35)\n", asp.format_complex(i_ramo[2][0], 'p')),
    ("\nCorrente na LT2 (I34)\n", asp.format_complex(i_ramo[6][0], 'p')),
    ("\nCorrente na LT3 (I46)\n", asp.format_complex(i_ramo[10][0], 'p')),
    ("\nCorrente na LT4 (I56)\n", asp.format_complex(i_ramo[7][0], 'p')),
    ("\nCorrente na LT5 (I57)\n", asp.format_complex(i_ramo[3][0], 'p')),
    ("\nCorrente na LT6 (I68)\n", asp.format_complex(i_ramo[11][0], 'p')),
    ("\nCorrente no delta de T3 (Iab)\n", asp.format_complex(Iab, 'p')),
    ("\nTensão de T1 na baixa (Vt1)\n", asp.format_complex(Vt1, 'p'))
]

asp.gerar_arquivo_texto(
    "Q21.txt", "Cálculo de Parâmetros da Rede Elétrica", calculos)

import asp


# Definição dos dados dos componentes
dadcomp = [
    (1, 2, 0, 0.9, 0.0),    # Ramo entre barras 1 e 2
    (2, 3, 0, 0.033, 0.0),  # Ramo entre barras 2 e 3
    (3, 4, 0, 0.022, 0.0),  # Ramo entre barras 3 e 4
    (2, 4, 0, 0.041, 0.0),  # Ramo entre barras 2 e 4
    (4, 1, 0, 1.478, 0.0)   # Ramo entre barras 4 e 1
]

# Uso da função
Ybus, Zbus = asp.YBUS("Sistema Elétrico 1", 4, 5,
                      dadcomp, "resultados_ybus.txt")

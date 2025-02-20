"17. """

import numpy as np
import asp
import matplotlib.pyplot as plt

# Definição dos números complexos para a parte (a)
za1 = (2 + 7j)
za2 = (5 - 2j)
za = za1 / za2

# Definição dos números complexos para a parte (b)
zb1 = (2 + 4j)
zb2 = (-7 - 3j)
modulo = 1.414  # Módulo do número polar
angulo = np.deg2rad(-60)  # Conversão para radianos
zb3 = modulo * np.exp(1j*angulo)
zb4 = (-1 + 5j)

# Resultado final da parte (b)
zb = (zb1 / zb2) + (zb3 / zb4)

# Resultado das expressões
rsp16 = [('\n17. ', ' '),
         ('(a) ', np.round(za, 2)),
         ('(b) ', np.round(zb, 2))]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp16)

# Plotando os números complexos no plano
fig, ax = plt.subplots()
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', linewidth=0.5)

# Números complexos envolvidos
numeros_complexos = {
    "Za TOTAL (a)": za,
    "Zb TOTAL (b)": zb,
    "Zb1": zb1/zb2,
    "Zb2": zb3/zb4
}

# Plotando os números
for rotulo, numero in numeros_complexos.items():
    plt.quiver(0, 0, numero.real, numero.imag, angles='xy',
               scale_units='xy', scale=1, color=np.random.rand(3,))
    plt.text(numero.real, numero.imag, rotulo,
             fontsize=12, verticalalignment='bottom')

# Configuração do gráfico
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Representação dos Números Complexos')

# Salvar o gráfico como imagem
plt.savefig("Q17_grafico.png", dpi=300, bbox_inches='tight')

plt.show()

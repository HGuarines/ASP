""" 9. Reproduza os comandos do PYTHON que permitem obter os gráficos da Figura 1
adicionando título e rótulo no eixo Y. """

import asp
import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo de x de 0 a 2π
x = np.linspace(0, 2 * np.pi, 100)

# Definir as funções
y1 = 2 * np.cos(x)    # 2*cos(x)
y2 = np.cos(x)        # cos(x)
y3 = 0.5 * np.cos(x)  # 0.5*cos(x)

# Criar o gráfico
plt.plot(x, y1, 'b--', label="2*cos(x)")   # Linha azul tracejada
plt.plot(x, y2, 'g-', label="cos(x)")      # Linha verde contínua
plt.plot(x, y3, 'r-.', label="0.5*cos(x)")  # Linha vermelha traço-ponto

# Adicionar título e rótulos
plt.xlabel(r"$0 \leq x \leq 2\pi$")  # Eixo X com notação matemática
plt.ylabel('Função cos(x)') # Adiciona um titulo e rotulo no eixo y
plt.legend()  # Adicionar legenda

# Salvar o gráfico como imagem
plt.savefig("Q9_grafico.png", dpi=300, bbox_inches='tight')

# Mostrar o gráfico
plt.show()


rsp9 = [
    ('\n9.', '\nBasta utilizar o comando ylabel() para adicionar um rótulo ao eixo y'),
    ("plt.ylabel('Função cos(x)')", " -> Adiciona o titulo 'Função cos(x)' no eixo y")
]

asp.gerar_arquivo_texto('Q9.txt',
                        'RESPOSTAS USO PYTHON', rsp9)

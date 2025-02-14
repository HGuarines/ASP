""" 8. Explique como os gráficos podem ser feitos no PYTHON. Apresente um arquivo que produza este gráfico. """

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
plt.legend()  # Adicionar legenda

# Salvar o gráfico como imagem
plt.savefig("Q8_grafico.png", dpi=300, bbox_inches='tight')

# Mostrar o gráfico
plt.show()


rsp8 = [
    ('\n8.', '\nPodemos gerar gráficos no python utilizando a biblioteca matplotlib'),
    ('Principais comandos', ':'),
    ('plot(): ', 'Plota o gráfico'),
    ('xlabel() e ylabel(): ', 'Criam os eixos horizontais e verticais respectivamente'),
    ('show(): ', 'Mostra o gráfico')
]

asp.gerar_arquivo_texto('pre_tarefa_uso_python_henrique.txt',
                        'RESPOSTAS USO PYTHON', rsp8)

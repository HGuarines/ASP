"""23.Apresente a equação do polinômio de segundo grau e de terceiro grau que
mais se aproxima do seguinte conjunto de pontos e plote os pontos e as curvas
que mais se aproximam de um conjunto de pontos."""


import numpy as np
import matplotlib.pyplot as plt
import asp
<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
=======
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79

# Dados fornecidos
x = np.array([0.9, 0.95, 1.00, 1.05, 1.10])
y1 = np.array([0.6924, 0.7456, 0.8, 0.8575, 0.9169])
y2 = np.array([0.5192, 0.5592, 0.6, 0.6427, 0.6879])

<<<<<<< HEAD
# Ajuste de polinômios
=======
# Ajuste de polinômios de grau 2 e 3
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
coeffs2_y1 = np.polyfit(x, y1, 2)
coeffs3_y1 = np.polyfit(x, y1, 3)
coeffs2_y2 = np.polyfit(x, y2, 2)
coeffs3_y2 = np.polyfit(x, y2, 3)

<<<<<<< HEAD
=======
# Funções polinomiais ajustadas
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
poly2_y1 = np.poly1d(coeffs2_y1)
poly3_y1 = np.poly1d(coeffs3_y1)
poly2_y2 = np.poly1d(coeffs2_y2)
poly3_y2 = np.poly1d(coeffs3_y2)

<<<<<<< HEAD
# Expandindo a faixa de x para evitar zoom excessivo
x_fit = np.linspace(min(x) - 0.9, max(x) + 0.9, 1000)

=======
# Gerando valores para o gráfico
x_fit = np.linspace(min(x), max(x), 100)
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
y1_fit2 = poly2_y1(x_fit)
y1_fit3 = poly3_y1(x_fit)
y2_fit2 = poly2_y2(x_fit)
y2_fit3 = poly3_y2(x_fit)

<<<<<<< HEAD
# Plotagem
plt.figure(figsize=(12, 5))

# Ajuste para y1
=======
# Plotagem dos dados e das curvas ajustadas
plt.figure(figsize=(10,5))

# Plot para o primeiro conjunto de pontos
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
plt.subplot(1, 2, 1)
plt.scatter(x, y1, color='red', label='Dados Originais')
plt.plot(x_fit, y1_fit2, label='Ajuste Grau 2', linestyle='dashed')
plt.plot(x_fit, y1_fit3, label='Ajuste Grau 3')
plt.title("Ajuste para y1")
plt.xlabel("x")
plt.ylabel("y1")
plt.legend()

<<<<<<< HEAD
# Ajustando os limites dos eixos para melhor visualização
plt.xlim(min(x) - 0.9, max(x) + 0.7)
plt.ylim(min(y1) - 0.9, max(y1) + 0.9)

# Ajuste para y2
=======
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
plt.subplot(1, 2, 2)
plt.scatter(x, y2, color='blue', label='Dados Originais')
plt.plot(x_fit, y2_fit2, label='Ajuste Grau 2', linestyle='dashed')
plt.plot(x_fit, y2_fit3, label='Ajuste Grau 3')
plt.title("Ajuste para y2")
plt.xlabel("x")
plt.ylabel("y2")
plt.legend()

<<<<<<< HEAD
# Ajustando os limites dos eixos
plt.xlim(min(x) - 0.4, max(x) + 0.4)
plt.ylim(min(y2) - 0.4, max(y2) + 0.6)

plt.tight_layout()
plt.savefig("Q23.png")
=======
plt.tight_layout()
plt.savefig('Q23.png')
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79
plt.show()


rsp23 = [('\n23. ', ' '),
<<<<<<< HEAD
         ('considerando os valores da segunda linha como y1\n',
          'E considerando os calores da terceira linha como y2, temos:'),
         ('Equação do polinômio de 2º grau para y1: ',
          f'{coeffs2_y1[0]:.4f}x² + {coeffs2_y1[1]:.4f}x + {coeffs2_y1[2]:.4f}'),
         ('Equação do polinômio de 3º grau para y1: ',
          f'{coeffs3_y1[0]:.4f}x³ + {coeffs3_y1[1]:.4f}x² + {coeffs3_y1[2]:.4f}x + {coeffs3_y1[3]:.4f}'),
         ('Equação do polinômio de 2º grau para y2: ',
          f'{coeffs2_y2[0]:.4f}x² + {coeffs2_y2[1]:.4f}x + {coeffs2_y2[2]:.4f}'),
         ('Equação do polinômio de 3º grau para y2: ', f'{coeffs3_y2[0]:.4f}x³ + {coeffs3_y2[1]:.4f}x² + {coeffs3_y2[2]:.4f}x + {coeffs3_y2[3]:.4f}')]

asp.gerar_arquivo_texto('Q23.txt',
                        'RESPOSTAS USO PYTHON', rsp23)
=======
         ('considerando os valores da segunda linha como y1\n', 'E considerando os calores da terceira linha como y2, temos:'),
         ('Equação do polinômio de 2º grau para y1: ', f'{coeffs2_y1[0]:.4f}x² + {coeffs2_y1[1]:.4f}x + {coeffs2_y1[2]:.4f}'),
         ('Equação do polinômio de 3º grau para y1: ', f'{coeffs3_y1[0]:.4f}x³ + {coeffs3_y1[1]:.4f}x² + {coeffs3_y1[2]:.4f}x + {coeffs3_y1[3]:.4f}'),
         ('Equação do polinômio de 2º grau para y2: ', f'{coeffs2_y2[0]:.4f}x² + {coeffs2_y2[1]:.4f}x + {coeffs2_y2[2]:.4f}'),
         ('Equação do polinômio de 3º grau para y2: ', f'{coeffs3_y2[0]:.4f}x³ + {coeffs3_y2[1]:.4f}x² + {coeffs3_y2[2]:.4f}x + {coeffs3_y2[3]:.4f}')]

asp.gerar_arquivo_texto('Q23.txt',
                        'RESPOSTAS USO PYTHON', rsp23)
>>>>>>> fc0ee377a0982cab8011d6911216b34bfef62b79

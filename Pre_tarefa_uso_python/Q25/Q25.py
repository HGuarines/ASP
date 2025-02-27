"""25. determine R"""

import numpy as np
import asp

a = np.log(4) + np.log10(34)
b = 35**2 + a**2
r = b**(1/4)

rsp25 = [('25.', ''),
         ('R = ', r)]

asp.gerar_arquivo_texto('Q25.txt',
                        'RESPOSTAS USO PYTHON', rsp25)

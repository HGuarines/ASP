import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt

# Criando o diagrama do circuito fechado
with schemdraw.Drawing() as d:
    fonte = d.add(elm.SourceSin().label('100V'))
    d.add(elm.Line().right().length(1))
    r = d.add(elm.Resistor().label('3Ω'))
    l = d.add(elm.Inductor().label('8Ω'))
    c = d.add(elm.Capacitor().label('4Ω'))
    d.add(elm.Line().down().length(3))
    d.add(elm.Line().left().to(fonte.end))  # Fecha o circuito corretamente

    d.draw()
    plt.savefig('Q22_circuito.png')
    plt.show()

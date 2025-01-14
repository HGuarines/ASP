# Exemplo 2
# Resolver um circuito RLC série em regime permanente senoidal.
# frequencia de 2 Hz 
# Obter a corrente e as tensões em cada elemento do circuito
# Obter a potência fornecida pela fonte
# Dados de entrada
import math
import cmath
import methodio as meth
R=2.0   # Resistencia em ohm
L=3.0   # Indutancia em H
C=1/4   # Capacitancia em F
f=2.0
Vs=meth.c_polar(10,30)  # Fonte de Tensão em Volt
#  Resolução
w=2*math.pi*f
Zr=R
Zl=(1j)*w*L
Zc=1/((1j)*w*C)
Zeq=Zr+Zl+Zc
I=Vs/Zeq
Vr=Zr*I
Vc=Zc*I
Vl=Zl*I
Sf=meth.pot_complexa1f(Vs,I)
titulo='     Circuito RLC série'
meth.Imprime_Titulo(titulo)
ident='Corrente no Circuito RLC serie'
meth.Imprime_Complexo (ident,I)
ident='Tensão no Resistor'
meth.Imprime_Complexo (ident,Vr)
ident='Tensão no Indutor'
meth.Imprime_Complexo (ident,Vl)
ident='Tensão no Capacitor'
meth.Imprime_Complexo (ident,Vc)
ident='Potencia Complexa da Fonte'
meth.Imprime_Complexo (ident,Sf)
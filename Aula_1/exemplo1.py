# Exemplo : Solução de Exercício Usando Python
#
# Problema:
# Obter a tensão no terminal transmissor de um alimentador cuja impedancia,
# tensão no terminal receptor e a carga são conhecidos.
# Dados: a carga (Nc, fpc , nfpc), a tensão no terminal receptor (Vfin)
# e a impedância do alimentador (zlt)
#
# Importação das Bibliotecas
#
import numpy as np
import methodio as meth
#
# Dados de Entrada
#
zlt=0.02+0.16j
Vfin=meth.c_polar(1.0,0.0)
Nc=0.60
fpc=0.8
nfpc="IND"
#
# Obter o módulo da corrente de carga
#
m_Ic=Nc/abs(Vfin)
#
# Obter a fase da corrente de carga
#
if nfpc=="IND":
   fase_Ic=-np.arccos(fpc)*180/np.pi
if nfpc=="RES":
   fase_Ic=np.arccos(0.0)
if nfpc=="CAP":
   fase_Ic=np.arccos(fpc)*180/np.pi
#
# Corrente de carga
#   
icarga=meth.c_polar(m_Ic,fase_Ic)
#
# Cálculo da tensão no início da LT
#
Vin=Vfin+zlt*icarga
# 
#  Mostro na tela os dados de entrada e resultado
#
titulo="Cálculo da Tensão no Transmissor"
meth.Imprime_Titulo(titulo)
#
linha1="             Dados de Entrada"
meth.Imprime_linha(linha1)
#
ident="      Impedancia da LT  "
meth.Imprime_Complexo(ident, zlt)
#
ident1="   Tensão Final da LT  "
meth.Imprime_Complexo(ident1, Vfin)
#
linha2="              Resultados"
meth.Imprime_linha(linha2)
#
ident2="   Corrente de Carga  "
meth.Imprime_Complexo(ident2, icarga)
#
ident3="    Tensão Inicio da LT  "
meth.Imprime_Complexo(ident3, Vin)
    
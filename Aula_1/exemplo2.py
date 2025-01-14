# Exemplo 2 : Solução Usando Python lendo e arquivos de texto e gravando
# os resultados em arquivo de texto 
#
# Problema:
# Obter a tensão no terminal transmissor de um alimentador cuja impedancia,
# tensão no terminal receptor e a carga são conhecidos.
# Dados: a carga (Nc, fpc , nfpc), a tensão no terminal receptor (Vfin)
# e a impedância do alimentador (zlt)
#
# Importação de Bibliotecas
#
import numpy as np
import methodio as meth
#
# Gerar um arquivo de dados de entrada tipo texto
#
f=open("dados.txt","w")
linha1="# Arquivo de Dados Caso: exemplo"
f.write(linha1+'\n')
linha2="# zlt"
f.write(linha2+'\n')
linha3="0.02+0.16j"
f.write(linha3+'\n')
linha4="# Vfin (modulo e fase)"
f.write(linha4+'\n')
linha5="1.0     0.0"
f.write(linha5+'\n')
linha6="# Nc(carga em pu  fator de potencia  natureza do FP )"
f.write(linha6+'\n')
linha7="0.6  0.8  IND"
f.write(linha7)
#
# Leitura do arquivo de Dados de Entrada
#
f=open("dados.txt","r")
comen=f.readline()
comen=f.readline()
szlt=f.read(10)     # Leitura do dado como string
zlt=complex(szlt)   # Converte o string em número complexo 
print(zlt)
comen=f.readline()
comen=f.readline()
smVfin=f.read(5)
mVfin=float(smVfin)
sfVfin=f.read(5)
fVfin=float(sfVfin)
Vfin=meth.c_polar(mVfin,fVfin)
print(Vfin)
comen=f.readline()
comen=f.readline()
sNc=f.read(5)
Nc=float(sNc)
sfpc=f.read(5)
fpc=float(sfpc)
nfpc=f.read(5)
print(Nc)
print(fpc)
print(nfpc)
#
#  Execução do cálculo dos resultados
#
if nfpc=="IND":
   fase_Ic=-np.arccos(fpc)*180/np.pi
if nfpc=="RES":
   fase_Ic=np.arccos(0.0)
if nfpc=="CAP":
   fase_Ic=np.arccos(fpc)*180/np.pi
m_Ic=Nc/abs(Vfin)
icarga=meth.c_polar(m_Ic,fase_Ic)
Vin=Vfin+zlt*icarga
#
#  Apresentar dados de entrada e saida na tela. 
#
titulo="Cálculo da Tensão no Transmissor"
meth.Imprime_Titulo(titulo)
linha1="             Dados de Entrada"
meth.Imprime_linha(linha1)
ident="      Impedancia da LT  "
meth.Imprime_Complexo(ident, zlt)
ident1="   Tensão Final da LT  "
meth.Imprime_Complexo(ident1, Vfin)
ident2="   Corrente de Carga  "
meth.Imprime_Complexo(ident2, icarga)
linha2="              Resultados"
meth.Imprime_linha(linha2)
ident3="    Tensão Inicio da LT  "
meth.Imprime_Complexo(ident3, Vin)
#
#  Apresentar dados de entrada e saida em arquivo. 
#
nome_arq="saida.txt"
meth.A_Imprime_Titulo(nome_arq,titulo)
meth.A_Imprime_linha(nome_arq,linha1)
meth.A_Imprime_Complexo(nome_arq,ident,zlt)
meth.A_Imprime_Complexo(nome_arq,ident1,Vfin)
meth.A_Imprime_Complexo(nome_arq,ident2,icarga)
meth.A_Imprime_linha(nome_arq,linha2)
meth.A_Imprime_Complexo(nome_arq,ident3, Vin)


# Biblioteca methodio
import numpy as np
from datetime import datetime

def c_polar(m1,f1):
    A = m1*np.cos(f1*np.pi/180.0)+1j*m1*np.sin(f1*np.pi/180.0)
    return A

def soma_polar(m1,f1,m2,f2):
    soma=c_polar(m1,f1)+c_polar(m2,f2)
    return soma

def subt_polar(m1,f1,m2,f2):
    subt=c_polar(m1,f1)-c_polar(m2,f2)
    return subt

def mult_polar(m1,f1,m2,f2):
    mult=c_polar(m1,f1)*c_polar(m2,f2)
    return mult

def div_polar(m1,f1,m2,f2):
    div=c_polar(m1,f1)/c_polar(m2,f2)
    return div

def ret_polar(real,imagi):
    modu=np.sqrt(real**2+imagi**2)
    if real < 0.0:
      fase=np.arctan(imagi/real)*180.0/np.pi+180.0  
    else:
      fase=np.arctan(imagi/real)*180.0/np.pi    
    return (modu,fase)

def polar_ret(modu,fasegraus):
    A = modu*np.cos(fasegraus*np.pi/180.0)+1j*modu*np.sin(fasegraus*np.pi/180.0)
    return A

def Imprime_Matriz (titulo,Mat, nL, nC) :
    linha1='\n*****************************************\n'  
    print(linha1) 
    print('            '+titulo) 
    print(linha1) 
    for i in range(0, nL) : # i entre 0 e nL-1
       for j in range(0, nC) :
           p=int(i+1)
           q=int(j+1)
           print(' Matriz_A(% 2d,% 2d) = %4.3f' % (p,q,Mat[i,j]))
    print(linha1)   

def Imprime_Complexo (ident,A) :
    linha1='*********************************************'  
    print(linha1) 
    print('       '+ident) 
    print(linha1) 
    ang_graus=np.angle(A)*180.0/np.pi
    print (' Módulo : %5.3f     Fase (graus) : %5.2f'%(abs(A),ang_graus))
    print (' P Real : %5.3f     Parte   Imag : %5.3f'%(np.real(A),np.imag(A)))
    print(linha1+'\n')   

def A_Imprime_Complexo (nome_arq,ident,A) :
    linha1='*********************************************'  
    f=open(nome_arq,"a")
    f.write(linha1+'\n')
    f.write('       '+ident+'\n') 
    f.write(linha1+'\n')
    ang_graus=np.angle(A)*180.0/np.pi
    f.write(' Módulo : %5.3f     Fase (graus) : %5.2f'%(abs(A),ang_graus))
    f.write('\n')
    f.write(' P Real : %5.3f     Parte   Imag : %5.3f'%(np.real(A),np.imag(A)))
    f.write('\n')
    f.write(linha1+'\n')
    f.close()

def Imprime_Titulo(titulo):
    linhai='\n'+45*"*" 
    linhaf=45*"*"+'\n' 
    print(linhai) 
    print('     '+titulo)
    print("            Methodio Godoy     ")
    print('    % 20s'%datetime.today().strftime('%d-%m-%Y'))
    print(linhaf) 

def A_Imprime_Titulo(nome_arq,titulo):
    f=open(nome_arq,"w")
    linhai='\n'+45*"*" 
    linhaf=45*"*"+'\n' 
    f.write(linhai+'\n')
    f.write('     '+titulo+'\n')
    f.write("            Methodio Godoy     "+'\n')
    f.write('    % 20s'%datetime.today().strftime('%d-%m-%Y')+'\n')
    f.write(linhaf+'\n')    

def Imprime_linha(linha):
    linhai=45*"*" 
    linhaf=45*"*"
    print(linhai) 
    print(linha)
    print(linhaf) 

def A_Imprime_linha(nome_arq,linha):
    f=open(nome_arq,"a")
    linhai=45*"*" 
    linhaf=45*"*" 
    f.write(linhai+'\n')
    f.write(linha+'\n')
    f.write(linhaf+'\n')
    
def s_carga(Po,a0,a1,a2,Qo,b0,b1,b2,Vc):
    Sc = Po*(a0+a1*Vc+a2*(Vc**2))+1j*Qo*(b0+b1*Vc+b2*(Vc**2))
    return Sc

def imprime_modelcarga(Po,a0,a1,a2,Qo,b0,b1,b2,Vc):
    linhai='\n'+45*"*"
    linhaf=45*"*"+'\n' 
    linham=45*"*" 
    print(linhai) 
    print('           MODELO DE CARGA   ')
    print(linham)
    print("           POTÊNCIA ATIVA     ")
    print('   Po = %6.3f  (na tensão de 1 pu)'%Po)
    print(' a0 = %5.2f    a1 = %5.2f  a2 = %5.2f'%(a0,a1,a2))
    print(linham)
    print("          POTÊNCIA REATIVA     ")
    print('   Qo = %6.3f  (na tensão de 1 pu)'%Qo)
    print(' b0 = %5.2f    b1 = %5.2f  b2 = %5.2f'%(b0,b1,b2))
    print(linhaf)
    return
    
    
# Calcular o valor de um Polinômio
# Coeficientes do maior para o menor
# separado por vírgula
def funcao(coeficientes, x):
    expoente = len(coeficientes)-1
    resultado = 0
    for c in coeficientes:
        resultado = resultado + c * x ** expoente
        expoente=expoente-1
    return resultado    
import math,numpy
'''
                _________________________________________   
               |                                         |      
               |        QUESTÃO 35 - TAREFA 6            |  
               |                                         |  
               |    ANÁLISE DE SISTEMAS DE POTÊNCIA I    |  
               |                                         |  
               |              CALIL GOMES                | 
               |                                         |  
               |    DATA REALIZAÇÃO: 21/06/2023          |  
               |_________________________________________|

'''

'''1° STEP:      Declarando nossos dados da questão'''
#______________________________________
#           Gerador 1 (G1)             | 
#______________________________________|
Sg1 = math.prod([30, math.pow(10,6)]) #MVA
Vg1 = math.prod([15,math.pow(10,3)]) #KV
Xg1 = 0.9 #PU
#______________________________________
#       Transformador 1 (T1)           | 
#______________________________________|
St1 = math.prod([35,math.pow(10,6)]) #MVA
Vt1P = math.prod([230,math.pow(10,3)]) #KV
Vt1S = math.prod([16,math.pow(10,3)])  #KV
Xt1 = 0.05 #PU
#______________________________________
#              LT's                    | 
#______________________________________|
Xlt = 40 + 300j #PU
#______________________________________
#              T2                      | 
#______________________________________|
St2P = math.prod([30,math.pow(10,6)]) #MVA
St2S = math.prod([20,math.pow(10,6)]) #MVA
St2T = math.prod([20,math.pow(10,6)]) #MVA
Vt2P = math.prod([230,math.pow(10,3)])#KV
Vt2S = math.prod([6.6,math.pow(10,3)])#KV
Vt2T = math.prod([6.6,math.pow(10,3)])#KV
Xps = 0.16 #PU
Xpt = 0.14 #PU
Xst = 0.14 #PU
#______________________________________
#               M1                     |
#______________________________________|
Sm1 = math.prod([15,math.pow(10,6)]) #MW
Vm1 = math.prod([6.5,math.pow(10,3)])#KV
Xm1 = 0.8 #PU
Nm1 = 0.89 
FPm1 = 0.88 
#______________________________________
#               M2                     | 
#______________________________________|
Sm2 = math.prod([10,math.pow(10,6)]) #MW
Vm2 = math.prod([6.5,math.pow(10,3)])#KV
Xm2 = 0.8 #PU
Nm2 = 0.89
FPm2 = 0.88

'''2° STEP:      Calculando valores bases da questão'''
# Adotando o valor da potência base à critério
Sb = math.prod([50,math.pow(10,6)])
Vb1 = math.prod([15,math.pow(10,3)])
Vb2 = math.prod([Vb1,(Vt1P/Vt1S)])
Vb3 = math.prod([Vb2,(Vt2S/Vt2P)])

'''3° STEP:      Transformação de base'''
Zg1 = (Xg1 * (Sb/Sg1) * ((Vg1/Vb1)**2))
Zt1 = (Xt1 * (Sb/St1) * ((Vt1S/Vb1)**2)) 
Zlt1= Xlt/ ((Vb2**2)/Sb)
Zlt1_real = round(Zlt1.real,3)
Zlt1_imag = round(Zlt1.imag,3)*(1j)
Zlt1 = Zlt1_real + Zlt1_imag
Zlt2 = Zlt1
Zps = round((Xps * (Sb/St2P) *((Vt2P/Vb2)**2)),2) 
Zpt = round((Xpt * (Sb/St2P) * ((Vt2P/Vb2)**2)),2)
Zst = round((Xst * (Sb/St2T) * ((Vt2T/Vb3)**2)),2) 
Zp = (1/2) * (Zps + Zpt - Zst)
Zs = (1/2) * (Zps + Zst - Zpt)
Zt = (1/2) * (Zpt + Zst - Zps)
Zm1 = round((Xm1 * (Sb/(Sm1/(Nm1*FPm1))) * ((Vm1/Vb3)**2) ),2) 
Zm2 = round((Xm2 * (Sb/(Sm2/(Nm2*FPm2))) * ((Vm2/Vb3)**2) ),2) 


'''4° STEP:      Plotando Diagrama de Impedância'''     
diagram = f''' 
                                                                              |       
                                                                _ _ _|{Zs}j|--|--|{Zm1}j|--
                 |            |----|{Zlt1}j|-----|             /              |            |
 -G1--|{Zg1}j|---|--|{Zt1}j|--|                  |---|{Zp}j|---               |            |  
|                |            |----|{Zlt2}j|-----|             \_ _ _|{Zt}j|--|--|{Zm2}j|--|
|_____________________________________________________________________________|____________|

               ''' 

'''5° STEP:      Achando a admitância'''
Yg1 = round(-(1/Zg1),2) 
Yt1 = round(-(1/Zt1),2)
Ylt1 = -(1/Zlt1) 
Ylt2 = Ylt1
Yp = round((1/Zp),2) 
Ys = round(-(1/Zs),2)
Yt = round(-(1/Zt),2)
Ym1 = round(-(1/Zm1),2)
Ym2 = round(-(1/Zm2),2)

'''6° STEP:      Achando a admitância'''
# O sistem possui 5 equações linearmente independentes: 6 - 1 = 5
# Então nossa matriz será 5x5
Lin1 = numpy.array([Yg1+Yt1,Yt1,0,0,0])
Lin2 = numpy.array([Yt1,Yt1 + ((Ylt1*Ylt2) / (Ylt1/Ylt2)),((Ylt1*Ylt2) / (Ylt1/Ylt2)),0,0] )
Lin3 = numpy.array([0,((Ylt1*Ylt2) / (Ylt1/Ylt2)),((Ylt1*Ylt2) / (Ylt1/Ylt2)) + (Yp + ((Ys*Yt)/(Ys+Yt))) ,Yp + Ys, Yp + Yt])
Lin4 = numpy.array([0,0,Yp + Ys, Ym1 + Ys + Yp + Yt, Ys + Yt])
Lin5 = numpy.array([0,0,0,Ys + Yt,Ym2 + Yp + Yt + Ys])
Elementos = numpy.array([Lin1,Lin2,Lin3,Lin4,Lin5])
Matrix = numpy.array(Elementos)
print(Matrix)
import numpy as np
import pandas as pd
import math
import time
import random
import statistics

vetor=[]
vetor1=[]
vetor2=[]
vetor3=[]
vetor4=[]

tempo1=[]
tempo2=[]
tempo3=[]
tempo4=[]
tempo5=[]

def Repetir_meu_código(vezes):
    
    for v in range(vezes):
        
        df=pd.read_csv('dj38.csv')
        v1 = df['11003'].to_numpy()
        v2 = df['42102'].to_numpy()
        random.shuffle(v1)
        random.shuffle(v2)
        display(v1)
        display(v2)
        tempo=(len(v1)*60)/1000
        time.sleep(tempo)
        dist = np.linalg.norm(v1-v2)
        vetor.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo1.append(tempo)
        print("tempo=",round(tempo))
        
        
        df=pd.read_csv('qa194.csv')
        v3 = df['24748'].to_numpy()
        v4 = df['50840'].to_numpy()
        random.shuffle(v3)
        random.shuffle(v4)
        display(v3)
        display(v4)
        tempo80=(len(v3)*60)/1000
        time.sleep(tempo80)
        dist = np.linalg.norm(v3-v4)
        vetor1.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo2.append(tempo80)
        print("tempo=",round(tempo80))
        
        
        df=pd.read_csv('wi29.csv')
        v5 = df['20833'].to_numpy()
        v6 = df['17100'].to_numpy()
        random.shuffle(v5)
        random.shuffle(v6)
        display(v5)
        display(v6)
        tempo90=(len(v5)*60)/1000
        time.sleep(tempo90)
        dist = np.linalg.norm(v5-v6)
        vetor2.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo3.append(tempo90)
        print("tempo=",round(tempo90))
        
        
        df=pd.read_csv('uy734.csv')
        v7 = df['30133'].to_numpy()
        v8 = df['57633'].to_numpy()
        random.shuffle(v7)
        random.shuffle(v8)
        display(v7)
        display(v8)
        tempo70=(len(v7)*60)/1000
        time.sleep(tempo70)
        dist = np.linalg.norm(v7-v8)
        vetor3.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo4.append(tempo70)
        print("tempo=",round(tempo70))
        
        
        df=pd.read_csv('zi929.csv')
        v9 = df['15700'].to_numpy()
        v10 =df['30316'].to_numpy()
        random.shuffle(v9)
        random.shuffle(v10)
        display(v9)
        display(v10)
        tempo40=(len(v9)*60)/1000
        time.sleep(tempo40)
        dist = np.linalg.norm(v9-v10)
        vetor4.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo5.append(tempo40)
        print("tempo=",round(tempo40))
        
        
Repetir_meu_código(10) # Repetir 10 vezes
instancia=['Djibouti','Qatar','Uruguay','Western Sahara', 'Zimbabwe']
autoria=['Sebastien','Sebastien','Sebastien','Sebastien','Sebastien']
algoritmo=['BTA','BTA','BTA','BTA','BTA']
q_medio=[]
q_desvio=[]
t_medio=[]

print("djibouti=",vetor)
print(q_medio.append(round(np.average(vetor))))
print(q_desvio.append(np.std(vetor)))
print(t_medio.append(round(np.average(tempo1))))

print("qatar=",vetor1)
print(q_medio.append(round(np.average(vetor1))))
print(q_desvio.append(np.std(vetor1)))
print(t_medio.append(round(np.average(tempo2))))

print("Western Sahara=",vetor2)
print(q_medio.append(round(np.average(vetor2))))
print(q_desvio.append(np.std(vetor2)))
print(t_medio.append(round(np.average(tempo3))))

print("Uruguay=",vetor3)
print(q_medio.append(round(np.average(vetor3))))
print(q_desvio.append(np.std(vetor3)))
print(t_medio.append(round(np.average(tempo4))))

print("zimbabwe=",vetor4)
print(q_medio.append(round(np.average(vetor4))))
print(q_desvio.append(np.std(vetor4)))
print(t_medio.append(round(np.average(tempo5))))

ds=pd.DataFrame(zip(instancia,autoria,algoritmo,q_medio,q_desvio,t_medio),columns=['instancia','autoria','algoritmo','q_medio','q_desvio','t_medio'])
print(ds)


ds.to_csv('resultados.csv', encoding='utf-8', index=False)
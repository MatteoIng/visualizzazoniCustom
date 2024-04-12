import json

import matplotlib.pyplot as plt
import numpy as np

dati = ''

file_uno = '/home/matteo/Documenti/tesi/reward_mosse_Diff_PPO_0.9_0-7,16-23_cpu_1000_75.txt'
file_due = '/home/matteo/Documenti/tesi/reward_mosse_Diff_PPO_0.9_gpu_1000_75_cuda.txt'
""" file_tre = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_PPO_0.9_0-3.txt'
file_quattro = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_PPO_0.9_0-7.txt'
file_cinque = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_PPO_0.9_0-7,10-17.txt'
 """
fig, ax = plt.subplots()
#plt.ylim(-6,-1)

#with open(pathCompleto, "r") as file:
with open(file_uno, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']


yA = []
yB = []
tempo = []

aPPEND = 0
bPPEND = 0
sommaTempo = 0

sommaMosse = 0
mossePartitaCpu =[]
mossePartitaGpu =[]


count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempo = bpp[i][2]
    sommaMosse += bpp[i][0] 

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        mossePartitaCpu.append(sommaMosse/10)
        sommaMosse = 0
        aPPEND = 0
        bPPEND = 0
        

plt.plot(np.arange(13000),[-1.4 for i in range(13000)],label='ottimo', color='orange')



# Plotta i dati
ax.plot(tempo,yB,label='CPU',color='green')
ax.set_xlabel('secondi')
ax.set_xlim(0,13000)


plt.ylabel('reward')


#-------------------------------------------------------------------------------------------------------------------------
sommaMosse = 0

with open(file_due, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']
""" print('APP:',app)
print('BPP:',bpp) """

yA = []
yB = []
tempo = []

aPPEND = 0
bPPEND = 0
sommaTempo = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempo = bpp[i][2]
    sommaMosse +=bpp[i][0]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        mossePartitaGpu.append(sommaMosse/10)
        sommaMosse = 0
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempo,yB,label='GPU',color='yellow')
ax.set_xlabel('secondi')
ax.set_xlim(0,13000)


#-------------------------------------------------------------------------------------------------------------------------
""" 
with open(file_tre, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']

yA = []
yB = []
tempo = []

aPPEND = 0
bPPEND = 0
sommaTempo = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempo = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempo,yB,label='0-3',color='black')
ax.set_xlabel('secondi')
ax.set_xlim(0,6000)


#-------------------------------------------------------------------------------------------------------------------------


with open(file_quattro, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']

yA = []
yB = []
tempo = []

aPPEND = 0
bPPEND = 0
sommaTempo = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempo = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempo,yB,label='0-7',color='purple')
ax.set_xlabel('secondi')
ax.set_xlim(0,6000)


#-------------------------------------------------------------------------------------------------------------------------


with open(file_cinque, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']

yA = []
yB = []
tempo = []

aPPEND = 0
bPPEND = 0
sommaTempo = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempo = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        
# Plotta i dati
ax.plot(tempo,yB,label='0-7,10-17',color='gray')
ax.set_xlabel('secondi')
ax.set_xlim(0,6000) """

plt.legend()

plt.figure()
plt.plot(np.arange(len(mossePartitaCpu)),mossePartitaCpu,label='CPU',color='blue')
plt.plot(np.arange(len(mossePartitaGpu)),mossePartitaGpu,label='GPU',color='red')
plt.legend()

plt.show()

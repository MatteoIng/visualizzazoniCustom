import json

import matplotlib.pyplot as plt
import numpy as np

dati = ''

file_uno = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_PPO_0.9_0.txt'
file_due = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_PG_0.9_0-1.txt'
file_tre = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_DQN_0.9_0-3.txt'
file_quattro = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_Impala_0.9_0-7.txt'
file_cinque = '/home/matteo/Documenti/tesi/grafici3/dif/reward_mosse_Diff_Apex_0.9_0-7,10-17.txt'

fig, ax = plt.subplots()
plt.ylim(-4,0)

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
        

plt.plot(np.arange(1200),[-1.4 for i in range(1200)],label='ottimo', color='orange')



# Plotta i dati
ax.plot(tempo,yB,label='PPO',color='green')
ax.set_xlabel('secondi')
ax.set_xlim(0,1200)


plt.ylabel('reward')


#-------------------------------------------------------------------------------------------------------------------------

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

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempo,yB,label='PG',color='yellow')
ax.set_xlabel('secondi')
ax.set_xlim(0,1200)


#-------------------------------------------------------------------------------------------------------------------------

with open(file_tre, "r") as file:
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

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempo,yB,label='DQN',color='black')
ax.set_xlabel('secondi')
ax.set_xlim(0,1200)


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
ax.plot(tempo,yB,label='Impala',color='purple')
ax.set_xlabel('secondi')
ax.set_xlim(0,1200)


#-------------------------------------------------------------------------------------------------------------------------


with open(file_cinque, "r") as file:
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

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempo.append(sommaTempo)
        aPPEND = 0
        bPPEND = 0
        
# Plotta i dati
ax.plot(tempo,yB,label='Apex',color='gray')
ax.set_xlabel('secondi')
ax.set_xlim(0,1200)

plt.legend()

plt.show()

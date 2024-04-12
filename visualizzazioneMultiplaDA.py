import json

import matplotlib.pyplot as plt
import numpy as np

dati = ''

file_uno = '/home/matteo/Documenti/tesi/grafici3/dif-att/reward_mosse_PPO_0.9_0.txt'
file_due = '/home/matteo/Documenti/tesi/grafici3/dif-att/reward_mosse_PPO_0.9_0-1.txt'
file_tre = '/home/matteo/Documenti/tesi/grafici3/dif-att/reward_mosse_PPO_0.9_0-3.txt'
file_quattro = '/home/matteo/Documenti/tesi/grafici3/dif-att/reward_mosse_PPO_0.9_0-7.txt'
file_cinque = '/home/matteo/Documenti/tesi/grafici3/dif-att/reward_mosse_PPO_0.9_0-7,10-17.txt'
fig, ax = plt.subplots()

#with open(pathCompleto, "r") as file:
with open(file_uno, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']


yA = []
yB = []
tempoA = []
tempoB = []

aPPEND = 0
bPPEND = 0
sommaTempoA = 0
sommaTempoB = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempoA = app[i][2]
    sommaTempoB = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempoA.append(sommaTempoA)
        tempoB.append(sommaTempoB)
        aPPEND = 0
        bPPEND = 0
        

# Crea il grafico
fig, ax = plt.subplots()
plt.plot(np.arange(2500),[-0.1 for i in range(2500)], label='ottimo Attaccante' ,color='orange')
plt.plot(np.arange(2500),[0 for i in range(2500)], label='ottimo Difensore' ,color='pink')

plt.ylim(-2,0.1)

# Plotta i dati
ax.plot(tempoA,yA, label='0 Attaccante' ,color='darkgreen')
ax.set_xlabel('secondi')
ax.plot(tempoB,yB ,label='0 Difensore' ,color='green')
ax.set_xlabel('secondi')
ax.set_xlim(0,2500)



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
tempoA = []
tempoB = []

aPPEND = 0
bPPEND = 0
sommaTempoA = 0
sommaTempoB = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempoA = app[i][2]
    sommaTempoB = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempoA.append(sommaTempoA)
        tempoB.append(sommaTempoB)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempoA,yA, label='0-1 Attaccante' ,color='darkred')
ax.plot(tempoB,yB,label='0-1 Difensore' ,color='red')
ax.set_xlabel('secondi')
ax.set_xlim(0,2500)


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
tempoA = []
tempoB = []

aPPEND = 0
bPPEND = 0
sommaTempoA = 0
sommaTempoB = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempoA = app[i][2]
    sommaTempoB = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempoA.append(sommaTempoA)
        tempoB.append(sommaTempoB)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempoA,yA,label='0-3 Attaccante' ,color='darkmagenta')
ax.plot(tempoB,yB,label='0-3 Difensore' ,color='magenta')
ax.set_xlabel('secondi')
ax.set_xlim(0,2500)

#-------------------------------------------------------------------------------------------------------------------------


with open(file_quattro, "r") as file:
    dati = file.read()
dati_dict = json.loads(dati)

# reward per epoca
app = dati_dict['attaccante']
bpp = dati_dict['difensore']
""" print('APP:',app)
print('BPP:',bpp) """

yA = []
yB = []
tempoA = []
tempoB = []

aPPEND = 0
bPPEND = 0
sommaTempoA = 0
sommaTempoB = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempoA = app[i][2]
    sommaTempoB = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempoA.append(sommaTempoA)
        tempoB.append(sommaTempoB)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempoA,yA, label='0-7 Attaccante' ,color='darkcyan')
ax.plot(tempoB,yB, label='0-7 Difensore' ,color='cyan')
ax.set_xlabel('secondi')
ax.set_xlim(0,2500)


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
tempoA = []
tempoB = []

aPPEND = 0
bPPEND = 0
sommaTempoA = 0
sommaTempoB = 0

count = 0
for i in range(len(app)):
    aPPEND += app[i][1]
    bPPEND += bpp[i][1]
    sommaTempoA = app[i][2]
    sommaTempoB = bpp[i][2]

    count +=1
    if count == 10:
        count = 0

        yA.append(aPPEND/10)
        yB.append(bPPEND/10)
        tempoA.append(sommaTempoA)
        tempoB.append(sommaTempoB)
        aPPEND = 0
        bPPEND = 0
        

# Plotta i dati
ax.plot(tempoA,yA, label='0-7,10-17 Attaccante' ,color='orange')
ax.plot(tempoB,yB, label='0-7,10-17 Difensore' ,color='orange')
ax.set_xlabel('secondi')
ax.set_xlim(0,2500)

plt.legend()

plt.show()

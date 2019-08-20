import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

partidos2015 = []
partidos2016 = []
partidos2017 = []
partidos2018 = []

dataOf2015 = pd.read_csv("data/votacoes_2015.csv",",").sort_values('partido')
dataOf2016 = pd.read_csv("data/votacoes_2016.csv",",").sort_values('partido')
dataOf2017 = pd.read_csv("data/votacoes_2017.csv",",").sort_values('partido')
dataOf2018 = pd.read_csv("data/votacoes_2018.csv",",").sort_values('partido')

nvotes2015 = dataOf2015.groupby("partido").count()
nvotes2016 = dataOf2016.groupby("partido").count()
nvotes2017 = dataOf2017.groupby("partido").count()
nvotes2018 = dataOf2018.groupby("partido").count()

#############################
for i in range(len(dataOf2015)):
	if dataOf2015.partido[i] not in partidos2015:
		partidos2015.append(dataOf2015.partido[i])

partidos2015.sort()
for i in range(len(nvotes2015.voto)):
	partidos2015[i] = [(partidos2015[i],nvotes2015.voto[i])]

#############################
for i in range(len(dataOf2016)):
	if dataOf2016.partido[i] not in partidos2016:
		partidos2016.append(dataOf2016.partido[i])

partidos2016.sort()
for i in range(len(nvotes2016.voto)):
	partidos2016[i] = [(partidos2016[i],nvotes2016.voto[i])]

#############################
for i in range(len(dataOf2017)):
	if dataOf2017.partido[i] not in partidos2017:
		partidos2017.append(dataOf2017.partido[i])

partidos2017.sort()
for i in range(len(nvotes2017.voto)):
	partidos2017[i] = [(partidos2017[i],nvotes2017.voto[i])]

#############################
for i in range(len(dataOf2018)):
	if dataOf2018.partido[i] not in partidos2018:
		partidos2018.append(dataOf2018.partido[i])

partidos2018.sort()
for i in range(len(nvotes2018.voto)):
	partidos2018[i] = [(partidos2018[i],nvotes2018.voto[i])]
print("###DATA OF 2015###")
print(partidos2015)
print("\n###DATA OF 2016###")
print(partidos2016)
print("\n###DATA OF 2017###")
print(partidos2017)
print("\n###DATA OF 2018###")
print(partidos2018)

print(":)")

#coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Dicionario responsavel por guardar votos de cada partido
votes = {}

#Listas responsaveis por guardar e relacionar partidos e quantidade de votos no ano
partidos2015 = []
partidos2016 = []
partidos2017 = []
partidos2018 = []

#Leitura e organização de dados obtidos atraves dos csv's dos anos de 2015, 2016, 2017 e 2018
dataOf2015 = pd.read_csv("data/votacoes_2015.csv",",").sort_values('partido')
dataOf2016 = pd.read_csv("data/votacoes_2016.csv",",").sort_values('partido')
dataOf2017 = pd.read_csv("data/votacoes_2017.csv",",").sort_values('partido')
dataOf2018 = pd.read_csv("data/votacoes_2018.csv",",").sort_values('partido')

#Realizando contagem de votos para conseguir de cada partido
nvotes2015 = dataOf2015.groupby("partido").count()
nvotes2016 = dataOf2016.groupby("partido").count()
nvotes2017 = dataOf2017.groupby("partido").count()
nvotes2018 = dataOf2018.groupby("partido").count()



###########################--2015--################################
#Agrupando votos por partido em lista
for i in range(len(dataOf2015)):
	if dataOf2015.partido[i] not in partidos2015:
		partidos2015.append(dataOf2015.partido[i])

#Reagrupando partidos junto aos votos relacionados a ele 
partidos2015.sort()
for i in range(len(nvotes2015.voto)):
	partidos2015[i] = (partidos2015[i],nvotes2015.voto[i])

###########################--2016--################################
#Agrupando partidos em lista
for i in range(len(dataOf2016)):
	if dataOf2016.partido[i] not in partidos2016:
		partidos2016.append(dataOf2016.partido[i])

#Reagrupando partidos junto aos votos relacionados a ele 
partidos2016.sort()
for i in range(len(nvotes2016.voto)):
	partidos2016[i] = (partidos2016[i],nvotes2016.voto[i])

###########################--2017--################################
#Agrupando partido em lista
for i in range(len(dataOf2017)):
	if dataOf2017.partido[i] not in partidos2017:
		partidos2017.append(dataOf2017.partido[i])

#Reagrupando partidos junto aos votos relacionados a ele 
partidos2017.sort()
for i in range(len(nvotes2017.voto)):
	partidos2017[i] = (partidos2017[i],nvotes2017.voto[i])
###########################--2018--################################
#Agrupando partido em lista
for i in range(len(dataOf2018)):
	if dataOf2018.partido[i] not in partidos2018:
		partidos2018.append(dataOf2018.partido[i])

#Reagrupando partidos junto aos votos relacionados a ele 
partidos2018.sort()
for i in range(len(nvotes2018.voto)):
	partidos2018[i] = (partidos2018[i],nvotes2018.voto[i])
"""
print("###DATA OF 2015###")
print(partidos2015)
print("\n###DATA OF 2016###")
print(partidos2016)
print("\n###DATA OF 2017###")
print(partidos2017)
print("\n###DATA OF 2018###")
print(partidos2018)
"""

#Agrupando partidos e votos de todos os anos relacionados a ele em dicionario
###########################--2015--################################
for i in range(len(partidos2015)):
	if partidos2015[i][0] not in votes:
		votes[partidos2015[i][0]] = [partidos2015[i][1]]
	else:
		votes[partidos2015[i][0]].append(partidos2015[i][1])
###########################--2016--################################
for i in range(len(partidos2016)):
	if partidos2016[i][0] not in votes:
		votes[partidos2016[i][0]] = [partidos2016[i][1]]
	else:
		votes[partidos2016[i][0]].append(partidos2016[i][1])
###########################--2017--################################
for i in range(len(partidos2017)):
	if partidos2017[i][0] not in votes:
		votes[partidos2017[i][0]] = [partidos2017[i][1]]
	else:
		votes[partidos2017[i][0]].append(partidos2017[i][1])
###########################--2018--################################
for i in range(len(partidos2018)):
	if partidos2018[i][0] not in votes:
		votes[partidos2018[i][0]] = [partidos2018[i][1]]
	else:
		votes[partidos2018[i][0]].append(partidos2018[i][1])

"""
print("\nAll data in the dictionary\n")
print(votes)
"""

#Tentativa de colocar os dados de votos de cada partido em um so grafico simples
plt.xlabel("x - anos de votação")
plt.ylabel("y - votos")
for i in votes:
	plt.plot(votes[i],label = i)
plt.legend()
plt.show()


print("\n:)")
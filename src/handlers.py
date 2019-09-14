# coding: utf-8
"""
Modulo responsavel por guardar funções responsaveis por manipular datasets
e transforma-los em novos, para facilitar a manipulação de dados com o uso da biblioteca "pandas" 
"""
import numpy as np
import pandas as pd

#Traduz um determinado DataFrame para um dicionario
def dataFrameToDic(dataFrame,dic):
	for i in range(len(dataFrame)):
		partido = dataFrame.partido[i]
		voto = dataFrame.voto[i]
		
		if partido not in dic:
			dic[partido] = (partido,{voto:[voto,1]})
		
		else:
			if voto not in dic[partido][1]:
				dic[partido][1][voto] = [voto,1]
			else:
				dic[partido][1][voto][1] += 1

#Separa a lista para criação de Data Frame especial a partir de dicionario
def separaEmLista(dictionary,listaVotos):
	
	for i in dictionary:
		auxDic = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0}
		
		for j in dictionary[i][1]:
			if j in auxDic:
				auxDic[j] = dictionary[i][1][j][1]
		contra = auxDic[-1]
		faltante = 	auxDic[0]
		aFavor = auxDic[1]
		obstrucao = auxDic[2]
		abstencao = auxDic[3]
		listaVotos.append([i,contra,faltante,aFavor,obstrucao,abstencao])

#filtra dados transformando de dicionario para matriz (lista de listas)
#para que seja criado o dataframe para facilitar a manipulação de dados com o uso da biblioteca pandas.
def filterData(ano):
	partidos = {}
	listaVotos = []
	
	path = "../data/pure_Data/votacoes_{ano}.csv".format(ano = ano)
	labels = ["partido","Votos-1","Votos0","Votos1","Votos2","Votos3"]
	data = pd.read_csv(path,",")

	dataFrameToDic(data, partidos)
	separaEmLista(partidos,listaVotos)
	dataFrame = pd.DataFrame(listaVotos,columns = labels)
	
	return dataFrame

#Gera menu para a escolha do partido
def getMenu(dataFrame,titles):
	lengthOfDataFrame = len(dataFrame)

	for i in range(lengthOfDataFrame):
		titles.append((dataFrame.partido[i],i))
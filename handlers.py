import numpy as np

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
def separaEmLista(dictionary):
	toReturn = []
	for i in dictionary:
		auxDic = {-1: None, 0: None, 1: None, 2: None, 3: None}
		
		for j in dictionary[i][1]:
			if j in auxDic:
				auxDic[j] = dictionary[i][1][j][1]
		
		toReturn.append([i,auxDic[-1],auxDic[0],auxDic[1],auxDic[2],auxDic[3]])

	return toReturn
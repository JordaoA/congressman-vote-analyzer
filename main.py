#coding: utf-8
import handlers
import pandas as pd
import matplotlib.pyplot as plt

#Dicionarios responsaveis por guardar e relacionar partidos e quantidade de votos no ano
partidos2015 = {}
partidos2016 = {}
partidos2017 = {}
partidos2018 = {}

#labesls para definicao de dados.
labels = ["partido","Votos-1","Votos0","Votos1","Votos2","Votos3"]

#Leitura de dados obtidos atraves dos csv's dos anos de 2015, 2016, 2017 e 2018
dataOf2015 = pd.read_csv("data/pure_Data/votacoes_2015.csv",",")
dataOf2016 = pd.read_csv("data/pure_Data/votacoes_2016.csv",",")
dataOf2017 = pd.read_csv("data/pure_Data/votacoes_2017.csv",",")
dataOf2018 = pd.read_csv("data/pure_Data/votacoes_2018.csv",",")

#Filtra alguns dados para um dicionario.
handlers.dataFrameToDic(dataOf2015,partidos2015)
handlers.dataFrameToDic(dataOf2016,partidos2016)
handlers.dataFrameToDic(dataOf2017,partidos2017)
handlers.dataFrameToDic(dataOf2018,partidos2018)

#Transforma dados em lista para a futura criação de um DataFrame.
listaVotos2015 = handlers.separaEmLista(partidos2015)
listaVotos2016 = handlers.separaEmLista(partidos2016)
listaVotos2017 = handlers.separaEmLista(partidos2017)
listaVotos2018 = handlers.separaEmLista(partidos2018)

#Cria Novo DataFrame a partir de dados extraidos do DataFrame original.
dataFrame2015 = pd.DataFrame(listaVotos2015,columns = labels)
dataFrame2016 = pd.DataFrame(listaVotos2016,columns = labels)
dataFrame2017 = pd.DataFrame(listaVotos2017,columns = labels)
dataFrame2018 = pd.DataFrame(listaVotos2018,columns = labels)

#Printa tabela referente a todos os anos. 
print('##DATAOF2015##\n')
print(dataFrame2015)
print('##DATAOF2016##\n')
print(dataFrame2016)
print('##DATAOF2017##\n')
print(dataFrame2017)
print('##DATAOF2018##\n')
print(dataFrame2018)

print("\n:)")
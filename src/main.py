#coding: utf-8
import handlers as hd
import matplotlib.pyplot as plt

#Dicionarios responsaveis por guardar e relacionar partidos e quantidade de votos no ano
partidos2015 = {}
partidos2016 = {}
partidos2017 = {}
partidos2018 = {}

#Cria Novo DataFrame a partir de dados extraidos do DataFrame original.
dataFrame2015 = hd.filtraDados("2015")
dataFrame2016 = hd.filtraDados("2016")
dataFrame2017 = hd.filtraDados("2017")#pd.DataFrame(listaVotos2017,columns = labels)
dataFrame2018 = hd.filtraDados("2018")

#Printa tabela referente a todos os anos. 
print('##DATAOF2015##\n')
print(dataFrame2015)
print('\n##DATAOF2016##\n')
print(dataFrame2016)
print('\n##DATAOF2017##\n')
print(dataFrame2017)
print('\n##DATAOF2018##\n')
print(dataFrame2018)

print("\n:)")
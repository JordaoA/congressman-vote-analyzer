#coding: utf-8
import handlers as hd
import numpy as np
import matplotlib.pyplot as plt

#Cria Novo DataFrame a partir de dados extraidos do DataFrame original.
dataFrame2015 = hd.filtraDados("2015")
dataFrame2016 = hd.filtraDados("2016")
dataFrame2017 = hd.filtraDados("2017")
dataFrame2018 = hd.filtraDados("2018")

#Gera menu de acordo com o ano escolhido
titles = []
while titles == []:
    ano = input("Ano de votação: ")
    
    if ano == 2015:
        titles = hd.preparaMenu(dataFrame2015)
    elif ano == 2016:
        titles = hd.preparaMenu(dataFrame2016)
    elif ano == 2017:
        titles = hd.preparaMenu(dataFrame2017)
    elif ano == 2018:
        titles = hd.preparaMenu(dataFrame2018)
    else:
        print("ano invalido")

#Printa menu gerado
print("Opções de partido...")
titles.sort()
for i in range(len(titles)):
    print("%d - %s" %(i+1,titles[i][0]))

#Gerencia a escolha do partido
partidoEscolhido = input("Escolha o partido: ")
index = titles[partidoEscolhido-1][1]
dataOp = None
if ano == 2015:
    dataOp = dataFrame2015.values[index]
elif ano == 2016:
    dataOp = dataFrame2016.values[index]
elif ano == 2017:
    dataOp = dataFrame2017.values[index]
else:
    dataOp = dataFrame2018.values[index]

#separa votos em lista
votes = []
for i in range(1,6):
    votes.append(dataOp[i])

#Gera grafico
plt.bar([0,1,2,3,4],votes)#scala)
plt.ylabel("Quantidade de votos")
plt.xticks(np.arange(len(dataOp)), ["Votos -1","Votos 0","Votos 1","Votos 2","Votos 3"])
plt.title("Votos de {ano} separados por Tipo".format(ano = ano))
plt.show()

print("\n:)")
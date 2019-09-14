#coding: utf-8
import handlers as hd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Cria Novo DataFrame a partir de dados extraidos do DataFrame original.
dataFrame2015 = hd.filterData("2015")
dataFrame2016 = hd.filterData("2016")
dataFrame2017 = hd.filterData("2017")
dataFrame2018 = hd.filterData("2018")

#Gera menu de acordo com o ano escolhido
titles = []
while titles == []:
    ano = input("Ano de votação: ")
    
    if ano == "2015":
        hd.getMenu(dataFrame2015,titles)
    elif ano == "2016":
        hd.getMenu(dataFrame2016,titles)
    elif ano == "2017":
        hd.getMenu(dataFrame2017,titles)
    elif ano == "2018":
        hd.getMenu(dataFrame2018,titles)
    else:
        print("ano invalido")

#Printa menu gerado
print("Opções de partido...")
titles.sort()
for i in range(len(titles)):
    print("%d - %s" %(i+1,titles[i][0]))

#Gerencia a escolha do partido
partidoEscolhido = int(input("Escolha o partido: "))
index = titles[partidoEscolhido-1][1]
partido = titles[partidoEscolhido-1][0]
dataOp = None

if ano == "2015":
    dataOp = dataFrame2015.values[index]
elif ano == "2016":
    dataOp = dataFrame2016.values[index]
elif ano == "2017":
    dataOp = dataFrame2017.values[index]
else:
    dataOp = dataFrame2018.values[index]

#separa votos em lista
votes = []
for i in range(1,6):
    votes.append(dataOp[i])

#Gera grafico
plt.bar([0,1,2,3,4],votes)
plt.ylabel("Quantidade de votos")
plt.xticks(np.arange(len(dataOp)), ["Contra"," N/Compareceu"," A favor"," Obstrução"," Abstencao"])
plt.title("Votos do partido {partido} em {ano}".format(partido =partido, ano = ano))
plt.show()

print("\n:)")

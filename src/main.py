#coding: utf-8
import handlers as hd
import numpy as np
import matplotlib.pyplot as plt

#Cria Novo DataFrame a partir de dados extraidos do DataFrame original.
dataFrame2015 = hd.filterData("2015")
dataFrame2016 = hd.filterData("2016")
dataFrame2017 = hd.filterData("2017")
dataFrame2018 = hd.filterData("2018")

#Gera menu de acordo com o ano escolhido
while True:
    titles = []
    while titles == []:
        ano = input("\n*** Escolha o ano de votação : ")

        if ano == "2015":
            hd.getMenu(dataFrame2015,titles)
        
        elif ano == "2016":
            hd.getMenu(dataFrame2016,titles)
        
        elif ano == "2017":
            hd.getMenu(dataFrame2017,titles)
        
        elif ano == "2018":
            hd.getMenu(dataFrame2018,titles)
        
        else:
            print("\n******************")
            print("***ANO INVALIDO***")
            print("******************\n")

    #Printa menu gerado
    print("****    Escolha pelo Numero   ****\n**** Opções de partido abaixo ****")
    titles.sort()
    for i in range(len(titles)):
        print("%d - %s" %(i+1,titles[i][0]))

    #Gerencia a escolha do partido
    partidoNaoValido = True  

    while partidoNaoValido:
        partidoEscolhido = int(input("**** Escolha o partido : "))
        if partidoEscolhido <= len(titles) and partidoEscolhido > 1:
            partidoNaoValido = False
        else:
            print("\n**** NUMERO DE PARTIDO INVALIDO ****\n")

    index = titles[partidoEscolhido-1][1] #indice usado para a escolha do partido e de seus votos dentro do data frame
        
    partido = titles[partidoEscolhido-1][0]
    dataOp = None

    if ano == "2015":
        dataOp = dataFrame2015.values[index]

    elif ano == "2016":
        dataOp = dataFrame2016.values[index]

    elif ano == "2017":
        dataOp = dataFrame2017.values[index]

    elif ano == "2018":
        dataOp = dataFrame2018.values[index]

    #separa votos em lista0
    votes = []
    for i in range(1,6):
        votes.append(dataOp[i])

    #Gera grafico de barras
    plt.bar([0,1,2,3,4],votes)
    plt.ylabel("Quantidade de votos")
    plt.xticks(np.arange(len(dataOp)), ["Contra"," N/Compareceu"," A favor"," Obstrução"," Abstencao"])
    plt.title("Votos do {partido} no ano de {ano}.".format(partido =partido, ano = ano))
    plt.show()
    
    #Checa se o usuario deseja continuar a gerar novos graficos
    afirmative = ["S","s","Sim","sim","Y","y","yes"]
    negative = ["N","n","Não","Nao","nao","não","No","no"]
    resp = input("**** Deseja continuar? ")
    if resp in negative:
        break    
    elif resp not in afirmative:
        print("\n*** Acho que isso significa um 'Sim' (??)") 

print("\nAté mais :)")
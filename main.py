import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

votes2015 = {}
votes2016 = {}
votes2017 = {}
votes2018 = {}

dataOf2015 = pd.read_csv("data/votacoes_2015.csv",",")
dataOf2016 = pd.read_csv("data/votacoes_2016.csv",",")
dataOf2017 = pd.read_csv("data/votacoes_2017.csv",",")
dataOf2018 = pd.read_csv("data/votacoes_2018.csv",",")

nvotes2015 = dataOf2015.groupby("partido").count()
nvotes2016 = dataOf2016.groupby("partido").count()
nvotes2017 = dataOf2017.groupby("partido").count()
nvotes2018 = dataOf2018.groupby("partido").count()

print("VOTOS 2015\n\n")
print(nvotes2015)
print("\nVOTOS 2016\n\n")
print(nvotes2016)
print("\nVOTOS 2017\n\n")
print(nvotes2017)
print("\nVOTOS 2018\n\n")
print(nvotes2018)


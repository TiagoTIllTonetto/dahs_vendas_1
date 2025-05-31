import json
import pandas as pd


#abrindo o arquivo json
file = open('dados/vendas.json')
#carregando o json
data = json.load(file)

#print(data)

#dataframe com pandas baseando em dicionario
df = pd.DataFrame.from_dict(data)


#print(df) 

#Convertendo a data de compra em dia mes ano
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')


file.close()
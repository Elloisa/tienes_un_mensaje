import pandas
df = pandas.read_csv('lista_correos.csv', delimiter = ';', index_col = "Nombre")

for i in range(len(df)):
    print(df.iloc[i]['email'])
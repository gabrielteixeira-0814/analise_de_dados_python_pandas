import pandas as pd

df = pd.read_csv("documents/lista_nomes2.csv", encoding='unicode_escape', sep=";")

# visualizar as 5 primeiras linhas
# print(df.head())

# Renomear coluna

df = df.rename(columns={"NOME": "name", "IDADE": "age"})

# print(df.head())

# Sabe o total de linhas e colunas
# print(df.shape)


# Tipo de cada coluna
# print(df.columns)
# print(df.dtypes)

# As ultimas linhas
# print(df.tail(2))

# Descricoes
# print(df.describe())

# Filtros na base de dados
#print(df["name"].unique())
name = df.loc[df["name"] == "Gabriel"]

# print(name.head())


# Agrupamento de dados

# print(df.groupby("name")["age"].nunique())

# media
# print(df.groupby("name")["age"].mean())
print(df["age"].mean())

# total
print(df["age"].sum())
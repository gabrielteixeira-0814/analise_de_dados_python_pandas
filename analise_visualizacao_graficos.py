import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_excel("documents/aracaju.xlsx")
df2 = pd.read_excel("documents/Fortaleza.xlsx")
df3 = pd.read_excel("documents/Natal.xlsx")

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3])

# Alterando tipo de dados da coluna
df["LojaId"] = df["LojaId"].astype("object")
df.dtypes

# Consultar valores nulos
df.isnull().sum()

# Substituindo os valores nulos pela média
#df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Substituindo os valores nulos por zero
#df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com os valores nulos
#df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
#f.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas colunas
#df.dropna(how="all", inplace=True)


############## Criando colunas novas #######################

# Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])  # vendas * quantidade

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Pegar maior receita
#df["Receita"].max()

# Pegar menor receita
#df["Receita"].min()


# Retornar as 3 maiores linhas com maiores receitas
# nlargest
#df.nlargest(3, "Receita")


# Retornar as 3 linhas com menores receitas
# nsmallest
#df.nsmallest(3, "Receita")

# Agrupamento por cidade

df.groupby("Cidade")["Receita"].sum()

# Ordernando do maior para o menor
df.sort_values("Receita", ascending=False).head(10)


################### Trabalhando com datas ######################

# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Transformando a coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando a coluna ano
df["Ano_Venda"] = df["Data"].dt.year

# Criando a coluna dia e mês
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Retorna a data mais antiga
df["Data"].min()

# Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

# Fitrando as vendas de 2019 que foram realizadas em janeiro
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 1)] # loc ele localizar fazendo filtr de busca



############ Visualização de dados #######################

# conta o total de lojas por ID
#df["LojaId"].value_counts(ascending=False)

# Gráfico de barras
#df["LojaId"].value_counts(ascending=False).plot.bar()

# Gráfico de barras horizontais
#df["LojaId"].value_counts(ascending=False).plot.barh()

# Gráfico de pizza
#df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# Total de vendas por cidade
# print(df["Cidade"].value_counts())


# Adicinando um título e alterando o nome dos eixos
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/vendas.csv")
df['Data'] = pd.to_datetime(df['Data'])
df['AnoMes'] = df['Data'].dt.to_period('M')

mais_vendidos = df['Produto'].value_counts().head(5)

sns.barplot(x=mais_vendidos.index, y=mais_vendidos.values)
plt.title("Top 5 Produtos Mais Vendidos")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.savefig("imgs/produtos_mais_vendidos.png")
plt.show()

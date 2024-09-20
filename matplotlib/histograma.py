import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Gerando um conjunto de dados de idades aleatórias para o exemplo
np.random.seed(42)  # Para reprodutibilidade
idade = np.random.randint(18, 70, size=100)

df = pd.DataFrame({'idade': idade})
print(df.head())
plt.figure(figsize=(10, 6))
##bins divide os dados em 100 intervalos
sns.histplot(df['idade'], bins=100, kde=False, color='skyblue', edgecolor='black')

# Adicionando a curva de densidade usando kdeplot
sns.kdeplot(df['idade'], color='red', linewidth=2)
plt.xlabel('Idade')
plt.ylabel('Frequência / Densidade')
plt.grid(True)
plt.show()


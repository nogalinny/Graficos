import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = ("ecommerce_estatistica.xlsx")  # Altere o caminho conforme necessário
df = pd.read_excel(file_path)

# Criar a figura com dois histogramas
plt.figure(figsize=(14, 5))

# Histograma das Notas dos produtos
plt.subplot(1, 2, 1)
sns.histplot(df['Nota'], bins=10, kde=True, color='blue')
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Produtos')

# Histograma do Número de Avaliações
plt.subplot(1, 2, 2)
sns.histplot(df['N_Avaliações'], bins=20, kde=True, color='green')
plt.title('Distribuição do Número de Avaliações')
plt.xlabel('Número de Avaliações')
plt.ylabel('Produtos')

# Exibir os gráficos
plt.tight_layout()
plt.show()

#Gráfico de dispersão
plt.hexbin(df['N_Avaliações'], df['Nota'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('N_Avaliações')
plt.ylabel('Nota')
plt.title('Produtos avaliados e suas notas')
plt.show()

df_corr = df[['Desconto', 'N_Avaliações', 'Preço', 'Qtd_Vendidos_Cod']].corr()

# Define o tamanho da figura do gráfico
plt.figure(figsize=(10, 8))  

# Cria um mapa de calor (heatmap) da correlação entre as variáveis
sns.heatmap(df_corr, annot=True, fmt=".2f")  
plt.title('Mapa de Calor - Correlação entre Variáveis')  
plt.show() 

#Gráfico de barras
plt.figure(figsize=(10, 6))
df['Temporada_Cod'].value_counts().plot(kind='bar', color= '#90ee70')
plt.title('Quantidade vendida na temporada')
plt.xlabel('Temporada')
plt.ylabel('Qtd_Vendidos_Cod')
plt.xticks(rotation=0)
plt.show()

# Gráfico de densidade de salários
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
sns.kdeplot(df['Preço_MinMax'], fill=True, color='#863e9c')  # Cria um gráfico de densidade (KDE) preenchido
plt.title('Densidade de preços')  # Adiciona um título ao gráfico
plt.xlabel('Preços')  # Define o rótulo do eixo X
plt.show()  # Exibe o gráfico

sns.regplot(
    x='Qtd_Vendidos_Cod', y='Desconto', data=df, color='#278f65',  # Define as variáveis e a cor da linha de regressão
    scatter_kws={'alpha': 0.5, 'color': '#34c289'}  # Configura os pontos de dispersão (transparência e cor)
)
plt.title('Regressão de quantidade vendida pelo desconto')  # Adiciona um título ao gráfico
plt.xlabel('Qtd_Vendidos_Cod')  # Define o rótulo do eixo X
plt.ylabel('Desconto')  # Define o rótulo do eixo Y
plt.show()  # Exibe o gráfico

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

genero_counts = df.groupby('Gênero')['Qtd_Vendidos_Cod'].sum()

# Definir cores específicas para cada categoria de gênero
cores = {
    'Bebês': '#ff9999',         # Rosa claro
    'Feminino': '#ff66b2',      # Rosa forte
    'Masculino': '#66b3ff',     # Azul
    'Meninas': '#ffcc99',       # Laranja claro
    'Meninos': '#3399ff',       # Azul forte
    'Sem gênero': '#c2c2c2',    # Cinza
    'Sem gênero infantil': '#8c8c8c',  # Cinza escuro
    'Unissex': '#99ff99',        # Verde claro
    'roupa para gordinha pluss P ao 52': '#9966cc' # Roxo
}

# Aplicar as cores conforme os gêneros encontrados no dataset
cores_usadas = [cores[categoria] for categoria in genero_counts.index]

# Criar o gráfico de pizza
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    genero_counts, labels=None, autopct='%.1f%%', startangle=90, colors=cores_usadas
)

# Adicionar a legenda ao lado
plt.legend(wedges, genero_counts.index, title="Gênero", loc="center left", bbox_to_anchor=(1, 0.5))

plt.title('Quantidade de Produtos Vendidos por Gênero')
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
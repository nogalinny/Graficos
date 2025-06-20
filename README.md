Gráficos com Python para Análise de E-commerce

Este projeto explora um conjunto de dados de e-commerce, utilizando as bibliotecas Pandas, Matplotlib e Seaborn para gerar gráficos e identificar insights. A análise foca em aspectos como quantidade vendida, número de avaliações, notas de avaliações, descontos, preços, temporadas de compra e gêneros de produtos.

Como Executar o Código
Para executar o código e reproduzir os gráficos, siga os passos abaixo:

Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema. Você também precisará das seguintes bibliotecas:

Pandas: Para manipulação e análise de dados.
Matplotlib: Para a criação de gráficos estáticos, interativos e animados.
Seaborn: Para visualização de dados estatísticos de alta qualidade, construído sobre o Matplotlib.
Você pode instalá-las usando pip:

Bash
pip install pandas matplotlib seaborn openpyxl
Observação: O openpyxl é necessário para ler arquivos .xlsx com o Pandas.

Estrutura do Projeto
Arquivo de Dados: Salve seu conjunto de dados (ecommerce_estatistica.xlsx) na mesma pasta do script Python.
Script Python: Salve o código fornecido em um arquivo .py (por exemplo, analise_ecommerce.py).
Execução
Abra um terminal ou prompt de comando.

Navegue até o diretório onde você salvou o script e o arquivo de dados.

Execute o script Python:

Bash
python analise_ecommerce.py
Ao executar o script, os gráficos serão exibidos sequencialmente em janelas separadas.

Análise e Decisões Tomadas com Base nos Gráficos
1. Histogramas
a) Distribuição das Notas dos Produtos
Análise: A maioria dos produtos possui notas entre 4.0 e 4.8, com um pico próximo de 4.5. Poucos produtos estão abaixo de 3.5. A curva KDE (linha azul) indica uma distribuição levemente assimétrica para a esquerda, sugerindo que a maioria das avaliações é positiva.
Decisão:
Destaque em Marketing: Focar em campanhas de marketing para produtos bem avaliados (notas acima de 4.0) para impulsionar as vendas, aproveitando a percepção positiva.
Análise de Produtos de Baixa Nota: Para produtos com notas abaixo de 3.5, investigar as causas das avaliações negativas (qualidade, entrega, atendimento, etc.) e buscar melhorias contínuas.
b) Distribuição do Número de Avaliações
Análise: Poucos produtos recebem muitas avaliações, enquanto a maioria tem poucas. Isso aponta para uma concentração da visibilidade das avaliações em alguns produtos populares.
Decisão:
Alavancar Produtos Populares: Utilizar os produtos com maior número de avaliações para impulsionar vendas, talvez promovendo-os em destaque.
Incentivar Novas Avaliações: Implementar estratégias para incentivar mais avaliações:
Envio de e-mails pós-compra solicitando feedback.
Oferta de descontos ou outros benefícios para clientes que avaliarem produtos.
Destaque para produtos mais bem avaliados na plataforma.

2. Gráfico de Dispersão - Relação entre Notas e Número de Avaliações
Análise: O padrão é similar ao segundo histograma: alguns produtos são altamente populares e recebem muitas avaliações, enquanto a maioria tem poucas. Isso reforça a ideia de que a visibilidade e o engajamento estão concentrados.

Decisão: Reforça as decisões tomadas para o histograma de número de avaliações, focando na maximização do engajamento em avaliações.

3. Mapa de Calor - Correlação entre Desconto, Avaliações, Preço e Quantidade Vendida
Análise:
A maior correlação (0.91) é entre o número de avaliações e a quantidade vendida, indicando que produtos mais vendidos tendem a ter mais avaliações.
A menor correlação (0.15) é entre desconto e quantidade vendida, sugerindo que a redução de preço, por si só, pode não ser um motor significativo de aumento de vendas.
Decisão:
Priorizar Avaliações: Concentrar esforços em estratégias que incentivem avaliações, pois produtos mais avaliados demonstram maior potencial de vendas.
Diversificar Estratégias de Venda: Testar outras abordagens além de descontos para impulsionar vendas, como ações de marketing mais focadas, programas de fidelidade ou benefícios adicionais (ex: frete grátis, brindes).

4. Gráfico de Barras - Quantidade Vendida nas Temporadas
Análise: A maior quantidade de vendas ocorreu na Primavera/Verão. No entanto, a presença de muitos valores "não definidos" para temporadas dificulta uma análise precisa e impede a identificação de padrões sazonais claros.
Decisão:
Melhorar a Categorização: É crucial melhorar a categorização das temporadas nos dados para permitir uma análise mais precisa dos padrões de compra sazonais e otimizar o planejamento de estoque e promoções.

5. Gráfico de Pizza - Distribuição de Produtos Vendidos por Gênero
Análise: A maior concentração de vendas está nos gêneros masculino e feminino. Há também uma parcela significativa de produtos sem definição de gênero, o que dificulta entender o público-alvo desses itens.
Decisão:
Refinar Filtros de Compra: Criar filtros mais específicos na hora da compra para que os clientes possam encontrar produtos por gênero com mais facilidade, fornecendo dados mais precisos para análises futuras.
Investir em Públicos Menos Atendidos: Avaliar o investimento em produtos para os públicos menos atendidos (ex: Bebês, Meninas, Meninos, Plus Size) para expandir o mercado e atender a nichos específicos.

6. Gráfico de Densidade - Distribuição de Preços
Análise: O gráfico exibe pelo menos dois picos, sugerindo uma distribuição bimodal ou multimodal de preços, o que pode indicar diferentes faixas de preço predominantes (ex: produtos de entrada, intermediários, premium). Além disso, a curva assimétrica com uma cauda longa à direita indica a existência de produtos com preços significativamente mais altos que a maioria.
Decisão:
Análise de Precificação por Categoria: Se houver grande variação de preços dentro de uma mesma categoria, é importante analisar se é necessário um ajuste de precificação para otimizar vendas e lucratividade.
Diferenciação de Produtos Caros: Verificar se os produtos de preço mais elevado possuem diferenciais claros que justifiquem seu custo para o cliente, como qualidade superior, marca ou exclusividade.

7. Gráfico de Regressão - Quantidade Vendida vs. Desconto
Análise: A linha de regressão indica uma relação fraca entre desconto e quantidade vendida. Muitos produtos com baixa quantidade vendida apresentam descontos variados, sugerindo que o desconto não é o único ou principal fator impulsionador de vendas. Há outliers onde grandes quantidades foram vendidas com descontos variados, o que pode indicar outros fatores em jogo.
Decisão:
Testar Outras Estratégias: Experimentar diferentes abordagens para impulsionar vendas, além dos descontos, como campanhas de marketing, ofertas de frete grátis ou brindes.
Analisar Outliers: Investigar os outliers (casos de alta venda com descontos variados) para identificar padrões ou fatores específicos que contribuíram para o sucesso nessas situações.


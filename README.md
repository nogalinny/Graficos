Graficos com python

Os gráficos foram gerados utilizando as bibliotecas Pandas, Matplotlib e Seaborn.
O conjunto de dados analisado é de um e-commerce, explorando os seguintes aspectos: quantidade vendida, número de avaliações, notas das avaliações, descontos, preços, temporadas de compra e gêneros de produtos.

Tipos de Gráficos
1. Histogramas
a) Distribuição das Notas dos Produtos (Esquerda)
A maioria dos produtos tem notas entre 4.0 e 4.8, com um pico próximo de 4.5. Poucos produtos possuem notas abaixo de 3.5.
A curva KDE (linha azul) sugere que a distribuição das notas é levemente assimétrica para a esquerda, indicando que a maioria das avaliações é positiva.

Decisão:

Destacar os produtos bem avaliados (notas acima de 4.0) em campanhas de marketing para impulsionar as vendas.

Para produtos com notas abaixo de 3.5, analisar as razões das avaliações negativas (qualidade, entrega, atendimento, etc.) e buscar melhorias.

b) Distribuição do Número de Avaliações (Direita)
Poucos produtos possuem muitas avaliações, enquanto a maioria tem poucas. Isso indica que a visibilidade das avaliações está concentrada em alguns produtos populares.

Decisão:

Aproveitar os produtos populares para impulsionar vendas.

Incentivar mais avaliações com estratégias como:

E-mails pós-compra pedindo feedback.

Ofertas ou descontos para clientes que avaliarem produtos.

Destaque para produtos mais bem avaliados.

2. Gráfico de Dispersão - Relação entre Notas e Número de Avaliações
O comportamento é semelhante ao segundo histograma: alguns produtos são populares e recebem muitas avaliações, enquanto a maioria tem poucas.

3. Mapa de Calor - Correlação entre Desconto, Avaliações, Preço e Quantidade Vendida
A maior correlação (0.91) foi entre número de avaliações e quantidade vendida. Isso mostra que produtos mais vendidos tendem a ter mais avaliações.

A menor correlação (0.15) foi entre desconto e quantidade vendida, indicando que reduzir o preço não é suficiente para aumentar as vendas.

Decisão:

Focar em estratégias que incentivem avaliações, pois produtos mais avaliados vendem mais.

Testar outras ações além de descontos para impulsionar vendas, como marketing e benefícios adicionais.

4. Gráfico de Barras - Quantidade Vendida nas Temporadas
As temporadas são codificadas como:
{7=primavera/verão, 3=outono/inverno, 1=não definido, 0=2021, 6=múltiplas estações, 5=múltiplas estações, 9=ano todo}.

A maior quantidade de vendas ocorreu na primavera/verão, mas há muitos valores indefinidos, dificultando uma análise mais precisa.

Decisão:

Melhorar a categorização das temporadas para entender melhor os padrões de compra.

5. Gráfico de Pizza - Distribuição de Produtos Vendidos por Gênero
Os gêneros identificados nos dados são: Feminino, Masculino, Meninas, Meninos, Unissex, Sem Gênero, Sem Gênero Infantil e Plus Size.

A maior concentração está no gênero masculino, seguido pelo feminino. Além disso, há muitos produtos sem definição de gênero.

Decisão:

Criar filtros mais específicos na hora da compra para entender melhor o público-alvo.

Investir em produtos para os públicos menos atendidos.

6. Gráfico de Densidade - Distribuição de Preços
O gráfico mostra pelo menos dois picos, sugerindo que os preços seguem uma distribuição bimodal ou multimodal. Isso pode indicar diferentes faixas de preço predominantes.

Além disso, a curva é assimétrica, com uma cauda longa à direita, sugerindo que existem produtos com preços muito altos em relação à maioria.

Decisão:

Se houver grande variação de preços dentro de uma mesma categoria, analisar se é necessário um ajuste de precificação.

Verificar se os produtos mais caros precisam de diferenciação para justificar o preço.

7. Gráfico de Regressão - Quantidade Vendida vs. Desconto
A linha de regressão mostra uma relação fraca entre desconto e quantidade vendida. Muitos produtos com baixa quantidade vendida têm descontos variados, sugerindo que o desconto não é o único fator impulsionador de vendas.

Além disso, há outliers onde grandes quantidades foram vendidas com descontos variados, indicando possíveis exceções.

Decisão:

Testar diferentes abordagens além de descontos para impulsionar vendas (ex.: marketing, frete grátis, brindes).

Analisar os outliers para entender se há padrões nesses casos.



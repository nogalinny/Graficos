# Graficos
Gráficos elaborados apartir das bibliotecas: Pandas, Matplotlib e Seaborn.
O arquivo é de ecommerce e os principais pontos explorados foram as quantidades vendidas, quantidades de avaliações, as notas das avaliações, os descontos, preço, temporadas de compras e gênero.

Tipos de gráficos

01. Histograma:
Gráfico da Distribuição das Notas dos Produtos (Esquerda)
O que observa-se?
A maioria dos produtos tem notas entre 4.0 e 4.8, com um pico próximo de 4.5.
Poucos produtos possuem notas abaixo de 3.5.
A curva KDE (linha azul) sugere que as avaliações seguem uma distribuição levemente assimétrica para a esquerda (notas tendendo a ser mais altas).

Interpretação e Decisão:
A maioria dos clientes está satisfeita, já que a maioria das notas está acima de 4.0.
Pode-se destacar esses produtos bem avaliados em campanhas de marketing para impulsionar vendas.
Caso existam produtos com notas abaixo de 3.5, é essencial entender os motivos das avaliações negativas (problemas com qualidade, entrega, etc.) e corrigi-los.

Gráfico da Distribuição do Número de Avaliações (Direita)
O que observamos?
A maioria dos produtos tem poucas avaliações, com um grande número tendo menos de 500 avaliações.
Apenas alguns produtos têm um número muito alto de avaliações (exemplo: mais de 6.000).
A distribuição é assimétrica para a direita, indicando que há poucos produtos que concentram muitas avaliações, enquanto a maioria tem poucas.

Interpretação e Decisão:
Alguns produtos são muito populares e recebem muitas avaliações (esses podem ser aproveitados para impulsionar vendas).
Muitos produtos quase não têm avaliações, o que pode reduzir a confiança do consumidor.
Ação recomendada: Implementar estratégias para incentivar mais avaliações, como:

E-mails pós-compra pedindo feedback.
Ofertas ou descontos para quem avaliar o produto.
Destaque para os produtos mais bem avaliados para atrair novos compradores.

Conclusão
Combinação das duas análises:
Notas altas + poucas avaliações: Produtos bons, mas precisam de mais visibilidade e incentivo para mais avaliações.
Notas baixas + poucas avaliações: Produtos que podem ser problemáticos e precisam de melhorias.
Muitas avaliações + notas altas: Produtos confiáveis e populares, que devem ser promovidos.
Muitas avaliações + notas medianas: Pode indicar que os produtos são populares, mas têm pontos a melhorar.

02. Gráfico de dispersão:

Assim como o segundo histograma, analisamos que há poucas avaliações para muitos produtos, já alguns produtos são mais populares.

03. Mapa de calor:

Cria um mapa de calor (heatmap) da correlação entre as variáveis: Desconto, número de avaliações, preço e quantidade vendidas.

04.Gráfico de barras:

Análisa a quantidade vendida nas temporadas. {7=primavera/verão, 3=outono/inverno, 1=não definido, 0=2021, 6=primavera-verão outono-inverno, 5=primavera-verão - outono-inverno, 9=primavera/verão/outono/inverno}

05. Gráfico de pizzas:

Analisa a distribuição de produtos vendidos para cada gênero.

06. Gráfico de densidade:

Gráfico de densidade de salários, analisando desde o preço mínimo até o máximo.

07. Gráfico de regressão:

Regressão de quantidade vendida pelo desconto. Analisa se há correlação da quantidade vendida com o desconto proporcionado ao cliente.



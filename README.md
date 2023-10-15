
<h1 align="center">Análise de Dados e Visualização para Tomada de Decisões em Publicidade</h1>

<h3 align="center">Teste Técnico - Analista de Dados Jr - RBS</h3>

<h3 align="center">Bruno Di Franco Albuquerque</h3>

<p align="center">
  <img src="pic/logo.png" width="200"/>
</p>

## Descrição do Teste:
Neste teste, os candidatos deverão realizar uma análise de dados simples relacionada a campanhas publicitárias e criar visualizações claras para ajudar na tomada de decisões de negócios. Eles terão acesso a um conjunto de dados fictício que contém informações sobre campanhas publicitárias e desempenho das mesmas.

## Informações Gerais:
- A explicação completa dos passos realizados e códigos para os pontos 1 e 2 estão disponíveis [nesse](https://github.com/brunodifranco/bruno-case-tecnico-rbs/blob/main/12-10-2023-bruno-case-tecnico.ipynb) Jupyter Notebook. O ponto 3, que conta com as visualizações é um [app do Streamlit](https://bruno-di-franco-rbs-dataviz-app.streamlit.app/). O ponto 4, é um relatório de recomendações [nesse](https://docs.google.com/document/d/1Q0-pwATZkMRp77GxQRD8DQ49AUdYC0zYzgYKmtFT-sE/edit?usp=sharing) Google Docs.

- Ferramentas utilizadas: **Python, VSCode, Streamlit, Google Docs, GitHub**.

# 1. **Exploração de Dados**

**A base de dados possui 7000 linhas e 9 colunas, e suas variáveis podem ser classificadas em 3 grupos:**

Primeiro grupo:

- Esse primeiro grupo representa as variáveis categóricas presentes na base de dados.

| **Nome da Variável** | **Significado** | **Tipo da Variável** |
|----------------------|-----------------|----------------------|
|  advertiserName        |   Nome do Cliente              |    objeto, string                  |
| creativeType                     | Tipo do Criativo                | objeto, string          |
|   deviceCategoryName       |  Categoria do dispositivo                  |  objeto, string    |

Segundo grupo:

- No segundo grupo temos apenas uma variável, que é a data, sendo, portanto, uma variável temporal, que pode ser muito útil para visualizações de séries temporais.

| **Nome da Variável** | **Significado** | **Tipo da Variável** |
|----------------------|-----------------|----------------------|
|  date        |   Data de exibição do anúncio              |    datetime, variável temporal                |

Terceiro grupo:

- Esse último grupo representa as variáveis numéricas, podendo ser encaradas como KPI's para publicidade, como indicadores de conversão, taxa de cliques, etc. **Portanto, se tivermos que elencar as "principais variáveis presentes" seriam exatamente as desse terceiro grupo.**

| **Nome da Variável** | **Significado** | **Tipo da Variável** |
|----------------------|-----------------|----------------------|
|  totalLineItemLevelImpressions         |    Impressões totais             |    numérica, integer              |
| totalLineItemLevelClicks               | Cliques totais             | numérica, integer        |
|   totalLineItemLevelCTR                |  Taxa de Cliques (click through rate), ou seja,   Cliques totais  /  Impressões totais  |  numérica, float    |
| clickThroughConversions                | Conversões diretas (oriundas de clique)        | numérica, integer        |
|   viewThroughConversions               |  Conversões indiretas (não relacionadas ao último clique)    |  numérica, integer   |

# 2. **Análise Descritiva**

## 2.1. Qual é a média de conversões por tipo de criativo?

Eu agrupei as conversões por dia e tipo de criativo, ou seja, somamos os valores de conversão em cada dia para cada tipo de criativo. Depois, tiramos a média diária de conversões:
<div align="center">

| Tipo do Criativo            | Média Diária de Conversões Diretas | Média Diária de Conversões Indiretas | Média Diária de Conversões Totais   |
|-------------------------|-------------------------|-------------------------|--------------------|
| Custom                  | 1.026,08                 | 2.124,27                 | 3.150,34            |
| Custom template         | 1.242,66                 | 2.349,38                 | 3.592,03            |
| DoubleClick Rich Media | 1.047,73                 | 2.208,34                 | 3.256,08            |
| HTML5                   | 1.140,93                 | 2.152,14                 | 3.293,08            |
| Image                   | 1.095,64                 | 2.283,29                 | 3.378,93            |
| Other                   | 1.031,88                 | 2.031,92                 | 3.063,80            |
| Programmatic            | 1.093,12                 | 2.224,81                 | 3.317,93            |
| Third-party             | 1.091,42                 | 2.182,46                 | 3.273,88            |
| Video creative sets     | 1.005,64                 | 2.010,03                 | 3.015,68            |

</div>

## 2.2. Quais são os tipos de criativos mais eficazes em termos de conversões?

<p align="justify"> Uma forma de avaliar a eficácia de cada criativo é calcularmos a taxa de conversão de cada criativo. A taxa de conversão, para nosso caso, pode ser calculada da seguinte forma: </p>

Taxa de Conversão = $\frac{Total\ de\ conversões}{Total\ de\ impressões}$

*Outra forma de avaliar a eficácia também seria usando a variável de "Click through rate", porém como estamos interessados na eficácia em termos de **conversão** será utilizada somente a taxa de conversão:*

<div align="center">

| Tipo de Criativo           | Total de Impressões no Período | Total de Conversões no Período | Taxa de Conversão  |
|-------------------------|-----------------------------|-----------------------------|----------|
| Custom template         | 20.463.676                  | 323.283                     | 1.5798%  |
| Custom                  | 18.189.377                  | 283.531                     | 1.5588%  |
| Video creative sets     | 17.999.009                  | 271.411                     | 1.5079%  |
| Programmatic            | 19.891.450                  | 298.614                     | 1.5012%  |
| Third-party             | 19.809.748                  | 294.649                     | 1.4874%  |
| DoubleClick Rich Media  | 19.913.654                  | 293.047                     | 1.4716%  |
| Image                   | 20.714.685                  | 304.104                     | 1.4681%  |
| HTML5                   | 20.294.235                  | 296.377                     | 1.4604%  |
| Other                   | 19.115.632                  | 275.742                     | 1.4425%  |

</div>

**Portanto, os dois tipos de criativos mais eficazes em termos de conversão são "Custom template" e "Custom"**.

## 2.3. Existe uma tendência sazonal nas conversões?

*Dois pontos são importantes de esclarecer antes de darmos essa resposta:* 

- *A sazonalidade se caracteriza por padrões regulares e repetitivos em um período específico.*

- *Para ter uma compreensão perfeita do processo feito é preciso realmente olhar o passos no notebook.*

<p align="justify"> Primeiramente, avaliei visualmente as conversões diretas e indiretas em uma série temporal e claramente não há constância no número de conversões, porém essa variação não parece ter um padrão bem definido em relação aos dias da semana. Por exemplo, poderia haver uma sazonalidade com mais conversões em finais de semana, porém isso não acontece. Em outras palavras, não há um padrão claro de determinado período da semana nos picos das séries, nem nos vales (pontos mais baixos), <strong>portanto, não há sazonalidade em relação aos dias da semana.</strong></p>

<p align="justify"> Se extrapolarmos a análise para uma <strong> sazonalidade mensal, é possível observar que nas três séries os finais de cada mês, portanto dias 30 e 31 (quando tiver), estão em pontos de vale.</strong> Porém, é importante observar que contamos com apenas 3 meses de série, ou seja, são poucos dados para que possamos definir propriamente esse comportamento como sazonalidade.</p>

<p align="justify"> Depois, busquei avaliar a sazonalidade com métodos quantitativos como:

- Estatística Descritiva
  
- <strong>teste de Dickey-Fuller Aumentado (ADF)</strong>, que na realidade é um teste de estacionariedade, porém quando a série é estacionária pode ser um indício da falta de sazonalidade. 
  
- Além desse teste, prossegui com um teste de <strong>Análise Espectral, utilizando Transformada de Fourier</strong>, que é propriamente um teste de sazonalidade. O teste foi feito buscando sazonalidade em 1, 7, 15 e 30 dias.</p>

<p align="justify"> As duas séries (conversões diretas e conversões indiretas) apresentaram estacionariedade, ou seja, é um indício a favor da não sazonalidade. Em relação a análise espectral com transformada de Fourier, esta é eficaz na detecção de padrões sazonais que têm frequências específicas, mas quando não há componentes de frequência distintos, o espectro de frequência tende a ser plano ou ter um pico central. <strong>Nesses casos, há fortes evidências de não sazonalidade na série, e é exatamente o que acontece no nosso caso, ou seja, há um pico central nessas duas séries, caracterizando a ausência de sazonalidade. </strong> </p>

<p align="justify"> Toda essa primeira análise foi feita com base nas conversões diretas e indiretas, sem distinção por tipo de criativo. Então parti para uma segunda análise, para ver se era possível encontrar sazonalidade nas conversões filtradas por tipo de criativo. Repeti os mesmos testes, de inspeção visual, teste de Dickey-Fuller Aumentado (ADF) e Análise Espectral, utilizando Transformada de Fourier e novamente não houveram indícios de sazonalidade nos dados. </p>

<p align="justify"> <strong> Portanto, de acordo com os extensos testes realizados, não há evidências de sazonalidade nos dados em termos de conversão, tanto avaliando os dados no nível macro (agrupando todos os tipos de criativos na mesma análise) quanto separando e avaliando individualmente por cada tipo de criativo. É importante definir que a sazonalidade se caracteriza por padrões regulares e repetitivos em um período específico, e isso não foi encontrado, inclusive com testes para 1, 7, 15 e 30 dias. </strong> </p>


## 2.4. Há algum outlier nos dados que mereça atenção?

A detecção de outliers pode ser uma tarefa complicada, já que não há uma maneira 100% definida para fazer essa identificação. É comum a utilização de alguns métodos como:

- Box plots
- Avaliação por desvio padrão (Z-Score) ou por Intervalo Interquartil, dependendo da distribuição de probabilidade.
- Métodos de Machine Learning mais avançados, como Redes Neurais com arquitetura de AutoEncoders por exemplo, ou outras formas de redução de dimensionalidade, como o UMAP. Ou ainda, algoritmos próprios para detectar outliers, como o Isolation Forest.

Para essa análise, me restringi aos dois primeiros métodos. Nessa tarefa também vale muito a pena olhar no Jupyter Notebook o passo a passo. 

<p align="justify"> Em relação às variáveis Conversões Indiretas, Cliques Totais e Impressões Totais a ausência de outliers fica muito clara, pois já no Box Plot não identificamos nenhum ponto que poderia se enquadrar como outlier. </p>

<p align="justify"> A variável de Conversões Diretas tem alguns valores um pouco acima no Box Plot, mas avaliando mais minuciosamente os valores seria muito exagero considerará-los como "outliers", ainda mais considerando as estatísticas descritivas para tal variável. Portanto, podemos concluir que não há outliers para as Conversões Diretas. </p>

Sobraria então avaliar a variável Click Through Rate, que tem uma peculiaridade, por ser calculada com base em outras duas variáveis, da seguinte forma:

Click through rate = $\frac{Cliques\ totais}{Total\ de\ impressões}$

<p align="justify"> Ou seja, a princípio esse número deve variar entre 0 e 1, pois para um mesmo tipo de criativo e dispositivo utilizado em determinada data não podemos ter mais cliques do que impressões. Entretanto, encontramos 35 observações com valores maiores que 1 nessa variável.<strong> Assim sendo, esses 35 valores no Click Through Rate podem ser considerados outliers, seja por algum erro nos dados, ou na própria contabilização das métricas.</strong> </p>


# 3. **Visualização de Dados**

No app do Streamlit é possível visualizar:

- Séries temporais de conversões diretas, indiretas e totais, com a possibilidade de filtrar por tipo de criativo, além selecionar o período desejado para a análise.
- Gráfico de barras com o somatório de uma dentre cinco escolhas de métricas para o período em questão.
- Mapas de calor de duas taxas (que podem ser escolhidas manualmente): ConversionRate e ClickThroughRate. Esses mapas de calor relacionam a mediana dessas taxas com outras duas variáveis: o dia da semana do anúncio e o tipo de criativo.
  
<div align="center">

|         **Clique abaixo para acessar o App**        |
|:------------------------:|
|         [![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://bruno-di-franco-rbs-dataviz-app.streamlit.app/)
</div>


*Obs: O repositório com o código do App está [aqui](https://github.com/brunodifranco/streamlit-app-rbs-analista-dados).*

# 4. **Recomendações**

<div align="center">

|         **Clique abaixo para acessar o Relatório de Recomendações**        |
|:------------------------:|
|        [![Docs](https://www.google.com/images/about/docs-icon.svg)](https://docs.google.com/document/d/1Q0-pwATZkMRp77GxQRD8DQ49AUdYC0zYzgYKmtFT-sE/edit?usp=sharing)
</div>

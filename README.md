# Análise de Anúncios de Veículos

## Sobre o projeto

Este projeto tem uma aplicação interativa desenvolvida com Streamlit para explorar os anúncios dos veículos. 

O objetivo é facilitar a visualização dos padrões e das relações entre as características dos veículos, de acordo com a quilometragem e os preços anunciados.

## Funcionalidades

- Visualização da distribuição da quilometragem dos veículos por meio de histograma.
- Análise da relação entre quilometragem e preço por meio de gráfico de dispersão.
- Exploração dos dados utilizando Pandas e Plotly Express.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit
- Jupyter Notebook

## Estrutura do projeto

- `app.py`: código da aplicação web.
- `vehicles_us_clean.csv`: base de dados utilizada pela aplicação.
- `vehicles_us.csv`: base de dados original.
- `notebooks/EDA.ipynb`: notebook de análise exploratória dos dados.
- `requirements.txt`: dependências do projeto.

## Como executar localmente

1. Instale as dependências:

   `pip install -r requirements.txt`

2. Execute a aplicação:

   `streamlit run app.py`

3. Acesse no navegador:

   `http://localhost:8501`

## Análise exploratória

O notebook `EDA.ipynb` apresenta a exploração inicial dos dados e as visualizações desenvolvidas com Plotly Express.
# ETL-OPENWHEATER

🌦️ Clima Brasil — Projeto de Engenharia de Dados

Status

✅ Concluído — Pipeline funcional, orquestrado e integrado a ferramenta de BI

📌 Sobre o Projeto

O Clima Brasil é um projeto de Engenharia de Dados desenvolvido para simular um pipeline real de ingestão, validação, transformação e disponibilização de dados climáticos do Brasil.

O projeto consome dados da OpenWeather API, realiza validações com Pydantic, transforma os dados com Pandas, armazena em um Data Warehouse PostgreSQL e disponibiliza os dados para análise no Power BI.
Toda a pipeline é orquestrada com Apache Airflow, rodando em ambiente Dockerizado.

O foco do projeto é demonstrar boas práticas de ETL, orquestração, modelagem dimensional e integração com BI, simulando um cenário real de mercado.

🎯 Objetivo do Projeto

O principal objetivo do projeto é:

- Construir um pipeline ETL completo e orquestrado

- Consumir dados reais de uma API externa (OpenWeather)

- Aplicar validação de dados com regras de negócio

- Transformar dados em formato analítico

- Armazenar em um Data Warehouse relacional

- Disponibilizar os dados para análises e dashboards

- Utilizar Docker para padronização do ambiente

- Demonstrar domínio de ferramentas amplamente usadas em Engenharia de Dados

🧩 Principais Etapas da Pipeline
1️⃣ Extração de Dados

- Leitura de um arquivo CSV contendo capitais brasileiras

- Consumo da API de Geolocalização da OpenWeather

- Consumo da API One Call (clima atual)

2️⃣ Validação de Dados

Uso do Pydantic para:

- Validar tipos

- Validar intervalos (latitude, longitude, temperatura, umidade, pressão)

- Separação de registros válidos e inválidos

- Persistência dos dados validados para rastreabilidade

3️⃣ Transformação

- Normalização de estruturas JSON

- Criação de colunas derivadas:

- Data, hora, ano, mês, dia

- Indicadores booleanos (chuva, umidade alta, sensação térmica elevada)

- Conversão para formato analítico (Parquet)

4️⃣ Carga de Dados

- Inserção no PostgreSQL utilizando SQLAlchemy

- Modelagem em esquema estrela

- UPSERT na dimensão de cidades

- Controle de duplicidade na tabela fato

5️⃣ Análise e Visualização

- Conexão direta do Power BI ao PostgreSQL

- Criação de relatórios e dashboards analíticos

🏗️ Arquitetura do Projeto
![Arquitetura](pics/arquitetura.png)

📁 Estrutura do Projeto

```
learning-airflow/
│
├── dags/
│   └── etl.py
│
├── include/
│   ├── extracao/
│   │   ├── extracao_cidade.py
│   │   └── extracao_clima.py
│   │
│   ├── validacao/
│   │   ├── validacao_cidades.py
│   │   └── validacao_clima.py
│   │
│   ├── transformacao/
│   │   └── transformacao.py
│   │
│   ├── carregamento/
│   │   └── carregamento_banco.py
│   │
│   ├── config/
│   │   └── caminhos.py
│   │
│   └── data/
│       └── capitais_brasil.csv
│
├── docker-compose.yml
├── .env
└── README.md
```

🛠️ Tecnologias Utilizadas
💻 Backend / Engenharia de Dados

- Python

- Apache Airflow (orquestração)

- Pandas (transformações)

- Pydantic (validação de dados)

- SQLAlchemy (integração com banco)

- PostgreSQL (Data Warehouse)

- Docker & Docker Compose

- OpenWeather API

📊 Análise de Dados

- Power BI

- Modelagem dimensional (Star Schema)

📊 Resultados

- Pipeline executando automaticamente

- Dados atualizados de forma incremental

- Base confiável para análises climáticas

- Projeto pronto para ser expandido (forecast, históricos, alertas, etc.)

🚀 Diferenciais do Projeto

- Pipeline real com API externa
- Orquestração com Airflow
- Validação robusta com Pydantic
- Modelagem analítica
- Integração com BI
- Ambiente Dockerizado
- Código modular e escalável
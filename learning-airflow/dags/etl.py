import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from airflow.decorators import dag, task
from datetime import datetime, timedelta
import pandas as pd
from include.config.caminhos import data_dir

from include.extracao.extracao_cidade import extracao_dados_cidades
from include.extracao.extracao_clima import extracao_clima
from include.validacao.validacao_cidades import validar_cidades
from include.validacao.validacao_clima import validar_clima
from include.transformacao.transformacao import transformar_clima
from include.carregamento.carregamento_banco import carregar_dados


@dag(
    dag_id="etl_clima_brasil",
    description="ETL de clima do Brasil: cidades e clima atual",
    start_date=datetime(2026, 1, 16),
    schedule=timedelta(hours=1),
    catchup=False,
    tags=["clima", "ETL", "OpenWeather"]
)
def pipeline_clima():

    @task(task_id="extrair_cidades")
    def task_extrair_cidades():
        caminho_entrada = data_dir / "capitais_brasil.csv"
        df_cidades = pd.read_csv(caminho_entrada)
        dados_cidades = extracao_dados_cidades(df_cidades)
        return dados_cidades

    @task(task_id="validar_cidades")
    def task_validar_cidades(dados_cidades):
        cidades_validas = validar_cidades(dados_cidades)
        return cidades_validas

    @task(task_id="extrair_clima")
    def task_extrair_clima(cidades_validas):
        dados_clima = extracao_clima(cidades_validas)
        return dados_clima

    @task(task_id="validar_clima")
    def task_validar_clima(dados_clima):
        clima_validado = validar_clima(dados_clima)
        return clima_validado

    @task(task_id="transformar_clima")
    def task_transformar_clima(dados_clima_validados):
        df_transformado = transformar_clima(dados_clima_validados)
        return df_transformado

    @task(task_id="carregar_dados")
    def task_carregar(df_transformado):
        return carregar_dados(df_transformado)

    cidades = task_extrair_cidades()
    cidades_validas = task_validar_cidades(cidades)
    clima = task_extrair_clima(cidades_validas)
    clima_valido = task_validar_clima(clima)
    df_transformado = task_transformar_clima(clima_valido)
    task_carregar(df_transformado)


pipeline_etl_clima = pipeline_clima()

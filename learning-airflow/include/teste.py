import requests
from dotenv import load_dotenv
import pandas as pd
import os
from pydantic import BaseModel,RootModel, ValidationError
from datetime import datetime
import json

base_diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(base_diretorio, 'data', 'dados_cidades.json')

with open(caminho_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

class Cidades(BaseModel):
    nome: str
    estado: str
    latitude: float
    longitude: float

class ListaCidades(RootModel[list[Cidades]]):
    pass

try:
    cidades_validadas = ListaCidades.model_validate(dados)
    print('Todos os dados validados.')
except ValidationError as e:
    print("Erros encontrados:", e)







# load_dotenv()
# api_key = os.getenv('api_key')
# url_dados = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitue}&lon={longitude}&units=metric&appid={api_key}'
# response = requests.get(url_dados)
# print(response.json())

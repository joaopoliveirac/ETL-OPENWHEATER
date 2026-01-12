import requests
import json
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
api_key = os.getenv('api_key')

cidade = 'Uberlândia'
estado = 'Minas gerais'

validos = []
invalidos = []
df_cida

for i, row in
url_cidade = f'http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},&appid={api_key}'
response = requests.get(url_cidade)
dados = response.json()[0]
nome_cidade = dados.get('name')
nome_estado = dados.get('state')
latitue = dados.get('lat')
longitude = dados.get('lon')
validos.append({'nome': nome_cidade, 'estado': nome_estado, 'latitude': latitue, 'longitude': longitude})
df = pd.DataFrame(validos)
df.to_json(r'learning-airflow\include\data\uberlandia.json', orient='records', force_ascii=False)

url_dados = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitue}&lon={longitude}&units=metric&appid={api_key}'
response_1 = requests.get(url_dados)
print(response_1.json())

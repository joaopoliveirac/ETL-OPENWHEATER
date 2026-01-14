import requests
from dotenv import load_dotenv
import pandas as pd
import os
from pydantic import BaseModel,RootModel, ValidationError, field_validator
from datetime import datetime
import json

load_dotenv()
api_key = os.getenv('api_key')

base_diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(base_diretorio, 'data', 'dados_cidades.json')
caminho_invalidos = os.path.join(base_diretorio, 'data', 'dados_cidades_invalidos.json')

with open(caminho_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

class Cidades(BaseModel):
    nome: str
    estado: str
    latitude: float
    longitude: float

    @field_validator('latitude')
    @classmethod
    def validar_latitude(cls,v):
        if not -90 <= v <= 90:
            raise ValueError("Latitute inválida")
        return v
    
    @field_validator('longitude')
    @classmethod
    def validar_longitude(cls,v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude inválida")
        return v

dados_validos: list[Cidades] = []
dados_invalidos: list[dict] = []

for i, item in enumerate(dados):
    try:
        cidade = Cidades.model_validate(item)
        dados_validos.append(cidade)
    except ValidationError as e:
        dados_invalidos.append({'index': i, 'erro': e.errors(), 'registro': item})

with open(caminho_invalidos, 'w', encoding='utf-8') as f:
    json.dump(dados_invalidos, f, ensure_ascii=False, indent=2)

print(f"Registros válidos: {len(dados_validos)}")
print(f"Registros inválidos: {len(dados_invalidos)}")


print(type((dados_validos)[0]))
# url_dados = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitue}&lon={longitude}&units=metric&appid={api_key}'
# response = requests.get(url_dados)
# print(response.json())

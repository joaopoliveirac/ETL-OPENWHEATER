from dotenv import load_dotenv
import pandas as pd
import os
from pydantic import BaseModel,RootModel, ValidationError, field_validator
from datetime import datetime
import json
from include.config.caminhos import data_dir

load_dotenv()
api_key = os.getenv('api_key')

caminho_json = data_dir / "cidades.json"
caminho_invalidos = data_dir / "cidades_invalidas.json"
caminho_validos = data_dir / "cidades_validas.json"

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

with open(caminho_validos, 'w', encoding='utf-8') as f:
    json.dump([c.model_dump() for c in dados_validos], f, ensure_ascii=False, indent=2)

with open(caminho_invalidos, 'w', encoding='utf-8') as f:
    json.dump(dados_invalidos, f, ensure_ascii=False, indent=2)

print(f"Registros válidos: {len(dados_validos)}")
print(f"Registros inválidos: {len(dados_invalidos)}")

import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import json
import pandas as pd
from include.config.caminhos import data_dir

load_dotenv()
api_key = os.getenv("api_key")

caminho_validos = data_dir / "cidades_validas.json"

with open(caminho_validos, 'r', encoding='utf-8') as f:
    cidades = json.load(f)

for cidade in cidades:
    lat = cidade.get('latitude')
    lon = cidade.get('longitude')
    print(lat,lon)

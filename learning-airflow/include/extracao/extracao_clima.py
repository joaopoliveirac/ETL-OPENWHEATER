import requests
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("api_key")

def extracao_clima(cidades_validas):
    dados = []
    for cidade in cidades_validas:
        nome = cidade['nome']
        estado = cidade['estado']
        lat = cidade['latitude']
        lon = cidade['longitude']
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid={api_key}'
        try:
            response = requests.get(url)
            json_response = response.json()
            if not json_response:
                continue
            json_response['nome'] = nome
            json_response['estado'] = estado
            dados.append(json_response)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao consumir API | url={url} | erro={e}")
    return dados

import requests
from dotenv import load_dotenv
import pandas as pd
import os
from include.config.caminhos import include_dir, data_dir

load_dotenv()
api_key = os.getenv("api_key")

caminho_entrada = data_dir / "capitais_brasil.csv"
caminho_saida = data_dir / "cidades.json"

def extracao_dados_cidades(df_cidades: pd.DataFrame) -> list[dict]:
    dados_geograficos_validos = []
    for row in df_cidades.itertuples(index=False):
        cidade = row.cidade
        estado = row.estado
        url_cidade = f'http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},&appid={api_key}'

        try:
            response = requests.get(url_cidade)
            json_response = response.json()
            if not json_response:
                continue
            dados = response.json()[0]
            nome_cidade = dados.get('name')
            nome_estado = dados.get('state')
            latitue = dados.get('lat')
            longitude = dados.get('lon')
            dados_geograficos_validos.append({'nome': nome_cidade, 'estado': nome_estado, 'latitude': latitue, 'longitude': longitude})
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao consumir API | url={url_cidade} | erro={e}")
    
    return dados_geograficos_validos


def main():
    df_cidades = pd.read_csv(caminho_entrada)
    dados = extracao_dados_cidades(df_cidades)
    df_dados_cidades = (pd.DataFrame(dados).drop_duplicates(subset=['latitude', 'longitude']))
    df_dados_cidades.to_json(caminho_saida, orient='records', force_ascii=False, indent=2)

if __name__ == "__main__":
    main()




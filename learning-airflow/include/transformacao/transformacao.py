import pandas as pd

def transformar_clima(dados_clima_validados):
    df = pd.json_normalize(dados_clima_validados)

    df = df.rename(columns={
        "nome": "cidade",
        "estado": "estado",
        "lat": "latitude",
        "lon": "longitude",
        "current.dt": "data_hora",
        "current.temp": "temperatura",
        "current.feels_like": "sensacao_termica",
        "current.humidity": "umidade",
        "current.pressure": "pressao",
        "current.wind_speed": "vento_velocidade",
        "current.weather": "weather"
    })

    df["data_hora"] = pd.to_datetime(df["data_hora"], utc=True)
    df["data"] = df["data_hora"].dt.date
    df["hora"] = df["data_hora"].dt.hour
    df["ano"] = df["data_hora"].dt.year
    df["mes"] = df["data_hora"].dt.month
    df["dia"] = df["data_hora"].dt.day

    df["condicao_clima"] = df["weather"].apply(lambda x: x[0]["main"] if isinstance(x, list) and len(x) > 0 else None)
    df["descricao_clima"] = df["weather"].apply(lambda x: x[0]["description"] if isinstance(x, list) and len(x) > 0 else None)
    df = df.drop(columns=["weather"])

    df["is_chuva"] = df["condicao_clima"].str.lower().eq("rain")
    df["umidade_alta"] = df["umidade"] >= 80
    df["sensacao_calor"] = df["sensacao_termica"] >= 30

    colunas_finais = [
        "cidade", "estado", "latitude", "longitude",
        "data_hora", "data", "hora", "ano", "mes", "dia",
        "temperatura", "sensacao_termica", "umidade",
        "pressao", "vento_velocidade",
        "condicao_clima", "descricao_clima",
        "is_chuva", "umidade_alta", "sensacao_calor"
    ]

    return df[colunas_finais]

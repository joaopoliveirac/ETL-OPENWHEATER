from datetime import datetime, timezone
from pydantic import BaseModel, field_validator, ValidationError

def validar_clima(dados_clima):
    class Weather(BaseModel):
        main: str
        description: str
        model_config = {"extra": "ignore"}

    class CurrentWeather(BaseModel):
        dt: datetime
        temp: float
        feels_like: float
        pressure: int
        humidity: int
        wind_speed: float
        weather: list[Weather]
        model_config = {"extra": "ignore"}

        @field_validator("dt", mode="before")
        @classmethod
        def validar_timestamp(cls, v):
            return datetime.fromtimestamp(v, tz=timezone.utc)

    class CidadeClima(BaseModel):
        nome: str
        estado: str
        lat: float
        lon: float
        current: CurrentWeather
        model_config = {"extra": "ignore"}

    dados_validos = []
    for item in dados_clima:
        try:
            registro = CidadeClima(**item)
            dados_validos.append(registro.model_dump())
        except ValidationError:
            continue
    return dados_validos

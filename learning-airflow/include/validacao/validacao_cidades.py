from pydantic import BaseModel, ValidationError, field_validator

def validar_cidades(dados_cidades):
    class Cidades(BaseModel):
        nome: str
        estado: str
        latitude: float
        longitude: float

        @field_validator('latitude')
        @classmethod
        def validar_latitude(cls, v):
            if not -90 <= v <= 90:
                raise ValueError("Latitude inválida")
            return v

        @field_validator('longitude')
        @classmethod
        def validar_longitude(cls, v):
            if not -180 <= v <= 180:
                raise ValueError("Longitude inválida")
            return v

    dados_validos = []
    for i, item in enumerate(dados_cidades):
        try:
            cidade = Cidades.model_validate(item)
            dados_validos.append(cidade.model_dump())
        except ValidationError as e:
            # opcional: logar erros
            continue

    print(f"Registros válidos: {len(dados_validos)}")
    return dados_validos

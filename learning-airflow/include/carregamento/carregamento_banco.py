from sqlalchemy import create_engine, text

url_database = "postgresql+psycopg2://postgres:postgres@host.docker.internal:5440/etl_db"
engine = create_engine(url_database)

def carregar_dados(df_transformado):
    if df_transformado is None or df_transformado.empty:
        print("DataFrame vazio. Nada para carregar.")
        return "Carga não realizada - DataFrame vazio"

    with engine.begin() as conn:
        for _, row in df_transformado.iterrows():
            cidade_sql = text("""
                INSERT INTO dim_cidade (nome, estado, latitude, longitude)
                VALUES (:nome, :estado, :latitude, :longitude)
                ON CONFLICT (latitude, longitude)
                DO UPDATE SET nome = EXCLUDED.nome, estado = EXCLUDED.estado
                RETURNING cidade_id
            """)
            cidade_id = conn.execute(
                cidade_sql,
                {
                    "nome": row["cidade"],
                    "estado": row["estado"],
                    "latitude": row["latitude"],
                    "longitude": row["longitude"],
                }
            ).scalar()

            clima_sql = text("""
                INSERT INTO fato_clima_atual (
                    cidade_id, data_hora, data, hora, ano, mes, dia,
                    temperatura, sensacao_termica, umidade, pressao,
                    vento_velocidade, condicao_clima, descricao_clima,
                    is_chuva, umidade_alta, sensacao_calor
                )
                VALUES (
                    :cidade_id, :data_hora, :data, :hora, :ano, :mes, :dia,
                    :temperatura, :sensacao_termica, :umidade, :pressao,
                    :vento_velocidade, :condicao_clima, :descricao_clima,
                    :is_chuva, :umidade_alta, :sensacao_calor
                )
                ON CONFLICT (cidade_id, data_hora) DO NOTHING
            """)
            conn.execute(
                clima_sql,
                {**row, "cidade_id": cidade_id}
            )

    print("Carga concluída com sucesso!")
    return "Carga concluída"

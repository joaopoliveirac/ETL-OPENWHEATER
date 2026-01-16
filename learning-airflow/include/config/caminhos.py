from pathlib import Path

base_dir = Path(__file__).resolve().parents[2] #define o 'learning-airflow' como a raiz do projeto

include_dir = base_dir / "include"
data_dir = include_dir/ "data"
extracao_dir = include_dir / "extracao"
validacao_dir = include_dir / "validacao"
transformacao_dir = include_dir / "transformacao"
import pandas as pd
from sqlalchemy import create_engine

from app.src.config import DB_USER, DB_NAME, DB_PORT, DB_PASSWORD, DB_HOST, DB_PROVIDER
from app.src.query_sql import query

DB_URL = (
    f"{DB_PROVIDER}+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
          )
engine_sync = create_engine(DB_URL)

sessions_df = pd.read_sql_query("SELECT * FROM web_data.sessions;", engine_sync)
communications_df = pd.read_sql_query("SELECT * FROM web_data.communications;", engine_sync)


result_df = pd.read_sql_query(query, engine_sync)


print(result_df.head())

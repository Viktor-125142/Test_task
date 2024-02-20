import pandas as pd
from app.src.database import get_session
from sqlalchemy import text
import asyncio

from app.src.query_sql import query

async def execute_sql_queries():
    async for session in get_session():
        query_sql = query
        result = await session.execute(text(query_sql))
        data = result.fetchall()

        return data

async def main():
    result = await execute_sql_queries()
    result_df = pd.DataFrame(result)

    print(result_df.head())


asyncio.run(main())

import pandas as pd
from sqlalchemy import text
from app.src.database import get_session
import asyncio

async def execute_sql_queries():
    async for session in get_session():
        sessions_query = text("SELECT * FROM web_data.sessions;")
        sessions_result = await session.execute(sessions_query)
        sessions_data = sessions_result.fetchall()

        communications_query = text("SELECT * FROM web_data.communications;")
        communications_result = await session.execute(communications_query)
        communications_data = communications_result.fetchall()

    return sessions_data, communications_data

async def main():
    result = await execute_sql_queries()
    sessions_data, communications_data = result
    sessions_df = pd.DataFrame(sessions_data)
    communications_df = pd.DataFrame(communications_data)

    print("Sessions DataFrame:")
    print(sessions_df.head())
    print("\nCommunications DataFrame:")
    print(communications_df.head())


asyncio.run(main())

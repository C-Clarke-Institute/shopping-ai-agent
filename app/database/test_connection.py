from sqlalchemy import text

from app.database.connection import engine

try:

    with engine.connect() as connection :

        result = connection.execute(
            text("SELECT version()")
        )

        print("Database connected Successfully !.")

        print(result.scalar())
        
except Exception as e:

    print("Database connection failed")
    print(e)
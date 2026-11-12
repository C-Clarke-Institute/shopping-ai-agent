from app.database.base import Base
from app.database.connection import engine

import app.models

def create_tabls():

    print("registerd tables : " , Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)
    print("Databe Tables created successfully.")


if __name__ == "__main__":
    create_tabls()
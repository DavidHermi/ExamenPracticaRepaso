import sqlite3

import pathlib


def createConnection(bdPath: str)-> sqlite3.Connection:
    pathToDB=pathlib.Path(bdPath).absolute().as_uri()

    try:

        connection=sqlite3.connect(f"{pathToDB}?mode=rw", uri=True)

    except:
        print(f"Error: La base de datos no existe")

    return connection

import logging
import urllib
from datetime import datetime
import uuid
import os

import azure.functions as func
from sqlalchemy import create_engine, Table, DateTime, Column, MetaData, String

engine = None

# Information used to build the connection string,
# stored in the local.settings.json file.
server = os.environ["DATABASE_SERVER"]
database = os.environ["DATABASE"]
user_id = os.environ["DATABASE_USER"]
password = os.environ["DATABASE_USER_PASSWORD"]

def init_engine():
    global engine
    if engine is None:
        odbc = urllib.parse.quote_plus(
            "Driver={ODBC Driver 17 for SQL Server};"
            f"Server=tcp:{server}.database.windows.net,1433;"
            f"Database={database};"
            f"Uid={user_id};"
            f"Pwd={password};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={odbc}")

def main(req: func.HttpRequest) -> func.HttpResponse:
    init_engine()
    m = MetaData()
    t = Table(
        'test_table', m,
        Column('timestamp', DateTime, primary_key=True),
        Column('uuid', String),
        Column('user_agent', String),
        implicit_returning=False
    )

    m.create_all(engine)
    with engine.begin() as conn:
        timestamp = datetime.utcnow()
        uuid_ = str(uuid.uuid4())
        user_agent = req.headers.get('User-Agent')

        logging.info(f"Insert data entry: timestamp={timestamp}, uuid={uuid_}, user_agent={user_agent}")
        conn.execute(t.insert(), {'timestamp': timestamp, 'uuid': uuid_, 'user_agent': user_agent})

    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
    )

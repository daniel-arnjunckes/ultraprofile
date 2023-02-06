from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ as sys_env

# pg_db_name  = sys_env("PG_DATABASE")
# pg_db_host  = sys_env("PG_HOSTNAME")
# pg_db_user  = sys_env("PG_USER")
# pg_db_pwd   = sys_env("PG_PASSWORD")

# SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(pg_db_user,pg_db_pwd,pg_db_host,pg_db_name)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/profiles"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {}
)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
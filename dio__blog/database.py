import os
import databases
import sqlalchemy as sa

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

engine_options = {}

if DATABASE_URL.startswith("sqlite"):
    engine_options["connect_args"] = {"check_same_thread": False}

engine = sa.create_engine(DATABASE_URL, **engine_options)

from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.sql.expression import Executable, ClauseElement

# For Demo only. Read from Env Normally
engine = create_engine(
    "postgresql://zarasupersetdb:easypassword@localhost:5432/zarasupersetdb"
)


class InjectorWithSchema:
    def data_injector(self, files, table_name, schema, exists='append'):
        # Write data into the table in PostgreSQL database
        for file in files:
            data = pd.read_csv(file)
            data.to_sql(table_name, engine, dtype=schema, if_exists=exists)

    def data_list_injector(self, list, table_name, schema):
        pd.DataFrame(list).to_sql(table_name, engine,
                                  dtype=schema, if_exists="replace")


class CreateView:
    def __init__(self, statement):
        self.engine = engine
        self.select = statement

    def view_creator(self):
        """Create DB Views"""
        self.engine.execute(self.select)

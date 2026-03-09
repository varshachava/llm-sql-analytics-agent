import pandas as pd
from sqlalchemy import create_engine


class DatabaseManager:

    def __init__(self):

        self.engine = create_engine("sqlite:///analytics.db")

    def create_tables(self, df):

        df.to_sql(
            "tasks",
            self.engine,
            if_exists="replace",
            index=False
        )

    def run_query(self, sql):

        result = pd.read_sql(sql, self.engine)

        return result

    def preview_data(self):

        query = """
        SELECT * FROM tasks
        LIMIT 10
        """

        return pd.read_sql(query, self.engine)

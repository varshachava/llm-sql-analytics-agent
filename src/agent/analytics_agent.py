from src.database.database_manager import DatabaseManager
from src.llm.sql_generator import SQLGenerator


class AnalyticsAgent:

    def __init__(self, api_key):

        self.database = DatabaseManager()

        self.llm = SQLGenerator(api_key)

    def answer_question(self, question):

        sql_query = self.llm.generate_sql(question)

        print("Generated SQL:")
        print(sql_query)

        result = self.database.run_query(sql_query)

        return result

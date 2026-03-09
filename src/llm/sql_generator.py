import openai


class SQLGenerator:

    def __init__(self, api_key):

        openai.api_key = api_key

    def generate_sql(self, question):

        prompt = f"""
You are an analytics assistant.

Convert the following question into SQL.

Table:
tasks(task_id, region, worker_id, task_type,
completion_time, task_cost, quality_score)

Question:
{question}

Return SQL only.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        sql = response["choices"][0]["message"]["content"]

        return sql

from src.ingestion.data_loader import DataLoader
from src.database.database_manager import DatabaseManager
from src.analytics.analytics_engine import AnalyticsEngine
from src.agent.analytics_agent import AnalyticsAgent


dataset_path = "data/analytics_dataset.csv"

loader = DataLoader(dataset_path)

df = loader.load_dataset()

df = loader.clean_dataset(df)

db = DatabaseManager()

db.create_tables(df)

analytics = AnalyticsEngine(df)

metrics = analytics.compute_metrics()

print("Dataset Metrics")

print(metrics)

agent = AnalyticsAgent(api_key="YOUR_API_KEY")

question = "What is the average completion time by region?"

result = agent.answer_question(question)

print("Query Result")

print(result)

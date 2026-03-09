import pandas as pd


class DataLoader:

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path

    def load_dataset(self):

        df = pd.read_csv(self.dataset_path)

        return df

    def clean_dataset(self, df):

        df = df.drop_duplicates()

        df = df[df["completion_time"] > 0]

        df = df[df["task_cost"] > 0]

        return df

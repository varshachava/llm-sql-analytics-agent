class AnalyticsEngine:

    def __init__(self, df):

        self.df = df

    def compute_metrics(self):

        metrics = {}

        metrics["total_tasks"] = len(self.df)

        metrics["avg_completion_time"] = (
            self.df["completion_time"].mean()
        )

        metrics["avg_task_cost"] = (
            self.df["task_cost"].mean()
        )

        metrics["avg_quality_score"] = (
            self.df["quality_score"].mean()
        )

        metrics["tasks_by_region"] = (
            self.df.groupby("region")["task_id"].count()
        )

        return metrics

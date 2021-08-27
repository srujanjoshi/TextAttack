import numpy as np

from textattack.attack_results import SkippedAttackResult
from textattack.metrics import Metric


class AttackQueries(Metric):
    """Calculates all metrics related to number of queries in an attack

    Args:
    results (:obj::`list`:class:`~textattack.goal_function_results.GoalFunctionResult`):
                    Attack results for each instance in dataset
    """

    def __init__(self, results):
        self.results = results

        self.all_metrics = {}

    def calculate(self):
        self.num_queries = np.array(
            [
                r.num_queries
                for r in self.results
                if not isinstance(r, SkippedAttackResult)
            ]
        )
        self.all_metrics["avg_num_queries"] = self.avg_num_queries()

        return self.all_metrics

    def avg_num_queries(self):
        avg_num_queries = self.num_queries.mean()
        avg_num_queries = round(avg_num_queries, 2)
        return avg_num_queries
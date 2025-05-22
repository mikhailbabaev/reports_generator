from collections import defaultdict
from .base import Report
from typing import List, Dict, Any


class AverageRateReport(Report):
    def generate(self, data: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Возвращает среднюю почасовую ставку по отделам:
        {
            "Marketing": 45.0,
            "Design": 50.0,
            ...
        }
        """
        sums = defaultdict(float)
        counts = defaultdict(int)
        for row in data:
            dept = row.get("department", "Unknown")
            rate = row.get("hourly_rate", 0)
            if rate is None:
                continue
            sums[dept] += float(rate)
            counts[dept] += 1

        averages = {}
        for dept in sums:
            averages[dept] = sums[dept] / counts[dept] if counts[dept] > 0 else 0.0

        return averages

    def render(self, report_data: Dict[str, float]) -> str:
        lines = []
        header = f"{'Department':<20} {'Average Rate':<15}"
        lines.append(header)
        lines.append("-" * len(header))
        for dept, avg_rate in sorted(report_data.items()):
            lines.append(f"{dept:<20} {avg_rate:<15.2f}")
        return "\n".join(lines)
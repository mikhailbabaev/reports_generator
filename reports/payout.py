from .base import Report
from typing import List, Dict, Any


class PayoutReport(Report):
    def generate(self, data: List[Dict[str, Any]]) -> List[Dict]:
        """
        Возвращает список словарей:
        [
            {
                "department": str,
                "name": str,
                "hours_worked": float,
                "hourly_rate": float,
                "payout": float
            },
            ...
        ]
        """
        report_rows = []

        for row in data:
            department = row.get("department", "Unknown")
            name = row.get("name", "Unknown")
            hours = float(row.get("hours_worked", 0))
            rate = float(row.get("hourly_rate", 0))
            payout = hours * rate

            report_rows.append({
                "department": department,
                "name": name,
                "hours_worked": hours,
                "hourly_rate": rate,
                "payout": payout
            })

        return report_rows

    def render(self, report_data: List[Dict[str, Any]]) -> str:
        lines = []
        header = f"{'Department':<15} {'Name':<20} {'Hours':<10} {'Rate':<10} {'Payout':<10}"
        lines.append(header)
        lines.append("-" * len(header))
        for row in report_data:
            line = f"{row['department']:<15} {row['name']:<20} {row['hours_worked']:<10.2f} {row['hourly_rate']:<10.2f} {row['payout']:<10.2f}"
            lines.append(line)
        return "\n".join(lines)
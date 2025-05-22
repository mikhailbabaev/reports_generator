from .payout import PayoutReport
from .average_rate import AverageRateReport

report_registry = {
    "payout": PayoutReport,
    "average_rate": AverageRateReport,
}
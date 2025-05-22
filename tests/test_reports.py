import pytest
from reports.payout import PayoutReport


@pytest.fixture
def sample_data():
    """
    Типовой образец данных.
    """
    return [
        {
            "name": "Alice",
            "department": "Marketing",
            "hours_worked": 160,
            "hourly_rate": 50
        },
        {
            "name": "Bob",
            "department": "Design",
            "hours_worked": 150,
            "hourly_rate": 40
        }
    ]

def test_generate_payout_report(sample_data):
    """
    Тестируем, что возвращает метод generate,
    сравниваем длину возвращаемого списка с кол-вом сотрудников,
    проверка подсчета зарплаты.
    """
    report = PayoutReport()
    result = report.generate(sample_data)

    assert isinstance(result, list)
    assert len(result) == 2

    alice = result[0]
    assert alice["name"] == "Alice"
    assert alice["department"] == "Marketing"
    assert alice["hours_worked"] == 160
    assert alice["hourly_rate"] == 50
    assert alice["payout"] == 8000

    bob = result[1]
    assert bob["payout"] == 6000


def test_render_payout_report(sample_data):
    """
    Проверяем, чтобы возвращалась строка, проверяем ключи.
    """
    report = PayoutReport()
    report_data = report.generate(sample_data)
    output = report.render(report_data)

    assert isinstance(output, str)
    assert "Alice" in output
    assert "Marketing" in output
    assert "8000.00" in output
    assert "Bob" in output
    assert "6000.00" in output



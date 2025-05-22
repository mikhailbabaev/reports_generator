import pytest
from csv_loader import load_multiple_csv, map_header


@pytest.fixture
def sample_csv_files(tmp_path):
    """
    Фикстура типовых данных для тестирования.
    """
    file1 = tmp_path / "data1.csv"
    file1.write_text(
        "name,department,hours_worked,rate\n"
        "Alice,Marketing,160,50\n"
    )

    file2 = tmp_path / "data2.csv"
    file2.write_text(
        "name,department,hours_worked,salary\n"
        "Bob,Design,150,40\n"
    )

    return [str(file1), str(file2)]


def test_load_multiple_csv_normalizes_columns(sample_csv_files):
    """Проверяем, нормализованы ли заголовки,
    сравниваем число строк с числом файлов,
    проверяем ключи."""
    rows = load_multiple_csv(sample_csv_files)

    assert isinstance(rows, list)
    assert len(rows) == 2

    for row in rows:
        assert "hourly_rate" in row
        assert "rate" not in row
        assert "salary" not in row

    alice = rows[0]
    assert alice["name"] == "Alice"
    assert alice["hourly_rate"] == 50

    bob = rows[1]
    assert bob["name"] == "Bob"
    assert bob["hourly_rate"] == 40


def test_map_header():
    """Проверяем, как заменяются заголовки,
    проверка удаления проблелов и перевода в нижний регистр."""
    assert map_header("rate") == "hourly_rate"
    assert map_header("salary") == "hourly_rate"
    assert map_header("hourly_rate") == "hourly_rate"

    assert map_header("name") == "name"
    assert map_header("  Department ") == "department"

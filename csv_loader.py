from typing import List, Dict, Any


def map_header(header: str) -> str:
    """Замена заголовка на стандартный."""
    mapping = {
        "rate": "hourly_rate",
        "salary": "hourly_rate",
        "hourly_rate": "hourly_rate"
    }
    return mapping.get(header.strip().lower(), header.strip().lower())


def load_one_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Подгрузка одного csv файла.
    """
    with open(file_path, encoding='utf-8') as f:
        lines = f.read().splitlines()

    if not lines:
        return []

    headers = [map_header(i) for i in lines[0].split(",")]
    rows = []

    for line in lines[1:]:
        values = line.split(",")
        row = dict(zip(headers, values))
        if 'hours_worked' in row:
            row['hours_worked'] = float(row['hours_worked'])
        if 'hourly_rate' in row:
            row['hourly_rate'] = float(row['hourly_rate'])
        rows.append(row)

    return rows


def load_multiple_csv(files: List[str]) -> List[Dict[str, Any]]:
    """
    Подгрузка всех отчетов.
    """
    data = []
    for file in files:
        data.extend(load_one_csv(file))
    return data
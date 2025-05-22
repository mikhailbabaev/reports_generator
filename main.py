import os
import sys
import argparse
from typing import List, Optional, Any
from csv_loader import load_multiple_csv
from reports import report_registry


def check_files_exist(files: List[str]) -> bool:
    """Проверяет, что все файлы из списка существуют.
    """
    for file_path in files:
        if not os.path.isfile(file_path):
            print(f"Ошибка: файл не найден — {file_path}")
            return False
    return True


def get_report_class(report_type: str) -> Optional[Any]:
    """Проверка названия отчёта по его имени из реестра.
    """
    report_class = report_registry.get(report_type)
    if report_class is None:
        print(f"Ошибка: неизвестный тип отчёта '{report_type}'.")
        print(f"Доступные типы: {', '.join(report_registry.keys())}")
    return report_class


def main():
    """
    Основная функция запуска генератора отчётов.
    """
    cmd_parser = argparse.ArgumentParser(description="Salary report generator")
    cmd_parser.add_argument("files", nargs="+",
                            help="CSV file paths")
    cmd_parser.add_argument("--report",
                            required=True,
                            help="Report type to generate")
    args = cmd_parser.parse_args()


    if not check_files_exist(args.files):
        sys.exit(1)

    report_class = get_report_class(args.report)
    if not report_class:
        sys.exit(1)
    try:
        data = load_multiple_csv(args.files)
        if not data:
            print("Внимание: данные пусты. Проверьте содержимое файлов.")
            sys.exit(1)

        report = report_class()
        report_data = report.generate(data)
        output = report.render(report_data)
        print(output)
    except Exception as e:
        print(f"При генерации отчёта произошла ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
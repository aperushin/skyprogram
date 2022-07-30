import json


def load_json(filename: str) -> list | dict:
    """Загружает данные из JSON-файла"""
    with open(filename, encoding='utf8') as f:
        return json.load(f)


def write_json(data: list | dict, filename: str) -> None:
    """Записывает данные в JSON-файл, перезаписывая содержимое"""
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f)

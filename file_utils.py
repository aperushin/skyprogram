import json


def load_json(filename: str) -> list | dict:
    """Load data from a JSON file"""
    with open(filename, encoding='utf8') as f:
        return json.load(f)


def write_json(data: list | dict, filename: str) -> None:
    """Write data to a JSON file, overwriting the existing contents"""
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f)

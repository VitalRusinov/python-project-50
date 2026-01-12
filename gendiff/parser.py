import json


def get_data(filepath):
    """
    Read and parse JSON file.

    Args:
        filepath (str): Path to JSON file

    Returns:
        dict or list: Parsed data from file

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If invalid JSON
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filepath}' not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in '{filepath}'")
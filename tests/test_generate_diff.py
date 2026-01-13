# tests/test_generate_diff.py
import os

from gendiff.generate_diff import generate_diff


# Получаем путь к фикстурам
def get_fixture_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "..", "fixtures", filename)


def test_generate_diff():
    """
    Проверяем, что generate_diff правильно сравнивает file1.json и file2.json
    и возвращает результат, который совпадает с result.txt
    """
    # Получаем пути к файлам
    file1_path = get_fixture_path("file1.json")
    file2_path = get_fixture_path("file2.json")
    result_path = get_fixture_path("result.txt")

    # Запускаем функцию сравнения
    actual_result = generate_diff(file1_path, file2_path)

    # Читаем ожидаемый результат
    with open(result_path, "r", encoding="utf-8") as f:
        expected_result = f.read()

    # Сравниваем
    assert actual_result == expected_result, (
        "Результат не совпадает с ожидаемым"
    )

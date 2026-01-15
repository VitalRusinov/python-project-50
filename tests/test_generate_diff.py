import json
import os

from gendiff import generate_diff


def get_fixture_path(filename):
    """Get path to fixture file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", filename)


def read_fixture(filename):
    """Read fixture file."""
    with open(get_fixture_path(filename), "r", encoding="utf-8") as f:
        return f.read()


def test_generate_diff_flat_json():
    """Test flat JSON comparison."""
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    result = read_fixture("result.txt")

    actual = generate_diff(file1, file2)
    assert actual == result


def test_generate_diff_flat_yaml():
    """Test flat YAML comparison."""
    file1 = get_fixture_path("file1.yml")
    file2 = get_fixture_path("file2.yaml")
    result = read_fixture("result.txt")

    actual = generate_diff(file1, file2)
    assert actual == result


def test_generate_diff_recursive_json():
    """Test recursive JSON comparison."""
    file1 = get_fixture_path("file_recursive1.json")
    file2 = get_fixture_path("file_recursive2.json")
    result = read_fixture("result_recursive.txt")

    actual = generate_diff(file1, file2)
    assert actual == result


def test_generate_diff_recursive_yaml():
    """Test recursive YAML comparison."""
    file1 = get_fixture_path("file_recursive1.yml")
    file2 = get_fixture_path("file_recursive2.yaml")
    result = read_fixture("result_recursive.txt")

    actual = generate_diff(file1, file2)
    assert actual == result


def test_default_format():
    """Test that default format is stylish."""
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    result_without_format = generate_diff(file1, file2)
    result_with_format = generate_diff(file1, file2, "stylish")

    assert result_without_format == result_with_format


def test_generate_diff_plain_format():
    """Test plain format output."""
    file1 = get_fixture_path("file_recursive1.json")
    file2 = get_fixture_path("file_recursive2.json")

    expected_plain = read_fixture("result_plain.txt")
    actual = generate_diff(file1, file2, "plain")

    assert actual == expected_plain


def test_generate_diff_plain_format_flat():
    """Test plain format for flat files."""
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    expected_plain_flat = read_fixture("result_plain_flat.txt")
    actual = generate_diff(file1, file2, "plain")

    assert actual == expected_plain_flat


def test_generate_diff_json_format():
    """Test JSON format output."""
    file1 = get_fixture_path("file_recursive1.json")
    file2 = get_fixture_path("file_recursive2.json")

    # Получаем результат
    actual_json = generate_diff(file1, file2, "json")

    # Читаем ожидаемый результат из файла
    expected_json = read_fixture("result_json.txt")

    # Для точного сравнения
    assert actual_json == expected_json

    # Дополнительная проверка, что это валидный JSON
    parsed_actual = json.loads(actual_json)
    parsed_expected = json.loads(expected_json)
    assert parsed_actual == parsed_expected


def test_generate_diff_json_format_flat():
    """Test JSON format for flat files."""
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    # Получаем результат
    actual_json = generate_diff(file1, file2, "json")

    # Читаем ожидаемый результат из файла
    expected_json = read_fixture("result_json_flat.txt")

    # Для точного сравнения
    assert actual_json == expected_json

    # Дополнительная проверка, что это валидный JSON
    parsed_actual = json.loads(actual_json)
    parsed_expected = json.loads(expected_json)
    assert parsed_actual == parsed_expected

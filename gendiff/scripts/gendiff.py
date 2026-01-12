#!/usr/bin/env python3
"""
CLI-утилита для сравнения конфигурационных файлов.
"""

import argparse
from gendiff.parser import get_data


def validate_format(format_value):
    """Проверяет, что формат корректен."""
    valid_formats = ['stylish', 'plain', 'json']
    if format_value not in valid_formats:
        raise argparse.ArgumentTypeError(
            f'Invalid format "{format_value}". '
            f'Allowed values: {", ".join(valid_formats)}'
        )
    return format_value


def main():
    """Основная функция, запускаемая при вызове скрипта."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Позиционные аргументы
    parser.add_argument('first_file', help='path to first configuration file')
    parser.add_argument('second_file', help='path to second configuration file')

    # Опция --format
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        type=validate_format,
    )

    # Парсим аргументы
    args = parser.parse_args()

    # Читаем и парсим файлы
    data1 = get_data(args.first_file)
    data2 = get_data(args.second_file)

    # Выводим результат (временно)
    print(f"Comparing: {args.first_file} with {args.second_file}")
    print(f"Data from {args.first_file}: {data1}")
    print(f"Data from {args.second_file}: {data2}")
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()
# #!/usr/bin/env python3
# """
# CLI-утилита для сравнения конфигурационных файлов.
# """

# import argparse
# import os


# def validate_file(file_path):
#     """Проверяет, существует ли файл."""
#     if not os.path.exists(file_path):
#         raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist")
#     return file_path


# def main():
#     """Основная функция, запускаемая при вызове скрипта."""
#     parser = argparse.ArgumentParser(
#         description='Compares two configuration files and shows a difference.',
#         # Добавляем эпилог для дополнительной информации
#         epilog='Example: gendiff file1.json file2.json',
#     )

#     # Добавляем аргументы с валидацией
#     parser.add_argument(
#         'first_file',
#         type=validate_file,  # автоматическая проверка файла
#         help='path to first configuration file'
#     )

#     parser.add_argument(
#         'second_file',
#         type=validate_file,
#         help='path to second configuration file'
#     )

#     # ДОБАВЛЯЕМ ОПЦИЮ --format (или -f)
#     parser.add_argument(
#         '-f', '--format',  # Два варианта: короткий (-f) и длинный (--format)
#         help='set format of output',  # Текст справки
#         default='stylish',  # Значение по умолчанию (позже заменим)
#     )

#     args = parser.parse_args()

#     # Основная логика (заглушка)
#     print(f"Comparing:")
#     print(f"  File 1: {args.first_file}")
#     print(f"  File 2: {args.second_file}")
#     print(f"Output format: {args.format}")
#     print("\nDifference will be implemented in next steps.")


# if __name__ == '__main__':
#     main()
#!/usr/bin/env python3
"""
CLI-утилита для сравнения конфигурационных файлов.
"""

import argparse

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

    # Добавляем позиционные аргументы (обязательные)
    parser.add_argument('first_file', help='path to first configuration file')
    parser.add_argument('second_file', help='path to second configuration file')

    # ДОБАВЛЯЕМ ОПЦИЮ --format (или -f)
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        type=validate_format,  # Добавляем валидацию
    )

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Выводим полученные аргументы для отладки
    print(f"Comparing: {args.first_file} with {args.second_file}")
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()
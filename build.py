import requests
import json
import os
from pathlib import Path
import sys
import re
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Константы
FILE_STRUCTURES = {
    'ContextMenu_RU.txt': {
        'table_name': 'ContextMenu_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Farming_UA.txt': {
        'table_name': 'Farming_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'IG_UI_RU.txt': {
        'table_name': 'IGUI_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'ItemName_UA.txt': {
        'table_name': 'ItemName_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Items_RU.txt': {
        'table_name': 'Items_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Recipes_RU.txt': {
        'table_name': 'Recipes_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Tooltip_RU.txt': {
        'table_name': 'Tooltip_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'UI_RU.txt': {
        'table_name': 'UI_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Moodles_RU.txt': {
        'table_name': 'Moodles_RU',
        'header_comments': ['////DRTranslate Team////']
    },
}


def fetch_data(api_url):
    """
    Получение данных из Google Sheets через POST запрос.
    """
    try:
        response = requests.post(api_url, json={"method":"export"})
        response.raise_for_status()
        print(response.content)
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Ошибка при запросе данных: {e}")
        sys.exit(1)

def read_last_checksum(checksum_file):
    """
    Чтение последнего хеша из файла.
    """
    try:
        if os.path.exists(checksum_file):
            with open(checksum_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except Exception as e:
        logging.error(f"Ошибка чтения файла хеша: {e}")
    return ""


def write_checksum(checksum_file, checksum):
    """
    Запись нового хеша в файл.
    """
    try:
        with open(checksum_file, 'w', encoding='utf-8') as f:
            f.write(checksum)
    except Exception as e:
        logging.error(f"Ошибка записи файла хеша: {e}")


def build_mod(data, output_dir):
    """
    Сборка мода из данных в соответствующие файлы с Lua-таблицами.
    """
    os.makedirs(output_dir, exist_ok=True)
    translations = {}

    # Регулярные выражения для преобразования пути
    mod_name_pattern = re.compile(r'^mods/[^/]+/')
    en_pattern = re.compile(r'/EN/([^/]+)_EN\.txt$')

    # Группировка данных по файлам
    for entry in data.get('data', []):
        original_path = entry['path'].replace('\\', '/')
        key = entry['key']
        string = entry['string']

        # Преобразование пути
        new_path = mod_name_pattern.sub('mods/DRTranslate/', original_path)
        new_path = en_pattern.sub(r'/RU/\1_RU.txt', new_path)

        if new_path == original_path:
            logging.warning(f"Путь не преобразован, возможно некорректный формат: {original_path}")
            continue

        translations.setdefault(new_path, []).append({
            'original_path': original_path,
            'key': key,
            'string': string
        })

    # Запись переводов в соответствующие файлы
    for new_path, entries in translations.items():
        full_path = Path(output_dir) / new_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        filename = full_path.name
        file_structure = FILE_STRUCTURES.get(filename, {
            'table_name': filename.replace('_RU.txt', '_Unknow_RU'),
            'header_comments': []
        })
        table_name = file_structure['table_name']
        header_comments = file_structure['header_comments']

        grouped_by_original = {}
        for entry in entries:
            grouped_by_original.setdefault(entry['original_path'], []).append((entry['key'], entry['string']))

        try:
            with open(full_path, 'w', encoding='cp1251', errors='replace') as f:
                f.write(f"{table_name} = {{\n")
                for comment in header_comments:
                    f.write(f"\t{comment}\n")
                if header_comments:
                    f.write("\n")

                # Запись данных
                for orig_path, key_string_pairs in grouped_by_original.items():
                    f.write(f"\t////Original path: {orig_path}////\n")
                    for key, string in key_string_pairs:
                        clean_string = string.replace('"', '\\"')
                        f.write(f'\t{key} = "{clean_string}",\n')
                    f.write("\n")
                f.write("}\n")
            logging.info(f"Файл создан: {full_path}")
        except Exception as e:
            logging.error(f"Ошибка записи файла {full_path}: {e}")

    if not translations:
        logging.warning("Нет данных для записи")
    logging.info(f"Мод собран в {output_dir}")


def main():
    """
    Основная функция для запуска скрипта.
    """
    api_url = os.getenv("GOOGLE_SHEETS_API_URL")
    checksum_file = "github/workspace/hash.txt"
    output_dir = "github/workspace/Contents/"

    if not api_url:
        logging.error("Переменная окружения GOOGLE_SHEETS_API_URL не установлена.")
        sys.exit(1)

    data = fetch_data(api_url)
    new_checksum = data.get('hash', '')

    if not new_checksum:
        logging.error("Ошибка: checksum отсутствует в данных.")
        sys.exit(1)

    old_checksum = read_last_checksum(checksum_file)

    if old_checksum == new_checksum:
        logging.info("Хеш не изменился, сборка не требуется.")
        print("::set-output name=BUILD_REQUIRED::false")
        return

    build_mod(data, output_dir)
    write_checksum(checksum_file, new_checksum)
    logging.info("Сборка завершена.")
    print("::set-output name=BUILD_REQUIRED::true")


if __name__ == "__main__":
    main()

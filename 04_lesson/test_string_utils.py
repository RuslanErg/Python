import pytest
from string_utils import StringUtils

# Тесты для класса StringUtils
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # обычный случай
    ("skyPro", "Skypro"),          # с заглавной буквой в середине
    ("", ""),                        # пустая строка
    ("a", "A"),                     # строка из одной буквы
    ("ABC", "Abc"),                 # строка из заглавных букв
])
def test_capitalize(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),        # пробелы в начале
    ("skypro  ", "skypro  "),      # пробелы в конце не удаляются
    ("   ", ""),                    # только пробелы
    ("", ""),                        # пустая строка
])
def test_trim(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),          # символ есть в начале
    ("SkyPro", "o", True),          # символ есть в конце
    ("SkyPro", "P", True),          # символ есть в середине
    ("SkyPro", "U", False),         # символ отсутствует
    ("", "a", False),               # пустая строка
])
def test_contains(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),       # удаление символа
    ("SkyPro", "Pro", "Sky"),       # удаление подстроки в конце
    ("SkyPro", "s", "SkyPro"),      # символ отсутствует
    ("", "a", ""),                   # пустая строка
])
def test_delete_symbol(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected

    def test_capitalize_invalid_type():
        string_utils = StringUtils()
        # Проверка на ввод чисел и других типов данных
        with pytest.raises(AttributeError):  # Ожидаем, что метод не вызывается на нестроках
            string_utils.capitalize(123)

    def test_trim_invalid_type():
        string_utils = StringUtils()
        # Проверка на ввод нестроковых значений
        with pytest.raises(AttributeError):  # Метод работает только со строками
            string_utils.trim(123.456)

    def test_contains_empty_symbol():
        string_utils = StringUtils()
        # Проверка на пустой символ
        assert string_utils.contains("Some text", "") is False  # Ожидаем False, символ не найден

    def test_contains_invalid_type():
        string_utils = StringUtils()
        # Проверка на ввод нестроковых значений
        with pytest.raises(TypeError):  # Символ должен быть строкой
            string_utils.contains("Hello", 3)

    def test_delete_symbol_empty_string():
        string_utils = StringUtils()
        # Проверка на удаление символа из пустой строки
        assert string_utils.delete_symbol("", "a") == ""  # Ожидаем пустую строку

    def test_delete_symbol_invalid_char_type():
        string_utils = StringUtils()
        # Проверка на удаление символа, который не является строкой
        with pytest.raises(TypeError):  # Метод принимает только строковые символы
            string_utils.delete_symbol("Hello", 3)

    @pytest.mark.parametrize("input_str", [
        None,  # Проверка на None
        [],  # Проверка на список
        {},  # Проверка на словарь
    ])
    def test_methods_with_non_string(input_str):
        string_utils = StringUtils()
        with pytest.raises(TypeError):  # Ожидаем, что будет ошибка при передаче нестрок
            string_utils.capitalize(input_str)
        with pytest.raises(TypeError):
            string_utils.trim(input_str)
        with pytest.raises(TypeError):
            string_utils.contains(input_str, "a")
        with pytest.raises(TypeError):
            string_utils.delete_symbol(input_str, "a")
def test_capitalize_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод чисел и других типов данных
    with pytest.raises(AttributeError):  # Ожидаем, что метод не вызывается на нестроках
        string_utils.capitalize(123)

def test_trim_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод нестроковых значений
    with pytest.raises(AttributeError):  # Метод работает только со строками
        string_utils.trim(123.456)

def test_contains_empty_symbol():
    string_utils = StringUtils()
    # Проверка на пустой символ
    assert string_utils.contains("Some text", "") is False  # Ожидаем False, символ не найден

def test_contains_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод нестроковых значений
    with pytest.raises(TypeError):  # Символ должен быть строкой
        string_utils.contains("Hello", 3)

def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    # Проверка на удаление символа из пустой строки
    assert string_utils.delete_symbol("", "a") == ""  # Ожидаем пустую строку

def test_delete_symbol_invalid_char_type():
    string_utils = StringUtils()
    # Проверка на удаление символа, который не является строкой
    with pytest.raises(TypeError):  # Метод принимает только строковые символы
        string_utils.delete_symbol("Hello", 3)

@pytest.mark.parametrize("input_str", [
    None,  # Проверка на None
    [],    # Проверка на список
    {},    # Проверка на словарь
])
def test_methods_with_non_string(input_str):
    string_utils = StringUtils()
    with pytest.raises(TypeError):  # Ожидаем, что будет ошибка при передаче нестрок
        string_utils.capitalize(input_str)
    with pytest.raises(TypeError):
        string_utils.trim(input_str)
    with pytest.raises(TypeError):
        string_utils.contains(input_str, "a")
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, "a")

# Негативные тесты для класса StringUtils
def test_capitalize_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод чисел и других типов данных
    with pytest.raises(AttributeError):  # Ожидаем, что метод не вызывается на нестроках
        string_utils.capitalize(123)

def test_trim_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод нестроковых значений
    with pytest.raises(AttributeError):  # Метод работает только со строками
        string_utils.trim(123.456)

def test_contains_empty_symbol():
    string_utils = StringUtils()
    # Проверка на пустой символ
    assert string_utils.contains("Some text", "") is False  # Ожидаем False, символ не найден

def test_contains_invalid_type():
    string_utils = StringUtils()
    # Проверка на ввод нестроковых значений
    with pytest.raises(TypeError):  # Символ должен быть строкой
        string_utils.contains("Hello", 3)

def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    # Проверка на удаление символа из пустой строки
    assert string_utils.delete_symbol("", "a") == ""  # Ожидаем пустую строку

def test_delete_symbol_invalid_char_type():
    string_utils = StringUtils()
    # Проверка на удаление символа, который не является строкой
    with pytest.raises(TypeError):  # Метод принимает только строковые символы
        string_utils.delete_symbol("Hello", 3)

@pytest.mark.parametrize("input_str", [
    None,  # Проверка на None
    [],    # Проверка на список
    {},    # Проверка на словарь
])
def test_methods_with_non_string(input_str):
    string_utils = StringUtils()
    with pytest.raises(TypeError):  # Ожидаем, что будет ошибка при передаче нестрок
        string_utils.capitalize(input_str)
    with pytest.raises(TypeError):
        string_utils.trim(input_str)
    with pytest.raises(TypeError):
        string_utils.contains(input_str, "a")
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, "a")
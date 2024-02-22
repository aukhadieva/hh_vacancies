import os

from config import ROOT
from src.Saver import JSONSaver

file_path = os.path.join(ROOT, 'tests', 'data_for_test_2.json')
json_saver = JSONSaver(file_path)


def test_get_vacancy():
    """Проверка работы метода для получения данных из файла."""
    assert json_saver.get_vacancy(file_path) == {}


def test_add_vacancy():
    """Проверка работы метода для добавления вакансий в файл."""
    assert json_saver.add_vacancy({'items': [{'id': '93361633'}]}) is None


def test_delete_vacancy():
    """Проверка работы метода для удаления информации о вакансиях из файла."""
    assert json_saver.delete_vacancy(file_path) is None

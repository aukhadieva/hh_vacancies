import os

from config import ROOT
from src.Saver import JSONSaver

vacancy_path = os.path.join(ROOT, 'data', 'vacancy.json')
json_saver = JSONSaver(vacancy_path)


def test_add_vacancy():
    assert json_saver.add_vacancy({'items': [{'id': '93361633'}]}) is None


def test_delete_vacancy():
    assert json_saver.delete_vacancy(vacancy_path) is None

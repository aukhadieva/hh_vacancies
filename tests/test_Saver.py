from src.Saver import JSONSaver

json_saver = JSONSaver()


def test_add_vacancy():
    assert json_saver.add_vacancy({'items': [{'id': '93361633'}]}) is None


def test_delete_vacancy():
    assert json_saver.delete_vacancy('93361633') is None

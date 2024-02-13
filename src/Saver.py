import json
from abc import ABC, abstractmethod


class Saver(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, vacancy):
        pass


class JSONSaver(Saver):
    """Класс для сохранения информации о вакансиях в JSON-файл."""

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансий в файл."""
        with open('vacancy.json', 'w') as json_file:
            json.dump(vacancy, json_file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy):
        """Метод для удаления информации о вакансиях по id вакансии."""
        with open('vacancy.json') as json_file:
            data = json.load(json_file)
            if vacancy == data["items"][0]["id"]:
                del data["items"][0]
                with open('vacancy.json', 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

    def get_vacancy(self, vacancy):
        """Метод для получения данных из файла по указанным критериям."""
        pass

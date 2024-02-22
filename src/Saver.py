import json
import os
from abc import ABC, abstractmethod

from config import ROOT


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
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансий в файл."""
        with open(self.file_path, 'w') as json_file:
            json.dump(vacancy, json_file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy):
        """Метод для удаления информации о вакансиях по id вакансии."""
        with open(self.file_path) as json_file:
            data = json.load(json_file)
            data.clear()
            with open(self.file_path, 'w') as file:
                json.dump(data, file)

    def get_vacancy(self, vacancy):
        """Метод для получения данных из файла по указанным критериям."""
        with open(self.file_path) as json_file:
            loaded_vacancies = json.load(json_file)
            return loaded_vacancies

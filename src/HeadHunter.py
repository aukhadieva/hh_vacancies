from abc import ABC, abstractmethod

import requests


class HeadHunter(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def get_vacancies(self, vacancy_name):
        pass


class HeadHunterAPI(HeadHunter):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru."""

    def get_vacancies(self, vacancy_name):  # передается ключевое слово для поиска по вакансиям, н-р "Python"
        """Метод для подключения к API и получения вакансий."""
        # Получение вакансий с hh.ru в формате JSON
        params = {
            'text': f'NAME:{vacancy_name}',  # Текст фильтра. В имени должно быть слово, н-р, "Python"
            'area': 2,  # Поиск осуществляется по вакансиям города С-П
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы кириллица отображалась корректно
        return data


if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")
    print(hh_vacancies)

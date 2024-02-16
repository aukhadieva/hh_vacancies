import json


class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, vacancy_name: str, salary: str, currency: str, requirement: str, responsibility: str,
                 schedule: str, employer: str) -> None:
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.currency = currency
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.employer = employer

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        """Преобразование набора данных из JSON в список объектов."""
        vacancies_list = []
        for vacancy in hh_vacancies["items"]:
            vacancy_name = vacancy["name"]
            try:
                salary = vacancy["salary"]["from"]
            except TypeError:
                salary = None#'Нет данных'
            else:
                if vacancy["salary"]["to"] is None:
                    vacancy["salary"]["to"] = 'Нет данных'
                salary = f'{vacancy["salary"]["from"]}-{vacancy["salary"]["to"]}'
            try:
                currency = vacancy["salary"]["currency"]
            except TypeError:
                currency = 'Валюта не указана'
            requirement = vacancy["snippet"]["requirement"]
            responsibility = vacancy["snippet"]["responsibility"]
            schedule = vacancy["schedule"]["name"]
            try:
                employer = vacancy["employer"]["name"]
            except TypeError:
                employer = None
            vacancies_list.append(cls(vacancy_name, salary, currency, requirement, responsibility, schedule, employer))
        return vacancies_list

    def __repr__(self):
        """
        Возвращает текстовое представление объекта полезное для отладки
        в виде названия классов и его атрибутов.
        """
        return (f'{self.__class__.__name__} ({self.vacancy_name}, {self.employer}, {self.salary}, {self.currency},'
                f'{self.requirement}, {self.responsibility}, {self.schedule})')

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return (f'Вакансия: {self.vacancy_name}\nКомпания: {self.employer}\n'
                f'Заработная плата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\nОбязанности: {self.responsibility}\nГрафик: {self.schedule}\n')

    @classmethod
    def filter_vacancies(self, vacancies_list, filter_words) -> list:
        """Метод для поиска вакансий по названию вакансии."""
        filtered_vacancies = []
        for item in vacancies_list:
            if filter_words in item.vacancy_name:
                filtered_vacancies.append(item)
        return filtered_vacancies

    @classmethod
    def sort_vacancies(cls, filtered_vacancies) -> list:
        """Метод для сравнения вакансий между собой по зарплате."""
        ranged_vacancies = []
        for item in filtered_vacancies:
            if item.salary is None:
                item.salary = 'Зарплата не указана'
            ranged_vacancies.append(item)
        return ranged_vacancies

    @classmethod
    def get_vacancies_by_salary(cls, ranged_vacancies, salary_range) -> list:
        """Метод для поиска вакансий по зарплате в файле."""
        filtered_by_salary= []
        for item in ranged_vacancies:
            try:
                if salary_range in item.salary:
                    filtered_by_salary.append(item)
            except TypeError:
                pass
        return filtered_by_salary

    @classmethod
    def get_top_vacancies(cls, sorted_vacancies, top_n) -> list:
        """Метод для вывода топа вакансий."""
        return sorted_vacancies[:top_n]

    @classmethod
    def print_vacancies(cls, top_vacancies) -> None:
        """Выводит отобранную вакансию/ -и пользователю."""
        for vacancy in top_vacancies:
            print(vacancy)

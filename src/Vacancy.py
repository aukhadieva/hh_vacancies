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
        vacancies_list_ = []
        for vacancy in hh_vacancies["items"]:
            vacancy_name = vacancy["name"]
            try:
                salary = vacancy["salary"]["from"]
            except TypeError:
                salary = None
            else:
                salary = f'{vacancy["salary"]["from"]}-{vacancy["salary"]["to"]}'
            try:
                currency = vacancy["salary"]["currency"]
            except TypeError:
                currency = None
            requirement = vacancy["snippet"]["requirement"]
            responsibility = vacancy["snippet"]["responsibility"]
            schedule = vacancy["schedule"]["name"]
            try:
                employer = vacancy["employer"]["name"]
            except TypeError:
                employer = None
            vacancies_list_.append(cls(vacancy_name, salary, currency, requirement, responsibility, schedule, employer))
        return vacancies_list_

    def __repr__(self):
        return (f'Вакансия: {self.vacancy_name}\nКомпания: {self.employer}\n'
                f'Заработная плата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\nОбязанности: {self.responsibility}\nГрафик: {self.schedule}\n')

    def filter_vacancies(self, vacancies_list, filter_words):
        """Метод для поиска вакансий по ключевому слову в файле."""
        pass

    def get_vacancies_by_salary(cls, filtered_vacancies, salary_range):
        """Метод для поиска вакансий по зарплате в файле."""
        pass

    def sort_vacancies(self, ranged_vacancies):
        """Метод для сравнения вакансий между собой по зарплате."""
        pass

    def get_top_vacancies(self, sorted_vacancies, top_n):
        """Метод для вывода топа вакансий."""
        pass

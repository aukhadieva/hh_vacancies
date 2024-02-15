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
            vacancies_list.append(cls(vacancy_name, salary, currency, requirement, responsibility, schedule, employer))
        return vacancies_list

    def __repr__(self):
        """Используется для отладки информации об атрибутах класса Vacancy."""
        return (f'Вакансия: {self.vacancy_name}\nКомпания: {self.employer}\n'
                f'Заработная плата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\nОбязанности: {self.responsibility}\nГрафик: {self.schedule}\n')

    @classmethod
    def filter_vacancies(self, vacancies_list, filter_words):
        """Метод для поиска вакансий по названию вакансии."""
        filtered_vacancies = []
        for item in vacancies_list:
            if filter_words in item.vacancy_name:
                filtered_vacancies.append(item)
        return filtered_vacancies

    @classmethod
    def get_vacancies_by_salary(cls, filtered_vacancies, salary_range):
        """Метод для поиска вакансий по зарплате."""
        filtered_by_salary = []
        for item in filtered_vacancies:
            if salary_range == item.salary:
                filtered_by_salary.append(item)
        return filtered_by_salary

    def sort_vacancies(self, ranged_vacancies):
        """Метод для сравнения вакансий между собой по зарплате."""
        pass

    def get_top_vacancies(self, sorted_vacancies, top_n):
        """Метод для вывода топа вакансий."""
        pass

    @classmethod
    def print_vacancies(self, top_vacancies):
        """Выводит отобранную вакансию/ -и пользователю."""
        for vacancy in top_vacancies:
            print(vacancy)

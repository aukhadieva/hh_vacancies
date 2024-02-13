import json


class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, vacancy_name: str, employer: str, salary: int, requirement: str, responsibility: str, schedule: str) -> None:
        self.vacancy_name = vacancy_name
        self.employer = employer
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        """Преобразование набора данных из JSON в список объектов."""
        vacancy_name = hh_vacancies["items"][0]["name"]
        try:
            salary = hh_vacancies["items"][0]["salary"]["from"]
        except TypeError:
            salary = None
        else:
            salary = f'{hh_vacancies["items"][0]["salary"]["from"]} - {hh_vacancies["items"][0]["salary"]["to"]}'
        requirement = hh_vacancies["items"][0]["snippet"]["requirement"]
        responsibility = hh_vacancies["items"][0]["snippet"]["responsibility"]
        schedule = hh_vacancies["items"][0]["schedule"]["name"]
        try:
            employer = hh_vacancies["items"][0]["employer"]["name"]
        except TypeError:
            employer = None
        return cls(vacancy_name, salary, requirement, responsibility, schedule, employer)

    def __repr__(self):
        """Магический метод __repr__ для отладки информации о классе Vacancy."""
        return (f'{self.__class__.__name__}({self.vacancy_name}, {self.employer}, {self.salary}, '
                f'{self.requirement}, {self.responsibility}, {self.schedule})')

    def filter_vacancies(self, vacancies_list, filter_words):
        """Метод для поиска вакансий по ключевому слову в файле."""
        pass

    def get_vacancies_by_salary(self, filtered_vacancies,
                                salary_range):  # self.filter_words = filter_words  # input("Введите ключевые слова для фильтрации вакансий: ").split()
        """Метод для поиска вакансий по зарплате в файле."""
        pass

    def sort_vacancies(self,
                       ranged_vacancies):  # self.salary_range = salary_range  # input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
        """Метод для сравнения вакансий между собой по зарплате."""
        pass

    def get_top_vacancies(self, sorted_vacancies,
                          top_n):  # self.top_n = top_n  # int(input("Введите количество вакансий для вывода в топ N: "))
        """Метод для вывода топа вакансий."""
        pass

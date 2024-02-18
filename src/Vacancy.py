import json


class Vacancy:
    """Класс для работы с вакансиями."""

    vacancies_list = []

    def __init__(self, vacancy_name: str, salary: str, currency: str, requirement: str, responsibility: str,
                 schedule: str, employer: str) -> None:
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.currency = currency
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.employer = employer
        Vacancy.vacancies_list.append(self)

    @classmethod
    def cast_to_object_list(cls, hh_vacancies) -> None:
        """Преобразование набора данных из JSON в список объектов."""
        with open(hh_vacancies) as json_file:
            vacancy_data = json.load(json_file)
            for vacancy in vacancy_data['items']:
                vacancy_name = vacancy['name']
                try:
                    if vacancy["salary"]["from"] is None:
                        vacancy["salary"]["from"] = 'Нет данных'
                    if vacancy["salary"]["to"] is None:
                        vacancy["salary"]["to"] = 'Нет данных'
                    salary = f'{vacancy["salary"]["from"]}-{vacancy["salary"]["to"]}'
                except TypeError:
                    salary = None
                try:
                    currency = vacancy["salary"]["currency"]
                except TypeError:
                    currency = 'Валюта не указана'
                requirement = vacancy["snippet"]["requirement"]
                responsibility = vacancy["snippet"]["responsibility"]
                schedule = vacancy["schedule"]["name"]
                employer = vacancy["employer"]["name"]
                cls(vacancy_name, salary, currency, requirement, responsibility, schedule, employer)

    def __repr__(self):
        """
        Возвращает текстовое представление объекта полезное для отладки
        в виде названия классов и его атрибутов.
        """
        return (f'{self.__class__.__name__} ({self.vacancy_name}, {self.employer}, {self.salary},'
                f'{self.requirement}, {self.responsibility}, {self.schedule})')

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return (f'Вакансия: {self.vacancy_name}\nКомпания: {self.employer}\n'
                f'Заработная плата: {self.salary}\n'
                f'Требования: {self.requirement}\nОбязанности: {self.responsibility}\nГрафик: {self.schedule}\n')

    @classmethod
    def sort_vacancies(cls, vacancies) -> list:
        """Метод для сравнения вакансий между собой."""
        ranged_vacancies = []
        for item in vacancies:
            if item.salary is None:
                item.salary = 'Зарплата не указана'
            try:
                item.requirement = item.requirement.replace('<highlighttext>Python</highlighttext>',
                                                            'Python')
            except AttributeError:
                if item.requirement is None:
                    item.requirement = 'Информация не указана'
            try:
                item.responsibility = item.responsibility.replace('<highlighttext>Python</highlighttext>',
                                                                  'Python')
            except AttributeError:
                if item.responsibility is None:
                    item.responsibility = 'Информация не указана'
            ranged_vacancies.append(item)
        return ranged_vacancies

    @classmethod
    def get_vacancies_by_salary(cls, ranged_vacancies, salary_range) -> list:
        """Метод для поиска вакансий по зарплате в файле."""
        filtered_by_salary = []
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
        try:
            return sorted_vacancies[:int(top_n)]
        except ValueError:
            if top_n == '':
                return sorted_vacancies

    @classmethod
    def print_vacancies(cls, top_vacancies) -> None:
        """Выводит отобранную вакансию/ -и пользователю."""
        for vacancy in top_vacancies:
            print(vacancy)

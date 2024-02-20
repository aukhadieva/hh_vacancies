import json


class Vacancies:
    """Класс для вакансий."""

    def __init__(self, hh_vacancies) -> None:
        self.__hh_vacancies = hh_vacancies

    @property
    def hh_vacancies(self) -> str:
        """Геттер для приватного атрибута __hh_vacancies."""
        return self.__hh_vacancies

    def load_vacancies(self) -> dict:
        """Загружает вакансии из json-словаря. Возвращает словарь."""
        with open(self.hh_vacancies) as json_file:
            loaded_vacancies = json.load(json_file)
            return loaded_vacancies

    def sort_salary(self, loaded_vacancies, salary_range) -> list:
        """Сравнивает вакансии из json-словаря по зарплате. Возвращает отфильтрованный список."""
        ranked_by_salary = []
        for item in loaded_vacancies['items']:
            try:
                if item['salary'] is None:
                    item['salary'] = 'Нет данных'
                if item['salary']['from'] is None:
                    item['salary']['from'] = 'Нет данных'
                if item['salary']['to'] is None:
                    item['salary']['to'] = 'Нет данных'
                if (salary_range == str(item['salary']['from']) or salary_range == str(item['salary']['to'])
                        or salary_range == f'{item["salary"]["from"]}-{item["salary"]["to"]}'):
                    ranked_by_salary.append(item)
            except TypeError:
                pass
            if salary_range == '':
                ranked_by_salary.append(item)
        return ranked_by_salary

    @staticmethod
    def sort_currency(ranked_by_salary) -> list:
        """Сортирует вакансии по валюте. Возвращает отсортированный список."""
        ranked_by_currency = []
        for item in ranked_by_salary:
            try:
                if item['salary']['currency'] == "RUR":
                    item['salary']['currency'] = "руб."
                    ranked_by_currency.append(item)
            except TypeError:
                pass
            if item['salary'] == 'Нет данных':
                ranked_by_currency.append(item)
        return ranked_by_currency

    @staticmethod
    def sort_req_res(ranked_by_currency) -> list:
        """Сортирует вакансии по требованиям и обязанностям. Возвращает отсортированный список."""
        ranked_by_other = []
        for item in ranked_by_currency:
            try:
                item["snippet"]["requirement"] = item["snippet"]["requirement"].replace(
                    '<highlighttext>Python</highlighttext>',
                    'Python')
            except AttributeError:
                if item["snippet"]["requirement"] is None:
                    item["snippet"]["requirement"] = 'Информация не указана'
            try:
                item["snippet"]["responsibility"] = item["snippet"]["responsibility"].replace(
                    '<highlighttext>Python</highlighttext>',
                    'Python')
            except AttributeError:
                if item["snippet"]["responsibility"] is None:
                    item["snippet"]["responsibility"] = 'Информация не указана'
            ranked_by_other.append(item)
        return ranked_by_other

    def sort_area(self, ranked_by_other, area) -> list:
        """Сравнивает вакансии по городу. Возвращает отфильтрованный список."""
        ranked_by_area = []
        for item in ranked_by_other:
            if area == item['area']['name']:
                ranked_by_area.append(item)
            elif area == '':
                ranked_by_area.append(item)
        return ranked_by_area


class Vacancy:
    """Класс для вакансии."""

    vacancies_list = []

    def __init__(self, vacancy_name: str, area: str, employer: str, salary: str, currency: str,
                 requirement: str, responsibility: str, schedule: str):
        self.vacancy_name = vacancy_name
        self.area = area
        self.employer = employer
        self.salary = salary
        self.currency = currency
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule

        Vacancy.vacancies_list.append(self)

    @classmethod
    def cast_to_object_list(cls, vacancies) -> None:
        """Преобразует набор данных из отфильтрованного списка в список объектов."""
        for vacancy in vacancies:
            vacancy_name = vacancy['name']
            area = vacancy['area']['name']
            employer = vacancy["employer"]["name"]
            try:
                salary = f'{vacancy["salary"]["from"]}-{vacancy["salary"]["to"]}'
            except TypeError:
                salary = vacancy["salary"]
            try:
                currency = vacancy["salary"]["currency"]
            except TypeError:
                currency = 'Валюта не указана'
            requirement = vacancy["snippet"]["requirement"]
            responsibility = vacancy["snippet"]["responsibility"]
            schedule = vacancy["schedule"]["name"]
            cls(vacancy_name, area, employer, salary, currency, requirement, responsibility, schedule)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return (f'Вакансия: {self.vacancy_name}\nГород: {self.area}\nКомпания: {self.employer}\n'
                f'Заработная плата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\nОбязанности: {self.responsibility}\nГрафик: {self.schedule}\n')

    @classmethod
    def print_vacancies(cls, vacancies_list) -> None:
        """Выводит отобранные вакансии пользователю."""
        for vacancy in vacancies_list:
            print(vacancy)

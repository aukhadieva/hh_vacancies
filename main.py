import os

from config import ROOT
from src.HeadHunter import HeadHunterAPI
from src.Saver import JSONSaver
from src.Vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies(input(f"Введите ключевые слова для фильтрации вакансий: \n"))

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(hh_vacancies)

# Преобразование набора данных из JSON в список объектов
vacancy_path = os.path.join(ROOT, 'data', 'vacancy.json')
Vacancy.cast_to_object_list(vacancy_path)
vacancies = Vacancy.vacancies_list  # все вакансии в виде списка экземпляров


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    salary_range = input(f"Введите диапазон зарплат или нажмите enter, чтобы увидеть все вакансии: \n")
    top_n = input(f"Введите количество вакансий для вывода в топ N или нажмите enter, чтобы увидеть все вакансии: \n")

    sorted_vacancies = Vacancy.sort_vacancies(vacancies)
    filtered_by_salary = Vacancy.get_vacancies_by_salary(sorted_vacancies, salary_range)
    top_vacancies = Vacancy.get_top_vacancies(filtered_by_salary, top_n)
    Vacancy.print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()

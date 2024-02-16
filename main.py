from src.HeadHunter import HeadHunterAPI
from src.Saver import JSONSaver
from src.Vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies(input("Введите поисковый запрос: "))

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(hh_vacancies)
#json_saver.delete_vacancy(hh_vacancies)


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")#.split()
    salary_range = input("Введите диапазон зарплат: ")
    top_n = int(input(f"Введите количество вакансий для вывода в топ N: "))

    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    sorted_vacancies = Vacancy.sort_vacancies(filtered_vacancies)
    filtered_by_salary = Vacancy.get_vacancies_by_salary(sorted_vacancies, salary_range)
    top_vacancies = Vacancy.get_top_vacancies(filtered_by_salary, top_n)
    Vacancy.print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()

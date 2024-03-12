from config import vacancy_path
from src.HeadHunter import HeadHunterAPI
from src.Saver import JSONSaver
from src.Vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем."""
    global ranked_by_other

    hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_vacancies = hh_api.get_vacancies(input(f"Введите ключевые слова для фильтрации вакансий: \n"))

    json_saver = JSONSaver(vacancy_path)
    json_saver.add_vacancy(hh_vacancies)  # Сохранение информации о вакансиях в файл

    loaded_vacancies = json_saver.get_vacancy(vacancy_path)

    while True:
        salary_range = input(f"Введите зарплату или диапазон зарплат или enter, чтобы увидеть все варианты: \n")
        ranked_by_salary = Vacancy.sort_salary(loaded_vacancies, salary_range)
        if len(ranked_by_salary) == 0:
            print('Вакансия не найдена. Попробуйте еще раз.')
            continue

        ranked_by_currency = Vacancy.sort_currency(ranked_by_salary)
        ranked_by_other = Vacancy.sort_req_res(ranked_by_currency)
        break

    while True:
        area = input(f"Введите город или enter, чтобы увидеть все варианты: \n").title()
        ranked_by_area = Vacancy.sort_area(ranked_by_other, area)
        if len(ranked_by_area) == 0:
            print('Вакансия не найдена. Попробуйте еще раз.')
            continue

        top_range = input(f"Введите число вакансий, которые хотите просмотреть или enter, "
                             f"чтобы увидеть все варианты: \n")
        ranked_by_top = Vacancy.get_top_vacancies(ranked_by_area, top_range)

        Vacancy.cast_to_object_list(ranked_by_top)  # инициализирую
        vacancies = Vacancy.vacancies_list  # отобранные вакансии в виде списка экземпляров

        Vacancy.print_vacancies(vacancies)  # печатаю отобранные вакансии
        break

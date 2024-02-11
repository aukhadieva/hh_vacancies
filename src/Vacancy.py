class Vacancy:
    """Класс для работы с вакансиями."""
    def __init__(self, top_n: int, filter_words: str, salary_range: str, schedule: str) -> None:
        #self.search_query = search_query  # input("Введите поисковый запрос: ")
        self.top_n = top_n  # int(input("Введите количество вакансий для вывода в топ N: "))
        self.filter_words = filter_words  # input("Введите ключевые слова для фильтрации вакансий: ").split()
        self.salary_range = salary_range  # input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
        self.schedule = schedule  # input("Введите тип занятости: ") # Гибкий график / Полный день / Удаленная работа

    @classmethod
    def cast_to_object_list(self):
        """Преобразование набора данных из JSON в список объектов."""
        pass

    def filter_vacancies(self, vacancies_list, filter_words):
        """Метод для поиска вакансий по ключевому слову в файле."""
        pass

    def get_vacancies_by_salary(self, filtered_vacancies, salary_range):
        """Метод для поиска вакансий по зарплате в файле."""
        pass

    def sort_vacancies(self, ranged_vacancies):
        """Метод для сравнения вакансий между собой по зарплате."""
        pass

    def get_top_vacancies(self, sorted_vacancies, top_n):
        """Метод для вывода топа вакансий."""
        pass

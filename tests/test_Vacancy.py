import os

import pytest

from config import ROOT
from src.Vacancy import Vacancies, Vacancy


@pytest.fixture
def item_for_test_Vacancies():
    vacancy_path = os.path.join(ROOT, 'tests', 'data_for_test.json')
    return Vacancies(vacancy_path)


def test_getter(item_for_test_Vacancies):
    """Проверка работы геттера."""
    assert item_for_test_Vacancies.hh_vacancies == '/Users/dns/PycharmProjects/hh_vacancies/tests/data_for_test.json'


def test_loaded_vacancies(item_for_test_Vacancies):
    """Проверка работы метода load_vacancies."""
    assert item_for_test_Vacancies.load_vacancies() == {'items': [
        {'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 50000, 'to': None, 'currency': 'RUR', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-02-19T14:27:33+0300', 'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/93469153',
         'relations': [], 'employer': {'id': '3530', 'name': 'СДЭК', 'url': 'https://api.hh.ru/employers/3530',
                                       'alternate_url': 'https://hh.ru/employer/3530',
                                       'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                                     '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                                     'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Уверенное владение MS Excel, MS Word. Знание <highlighttext>Python</highlighttext> (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
            'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
         'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]}


def test_sort_salary(item_for_test_Vacancies):
    """Проверка работы метода sort_salary."""
    assert item_for_test_Vacancies.sort_salary(item_for_test_Vacancies.load_vacancies(), '50000') == [
        {'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 50000, 'to': 'Нет данных', 'currency': 'RUR', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-02-19T14:27:33+0300', 'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/93469153',
         'relations': [], 'employer': {'id': '3530', 'name': 'СДЭК', 'url': 'https://api.hh.ru/employers/3530',
                                       'alternate_url': 'https://hh.ru/employer/3530',
                                       'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                                     '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                                     'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Уверенное владение MS Excel, MS Word. Знание <highlighttext>Python</highlighttext> (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
            'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
         'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]


def test_sort_currency(item_for_test_Vacancies):
    """Проверка работы метода sort_currency."""
    assert item_for_test_Vacancies.sort_currency(
        item_for_test_Vacancies.sort_salary(item_for_test_Vacancies.load_vacancies(), '50000')) == [
               {'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)', 'department': None,
                'has_test': False, 'response_letter_required': False,
                'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                'salary': {'from': 50000, 'to': 'Нет данных', 'currency': 'руб.', 'gross': False},
                'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
                'sort_point_distance': None,
                'published_at': '2024-02-19T14:27:33+0300', 'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
                'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
                'show_logo_in_search': None, 'insider_interview': None,
                'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru',
                'alternate_url': 'https://hh.ru/vacancy/93469153',
                'relations': [], 'employer': {'id': '3530', 'name': 'СДЭК', 'url': 'https://api.hh.ru/employers/3530',
                                              'alternate_url': 'https://hh.ru/employer/3530',
                                              'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                                            '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                                            'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                                              'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                                              'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                   'requirement': 'Уверенное владение MS Excel, MS Word. Знание <highlighttext>Python</highlighttext> (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
                   'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
                'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
                'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                'accept_incomplete_resumes': False,
                'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                'is_adv_vacancy': False,
                'adv_context': None}]


def test_sort_req_res(item_for_test_Vacancies):
    """Проверка работы метода sort_req_res."""
    assert item_for_test_Vacancies.sort_req_res(
        item_for_test_Vacancies.sort_currency(
            item_for_test_Vacancies.sort_salary(item_for_test_Vacancies.load_vacancies(), '50000'))) == [
               {'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)', 'department': None,
                'has_test': False, 'response_letter_required': False,
                'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                'salary': {'from': 50000, 'to': 'Нет данных', 'currency': 'руб.', 'gross': False},
                'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
                'sort_point_distance': None, 'published_at': '2024-02-19T14:27:33+0300',
                'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
                'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
                'show_logo_in_search': None, 'insider_interview': None,
                'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru',
                'alternate_url': 'https://hh.ru/vacancy/93469153', 'relations': [],
                'employer': {'id': '3530', 'name': 'СДЭК', 'url': 'https://api.hh.ru/employers/3530',
                             'alternate_url': 'https://hh.ru/employer/3530',
                             'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                           '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                           'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                             'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                             'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                   'requirement': 'Уверенное владение MS Excel, MS Word. Знание Python (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
                   'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
                'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
                'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                'is_adv_vacancy': False, 'adv_context': None}]


def test_sort_area(item_for_test_Vacancies):
    """Проверка работы метода sort_area."""
    assert item_for_test_Vacancies.sort_area(item_for_test_Vacancies.sort_req_res(
        item_for_test_Vacancies.sort_currency(
            item_for_test_Vacancies.sort_salary(item_for_test_Vacancies.load_vacancies(), '50000'))), 'Москва') == [
               {'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)', 'department': None,
                'has_test': False, 'response_letter_required': False,
                'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                'salary': {'from': 50000, 'to': 'Нет данных', 'currency': 'руб.', 'gross': False},
                'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
                'sort_point_distance': None, 'published_at': '2024-02-19T14:27:33+0300',
                'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
                'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
                'show_logo_in_search': None, 'insider_interview': None,
                'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru',
                'alternate_url': 'https://hh.ru/vacancy/93469153', 'relations': [],
                'employer': {'id': '3530', 'name': 'СДЭК', 'url': 'https://api.hh.ru/employers/3530',
                             'alternate_url': 'https://hh.ru/employer/3530',
                             'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                           '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                           'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                             'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                             'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                   'requirement': 'Уверенное владение MS Excel, MS Word. Знание Python (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
                   'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
                'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
                'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                'is_adv_vacancy': False, 'adv_context': None}]

def test_cast_to_object_list():
    assert Vacancy.cast_to_object_list([{'id': '93469153', 'premium': False, 'name': 'Junior Разработчик (удаленно)',
                                         'department': None, 'has_test': False, 'response_letter_required': False,
                                         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                                         'salary': {'from': 50000, 'to': 'Нет данных', 'currency': 'руб.',
                                                    'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'},
                                         'address': None, 'response_url': None, 'sort_point_distance': None,
                                         'published_at': '2024-02-19T14:27:33+0300',
                                         'created_at': '2024-02-19T14:27:33+0300', 'archived': False,
                                         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93469153',
                                         'show_logo_in_search': None, 'insider_interview': None,
                                         'url': 'https://api.hh.ru/vacancies/93469153?host=hh.ru',
                                         'alternate_url': 'https://hh.ru/vacancy/93469153', 'relations': [],
                                         'employer': {'id': '3530', 'name': 'СДЭК',
                                                      'url': 'https://api.hh.ru/employers/3530',
                                                      'alternate_url': 'https://hh.ru/employer/3530',
                                                      'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5393076.png',
                                                                    '240': 'https://hhcdn.ru/employer-logo/5393077.png',
                                                                    'original': 'https://hhcdn.ru/employer-logo-original/964764.png'},
                                                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3530',
                                                      'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Уверенное владение MS Excel, MS Word. Знание Python (Selenium, BeautifulSoup), VBA, PowerShell. Понимание методологий разработки ПО. Базовые знания SQL, опыт...',
            'responsibility': 'Разработка и внедрение программных решений для повышения производительности и оптимизации бизнес-процессов. Тестирование, отладка и поддержка разработанных решений. '},
                                         'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
                                         'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
                                         'accept_temporary': False,
                                         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                                         'accept_incomplete_resumes': False,
                                         'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                                         'employment': {'id': 'full', 'name': 'Полная занятость'},
                                         'adv_response_url': None, 'is_adv_vacancy': False,
                                         'adv_context': None}]) is None


def test_print_vacancies():
    vacancies = Vacancy.vacancies_list
    assert Vacancy.print_vacancies(vacancies) is None

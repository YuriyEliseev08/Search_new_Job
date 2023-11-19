from src.saves import JsonSave, add_vacancy
from src.api_class import HH_API, SJ_API
from src.vacancies import Vacancy


def user_interaction():
    """Функция для вывода в main"""
    print()
    print('Если не указать ключевых слов, то выведутся все возможные вакансии без фильтрации.')
    keyword = input('Введите ключевые слова для фильтрации вакансий: ')
    print()
    print(" '1' - hh.ru\n '2' - superjob.ru\n '3' - на обоих платформах\n")
    set_platform = input('Выберите платформу для поиска вакансий: ')
    print()
    print('если не указать количество вакансий в ТОПЕ, будет выведено первых 20 вакансий.')

    try:
        num_of_vacancy_top = int(input('Укажите количество выводимых вакансий ТОП: '))
    except ValueError:
        num_of_vacancy_top = 20  # Устанавливаем значение по умолчанию в 20

    hh = HH_API(keyword)
    hh_vacancies = hh.format_vacancies(hh.get_vacancies())

    sj = SJ_API(keyword)
    sj_vacancies = sj.format_vacancies(sj.get_vacancies())

    if set_platform == '1':
        print('Ваш выбор искать на hh.ru')
        JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies']
    elif set_platform == '2':
        print('Ваш выбор искать на superjob.ru')
        JsonSave.all_vacancies['vacancies'] = sj_vacancies['vacancies']
    elif set_platform == '3':
        print('Ваш выбор искать везде')
        JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']
    else:
        print('Ваш выбор не опознан, ищем везде.')
        JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']
    print()
    add_vacancy()
    Vacancy.compare_vacancies_by_salary()
    vac = Vacancy.print_vacancies(num_of_vacancy_top)
    print(vac)
    Vacancy.print_vacancies(num_of_vacancy_top)
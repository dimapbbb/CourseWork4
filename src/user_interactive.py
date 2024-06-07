from src.load_vacancies import HH
from src.vacancy import Vacancy
from src.file_worker import FileWorkPickle, FileWorkJson


class UserInteractive(FileWorkPickle, FileWorkJson):
    """
    Класс для общения с пользователем
    """
    name: str

    def __init__(self, name):
        self.name = name
        self.say_hello()          # Приветсвенное сообщение
        self.vacancies_list = []
        self.tech_message = ''    # тех сообщение после выполнения команды

    def filter_by_keywords(self):
        """
        Фильтр по ключевым словам
        """
        keywords = input('Введите ключевые слова через пробел: ').split()
        filter_vacancies = []
        for word in keywords:
            for vacancy in self.vacancies_list:
                if vacancy.name.find(word.lower()) != -1 or vacancy.name.find(word.title()) != -1:
                    filter_vacancies.append(vacancy)

        if len(filter_vacancies) == 0:
            self.tech_message = "Запрос не дал результатов, попоробуй другой"
        else:
            self.vacancies_list = list(set(filter_vacancies))
            self.tech_message = f'Отсортировано по ключевым словам: {','.join(keywords)}'

    def sort_by_date(self):
        """
        сортировать по дате публикации, сначала самые свежие
        """
        self.vacancies_list = sorted(self.vacancies_list, key=lambda x: x.published_at)
        self.tech_message = 'Отсортировано по дате'

    def filter_by_min_salary(self):
        """
        Отфильтровать по минимальной зарплате
        """
        try:
            min_salary = int(input("Сколько минимум хочешь зарабатывать? : "))
        except ValueError:
            self.tech_message = 'Нужно ввести число'
        filter_vacancies = list(filter(lambda x: x.salary >= min_salary, self.vacancies_list))

        if len(filter_vacancies) == 0:
            self.tech_message = "Губа не треснет??? Введи меньше"
        else:
            self.tech_message = 'Отфильтровано'
            self.vacancies_list = filter_vacancies

    def sort_by_salary(self):
        """
        Сортировать по убыванию зарплаты
        """
        self.vacancies_list = sorted(self.vacancies_list, key=lambda x: x.salary)
        self.tech_message = 'Сортировано по зарплате'

    def filter_by_area(self):
        """
        Отфильтровать по городу
        """
        area = input('Введи город: ')
        filter_vacancies = list(filter(lambda x: x.area == area.title(), self.vacancies_list))
        if len(filter_vacancies) == 0:
            self.tech_message = "В этом городе нет данной ваансии"
        else:
            self.tech_message = 'Отфильтровано по городу'
            self.vacancies_list = filter_vacancies

    def print_vacancies_list(self):
        """
        Вывести на экран
        """
        for vacancy in self.vacancies_list:
            print(vacancy)

    def get_vacancies_list(self):
        """
        Получение списка вакансий по ключевому слову
        """
        query = input("Какую должность ищем? : ")
        print("Собираю информацию....")
        get_api = HH(query)
        get_api.load_vacancies()
        self.vacancies_list = [Vacancy.new_vacancy(vacancy) for vacancy in get_api.vacancies]

    @staticmethod
    def say_hello():
        """
        Приветсвенне сообщение
        """
        print("Приветсвую тебя соискатель, сейчас найдем тебе работу")

    @staticmethod
    def print_commands():
        print("1 - Отфильтровать по городу\n"
              "2 - Сортировать по убыванию зарплаты\n"
              "3 - Отфильтровать по минимальной зарплате\n"
              "4 - сортировать по дате публикации, сначала самые свежие\n"
              "5 - Фильтровать по ключевым словам\n"
              "6 - Сохранить в избранное\n"
              "7 - Посмотреть избранное\n"
              "8 - Очистить избранное\n"
              "9 - Новый запрос\n"
              "0 - Завершить поиск\n")

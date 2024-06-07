class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name, area, salary, experience, responsibility, employment, published_at, url):
        self.name = self.validation_data(name)                        # имя
        self.area = self.validation_data(area)                        # город
        self.salary = self.validation_salary(salary)                  # зарплата
        self.experience = self.validation_data(experience)            # опыт работы
        self.responsibility = self.validation_data(responsibility)    # обязаности
        self.employment = self.validation_data(employment)            # занятость
        self.published_at = self.validation_data(published_at)        # дата публикации
        self.url = self.validation_data(url)                          # ссылка

    def __str__(self):
        return (f"Описание: {self.name}, {self.salary if self.salary else 'Зарплата не указана'}, "
                f"{self.area}, {self.employment}\n"
                f"Требования: {self.experience}\n"
                f"Обязанности: {self.responsibility}\n"
                f"Дата публикации: {self.get_date()}\n"
                f"Ссылка: {self.url}\n")

    def __lt__(self, other):
        if not self.salary:
            return 'Не указана зарплата у первой вакансии'
        elif not other.salary:
            return 'Не указана зарплата у второй вакансии'
        elif self.salary > other.salary:
            return False
        else:
            return True

    def __getstate__(self):
        state = {'name': self.name,
                 'area': self.area,
                 'salary': self.salary,
                 'experience': self.experience,
                 'responsibility': self.responsibility,
                 'employment': self.employment,
                 'published_at': self.published_at,
                 'url': self.url}
        return state

    def __setstate__(self, state):
        self.name = state['name']
        self.area = state['area']
        self.salary = state['salary']
        self.experience = state['experience']
        self.responsibility = state['responsibility']
        self.employment = state['employment']
        self.published_at = state['published_at']
        self.url = state['url']

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get('name')                                     # имя
        area = vacancy.get('area').get('name')                         # город
        salary = vacancy.get('salary')                                 # зарплата
        experience = vacancy.get('snippet').get('requirement')         # опыт работы
        responsibility = vacancy.get('snippet').get('responsibility')  # обязаности
        employment = vacancy.get('employment').get('name')             # занятость
        published_at = vacancy.get('published_at')                     # дата публикации
        url = vacancy.get('alternate_url')                             # ссылка

        return cls(name, area, salary, experience, responsibility, employment, published_at, url)

    @staticmethod
    def validation_salary(data):
        if data:
            if data['from']:
                return data['from']
            elif not data['from'] and data['to']:
                return data['to']
            else:
                return 0
        else:
            return 0

    @staticmethod
    def validation_data(data):
        if data:
            return data
        else:
            return 'Отсутсвует'

    def get_date(self):
        return f'{self.published_at[8:10]}.{self.published_at[5:7]}.{self.published_at[:4]}'

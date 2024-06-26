import json
import os
import pickle
from abc import ABC, abstractmethod


class FileWork(ABC):
    """
    Абстракный класс коннектор
    """
    @abstractmethod
    def save_query(self, data):
        pass

    @abstractmethod
    def read_query(self):
        pass

    @abstractmethod
    def delete_query(self):
        pass


class FileWorkPickle(FileWork):
    """
    Работа с форматом bin
    """
    __path = os.path.abspath('data/favorite_vacancies')

    def save_query(self, data: list):
        with open(self.__path, 'ab') as file:
            pickle.dump(data, file)

    def read_query(self):
        with open(self.__path, 'rb') as file:
            data = pickle.load(file)
        return data

    def delete_query(self):
        try:
            os.remove(self.__path)
        except FileNotFoundError:
            print('Файл избранных пуст')


class FileWorkJson(FileWork):
    """
    Работа с форматом json
    """
    __path = os.path.abspath('data/vacancies.json')

    def save_query(self, data):
        with open(self.__path, 'aw', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read_query(self):
        with open(self.__path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        return data

    def delete_query(self):
        try:
            os.remove(self.__path)
        except FileNotFoundError:
            print('Файл избранных пуст')

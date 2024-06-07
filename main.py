from src.user_interactive import UserInteractive


def main():
    name = input('Как зовут? : ')
    user = UserInteractive(name)
    user.get_vacancies_list()
    user.print_vacancies_list()

    while True:
        user.print_commands()
        print(user.tech_message)
        print(f'Найдено {len(user.vacancies_list)} вакансий')
        try:
            command = int(input("Введите команду: "))
        except ValueError:
            print('Нужно ввести число')
            continue

        if command == 1:
            user.filter_by_area()
        elif command == 2:
            user.sort_by_salary()
        elif command == 3:
            user.filter_by_min_salary()
        elif command == 4:
            user.sort_by_date()
        elif command == 5:
            user.filter_by_keywords()
        elif command == 6:
            user.save_query(user.vacancies_list)
            user.tech_message = 'Сохранено в избранное'
        elif command == 7:
            user.vacancies_list = user.read_query()
            user.tech_message = 'Показано избранное'
        elif command == 8:
            user.delete_query()
            user.tech_message = 'Избранное очищено'
        elif command == 9:
            user.get_vacancies_list()
        elif command == 0:
            print(f'Удачи, {user.name.title()}')
            break
        else:
            print('Комманда не существует, введите коррекную команду')

        user.print_vacancies_list()


if __name__ == '__main__':
    main()

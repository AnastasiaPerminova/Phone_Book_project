# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Обязательное ДЗ - доделать телефонный справочник с внешним хранилищем информации,
# дополнить функционалом добавления информации, удаления и редактирования.

import json


def save():
    with open('Phone_book_project\Phone_Book.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(BDnew,
                            ensure_ascii=False))


def load():
    fname = 'Phone_book_project\Phone_Book.json'
    with open(fname, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
    return BD_local


def print_names(names_book):
    for name in names_book.keys():
        print(name)


def print_names_phones(names_book):
    for key in names_book.keys():
        for key2 in names_book[key].keys():
            if key2.lower().find('телефон') >= 0:
                print(f"\033[34m {key} \033[0;0m")
                print(f'{key2} : {names_book[key][key2]}')


def print_info_name(names_book, name):
    find = None
    for key in names_book.keys():
        if name in key.lower():
            find = True
            print(f"\033[34m {key} \033[0;0m")
            for i in names_book[key].items():
                print(*i)
    if find == None:
        print("\033[31mКонтакт не найден. \033[0;0m")


def print_info_info(names_book, info):
    find = None
    for key in names_book.keys():
        for value in names_book[key].values():
            if value.lower().find(info) >= 0:
                print(f"\033[34m {key} \033[0;0m")
                for i in names_book[key].items():
                    print(*i)
                find = True
    if find == None:
        print("\033[31mКонтакт не найден. \033[0;0m")


def edit_contact(names_book):
    print('-' * 50)
    print_names(names_book)
    print('-' * 50)
    print()
    print('Какой контакт Вы хотите отредактировать?')
    name = input('Введите ФИО: ')
    print(f"\033[34m {name} \033[0;0m")
    try:
        for i in names_book[name].items():
            print(*i)
        answer = int(input(
            'Если Вы хотите отредактировать этот контакт, введите 1. Для отмены нажмите 0. Ввод: '))
        if answer == 1:
            names_book.update({f'{name}': {'Номер телефона: ': input('Номер телефона: '),
                                           'Дополнительный номер телефона': input('\nДополнительный номер телефона: '),
                                           'Дата рождения': input('\nДень рождения: '),
                                           'Адрес': input('\nАдрес: ')}})
    except KeyError:
        print('Ошибка ввода данных')


def delete_contact(names_book):
    print('-' * 50)
    print_names(names_book)
    print('-' * 50)
    print()
    print('Какой контакт Вы хотите удалить?')
    name = input('Введите ФИО: ')
    print(f"\033[34m {name} \033[0;0m")
    try:
        for i in names_book[name].items():
            print(*i)
        answer = int(input(
            'Если Вы хотите удалить этот контакт, введите 1. Для отмены нажмите 0. Ввод: '))
        if answer == 1:
            names_book.pop(name)
    except KeyError:
        print('Ошибка ввода данных')


command = None
file = open('Phone_book_project\Phone_Book.json', 'a+')
print('-' * 50)

while command != 0:
    command = int(input('Если Вы хотите просмотреть контакты, введите 1.'
                        '\nЕсли Вы хотите добавить новый контакт, введите 2.'
                        '\nЕсли Вы хотите отредактировать существующий контакт, введите 3.'
                        '\nЕсли Вы хотите удалить контакт, введите 4.'
                        '\nДля завершения работы, введите 0.'
                        '\nВведите команду: '))
    print('-' * 50)
    print()
    if command == 1:
        next_command = int(input('Если Вы хотите вывести весь список контактов, введите 1.'
                                 '\nЕсли Вы хотите вывести весь список контактов с телефонами, введите 2.'
                                 '\nЕсли Вы хотите найти контакт, введите 3.'
                                 '\nДля возврата в главное меню введите 0.'
                                 '\nВведите команду: '))
        print('-' * 50)

        if next_command == 1:
            print('-' * 50)
            try:
                BDnew = load()
                print_names(BDnew)
                print('-' * 50)
                print()
            except ValueError:
                print(
                    '\033[31mТелефонный справочник пуст.Необходимо ввести данные.\033[0;0m')
                print('-' * 50)
                print()
        if next_command == 2:
            print('-' * 50)
            try:
                BDnew = load()
                print_names_phones(BDnew)
                print('-' * 50)
                print()
            except ValueError:
                print(
                    '\033[31mТелефонный справочник пуст.Необходимо ввести данные.\033[0;0m')
                print('-' * 50)
                print()

        if next_command == 3:
            print('-' * 50)
            next_next_command = int(input('Если Вы хотите найти контакт по имени, введите 1.'
                                          '\nЕсли Вы хотите найти контакт по номеру телефона или другой информации, введите 2.'
                                          '\nДля возврата в главное меню введите 0.'
                                          '\nВведите команду: '))
            print('-' * 50)
            print()
            if next_next_command == 1:
                try:
                    BDnew = load()
                    name = input('Введите ФИО: ').lower()
                    print_info_name(BDnew, name)
                    print('-' * 50)
                    print()

                except ValueError:
                    print(
                        '\033[31mТелефонный справочник пуст.Необходимо ввести данные.\033[0;0m')
                    print('-' * 50)
                    print()

            if next_next_command == 2:
                try:
                    BDnew = load()
                    info = input(
                        'Введите информацию(например, номер телефона, дату рождения, адрес): ').lower()
                    print_info_info(BDnew, info)
                    print('-' * 50)
                    print()
                except ValueError:
                    print(
                        '\033[31mТелефонный справочник пуст.Необходимо ввести данные.\033[0;0m')
                    print('-' * 50)
                    print()
    if command == 2:
        try:
            BDnew = load()
            BDnew.update({input('Введите ФИО:'): {'Номер телефона: ': input('Номер телефона: '),
                                                  'Дополнительный номер телефона': input('\nДополнительный номер телефона: '),
                                                  'Дата рождения': input('\nДень рождения: '),
                                                  'Адрес': input('\nАдрес: ')}})
            save()
            print('-' * 50)
            print()
        except ValueError:
            BDnew = {}
            BDnew.update({input('Введите ФИО:'): {'Номер телефона: ': input('Номер телефона: '),
                                                  'Дополнительный номер телефона': input('\nДополнительный номер телефона: '),
                                                  'Дата рождения': input('\nДень рождения: '),
                                                  'Адрес': input('\nАдрес: ')}})
            save()
            print('-' * 50)
            print()

    if command == 3:
        try:
            BDnew = load()
            edit_contact(BDnew)
            save()
            print('-' * 50)
            print()
        except ValueError:
            print(
                '\033[31mТелефонный справочник пуст.Необходимо cначала ввести данные.\033[0;0m')
            print('-' * 50)
            print()

    if command == 4:
        try:
            BDnew = load()
            delete_contact(BDnew)
            save()
            print('-' * 50)
            print()
        except ValueError:
            print(
                '\033[31mТелефонный справочник пуст.Необходимо cначала ввести данные.\033[0;0m')
            print('-' * 50)
            print()

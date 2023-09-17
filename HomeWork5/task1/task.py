# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

filename = 'telebook.txt'

# Показывает информацию в файле
def show_data(filename):
    print('\n№ | ФИО | Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        print(data.read())
    print('')

# Ищет контакт по ФИО
def find_contact(filename):
    with open(filename, 'r', encoding='UTF-8') as data:
        fio = input('Поиск: ')
        lines = data.readlines()
        None_contact = True
        for i in lines:
            if fio in i:
                print('Контакт найден:', i, end = '')
                None_contact = False
        if None_contact:
            print('Контакт не найден')

# Записывает информацию в файл
def export_data(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        tel_file = data.read()
    num = (len(tel_file.split('\n')) + 1)
    with open(filename, 'a', encoding='utf-8') as data:
        fio = input('Введите ФИО: ')
        phone_number = input('Введите номер телефона: ')
        data.write(f'\n{num} | {fio} | {phone_number}')
    print(f'Добавлена запись : {num} | {fio} | {phone_number}\n')

# Изменяет информацию из файла
def edit_data(filename):
    print('\n№ | ФИО | Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
        index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
        tel_book_lines = tel_book.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' | ')
        fio = input('Введите ФИО: ')
        phone = input('Введите номер телефона: ')
        num = elements[0]
        if len(fio) == 0:
            fio = elements[1]
        if len(phone) == 0:
            phone = elements[2]
        edited_line = f'{num} | {fio} | {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print('\n№ | ФИО | Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
        index_delete_data = (int(input('Введите номер строки для удаления: ')) - 1)
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
        with open(filename, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))

choice = -1
while choice != 0:
    print('Выберите одно из действий: ')
    print('1 — Вывести инфо на экран')
    print('2 — Произвести экпорт данных')
    print('3 — Произвести изменение данных')
    print('4 — Произвести удаление данных')
    print('5 — Произвести поиск по ФИО')
    print('0 — Выход из программы')
    choice = int(input('Действие: '))
    if choice == 1: show_data(filename)
    elif choice == 2: export_data(filename)
    elif choice == 3: edit_data(filename)
    elif choice == 4: delete_data(filename)
    elif choice == 5: find_contact(filename)
    else: choice = 0
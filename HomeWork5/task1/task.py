# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# # Показывает информацию в файле
# def show_data(filename):
#     print('\nПП | ФИО | Телефон')
# with open(filename, 'r', encoding='utf-8') as data:
#     print(data.read())
# print('')

# # Записывает информацию в файл
# def export_data(filename):
#     with open(filename, 'r', encoding='utf-8') as data:
#         tel_file = data.read()
# num = len(tel_file.split('\n'))
# with open(filename, 'a', encoding='utf-8') as data:
#     fio = input('Введите ФИО: ')
# phone_number = input('Введите номер телефона: ')
# data.write(f'{num} | {fio} | {phone_number}\n')
# print(f'Добавлена запись : {num} | {fio} | {phone_number}\n')

# # Изменяет информацию из файла
# def edit_data(filename):
#     print('\nПП | ФИО | Телефон')
# with open(filename, 'r'', encoding='utf-8') as data:
#     tel_book = data.read()
# print(tel_book)
# print('')
# index_delete_data = int(input('Введите номер строки для редактирования: '')) — 1
# tel_book_lines = tel_book.split('\n')
# edit_tel_book_lines = tel_book_lines[index_delete_data]
# elements = edit_tel_book_lines.split(» | «)
# fio = input('Введите ФИО: '')
# phone = input('Введите номер телефона: ')
# num = elements[0]
# if len(fio) == 0:
# fio = elements[1]
# if len(phone) == 0:
# phone = elements[2]
# edited_line = f»{num} | {fio} | {phone}»
# tel_book_lines[index_delete_data] = edited_line
# print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
# with open(filename, «w», encoding='utf-8') as f:
# f.write('\n'.join(tel_book_lines))

# # Удаляет информацию из файла
# def delete_data(filename):
#     print('\nПП | ФИО | Телефон')
# with open(filename, 'r', encoding='utf-8') as data:
#     tel_book = data.read()
# print(tel_book)
# print('')
# index_delete_data = int(input('Введите номер строки для удаления: ')) — 1
# tel_book_lines = tel_book.split('\n')
# del_tel_book_lines = tel_book_lines[index_delete_data]
# tel_book_lines.pop(index_delete_data)
# print(f'Удалена запись: {del_tel_book_lines}\n')
# with open(filename, 'w', encoding='utf-8') as data:
# data.write('\n'.join(tel_book_lines))

# def main():
# my_choice = -1
# file_tel = 'tel.txt'

# # Создает файл если его нет в папке
# with open(file_tel, 'a', encoding='utf-8') as file:
# file.write('')

# while my_choice != 0:
# print('Выберите одно из действий: ')
# print('1 — Вывести инфо на экран')
# print('2 — Произвести экпорт данных')
# print('3 — Произвести изменение данных')
# print('4 — Произвести удаление данных')
# print('0 — Выход из программы')
# action = int(input('Действие: '))
# if action == 1:
# show_data(file_tel)
# elif action == 2:
# export_data(file_tel)
# elif action == 3:
# edit_data(file_tel)
# elif action == 4:
# delete_data(file_tel)
# else:
# my_choice = 0

# print('До свидания')

# if __name__ == "__main__":
#     main()




# var2
# class Member:
#     def __init__(self, last_name=None, name=None, phone_number=None, from_line=None):
#         if from_line is None:
#             self.last_name = last_name
#             self.name = name
#             self.phone_number = phone_number
#         else:
#             self.last_name, self.name, self.phone_number = str(from_line).replace(" ", '').split("|")

#     def input_characters(self):
#         self.last_name = input("Введите фамилию: ").capitalize()
#         self.name = input("Введите имя: ").capitalize()
#         self.phone_number = input("Введите номер телефона: ").capitalize()

#     def __str__(self):
#         return '{0:10} | {1:10} | {2}'.format(self.last_name, self.name, self.phone_number) + '\n'


# class Contacts:
#     def find_member(self, query):
#         with open('data.txt') as file:
#             for line in file:
#                 member = Member(from_line=line)
#                 if (member.last_name, member.name) == query:
#                     return member

#     def add_member(self):
#         m = Member()
#         m.input_characters()
#         if c.find_member(query=(m.last_name, m.name)) is None:
#             f = open('data.txt', 'a')
#             f.write('{0:10} | {1:10} | {2}'.format(m.last_name, m.name, m.phone_number) + '\n')
#             print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=m.last_name, name=m.name))
#             f.close()
#         else:
#             print('Такой контакт уже есть')

#     def delete_member(self, query):
#         objects = []
#         f = open('data.txt', 'r+')
#         for line in f.readlines():
#             member = Member(from_line=line)
#             objects.append(member)
#         for object in objects:
#             if (member.last_name, member.name) != query:
#                 f.write(object.__str__())


#     def show_all_contacts(self):
#         with open('data.txt') as file:
#             for line in file:
#                 member = Member(from_line=line)
#                 print(member)


# def choice():
#     selector = None
#     try:
#         selector = int(input('Введите "1" если хотите найти контакт\n' + \
#                              'Введите "2" если хотите добавить новый контакт\n' + \
#                              'Введите "3" если хотите удалить контакт\n' + \
#                              'Введите "4" если хотите просмотреть всю адресную книгу\n' + \
#                              'Ввести здесь ------->:'))
#     except ValueError:
#         print('\n\nНе корректный ввод!!!\n')
#         print('Необходимо ввести целое число!!!\n\n')
#     return selector


# c = Contacts()
# while True:
#     selector = choice()
#     if selector == 1:
#         query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
#                   input('Для поиска контакта введите его имя: ').capitalize()))
#         print(c.find_member(query))
#     elif selector == 2:
#         c.add_member()
#     elif selector == 3:
#         query = ((input('Для удаления контакта введите его фамилию: ').capitalize(),
#                   input('Для удаления контакта введите его имя: ').capitalize()))
#         c.delete_member(query)
#     elif selector == 4:
#         c.show_all_contacts()

# Добавьте к классу Member такой полезный метод:

# def __str__(self):
#     return 'Member("{}", "{}", "{}")'.format(self.last_name, self.name, self.phone_number)
# Затем простейший дебаг:

# class Contacts:
#     def find_member(self, query=None):
#         with open('data.txt') as file:
#             for line in file:
#                 member = Member(from_line=line)
#                 print(member)
#                 if member.last_name == query:
#                     return member
# Вы получите такой вывод:

# Member("Last_name       ", "Name      ", "3141592
# ")
# То есть, метод __init__ класса Member неправильно распарсил данную ему строку, оставил табы и перенос строки.

# Решения:
# Вариант 1. Убирайте эти лишние символы, например, методом str.strip()
# Вариант 2. Используйте готовый функционал для сохранения файлов, например, модуль csv.
# Вариант 3. Используйте БД, например, встроенный SQLite.
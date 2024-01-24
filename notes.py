import os
from datetime import datetime

# Показать заметки
def print_notes():
    print('\n№пп | Заголовок | Заметка | Дата/время')
    with open('notesbook.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        print('')

# Запись заметки

def input_notehead():
    return input('Введите заголовок: ').title()

def input_notebody():
    return input('Введите текст заметки: ').title()

# def input_notedate():
#     return input('Введите текущую дату/время: ').title()





def add_notes():
    with open('notesbook.txt', 'r', encoding='utf-8') as data:
        notes_file = data.read()
        num = len(notes_file.split('\n'))

    with open('notesbook.txt', 'a', encoding='utf-8') as data:
        notehead = input_notehead()
        notebody = input_notebody()
        wr_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        data.write(f'{num} | {notehead} | {notebody} | {wr_time}\n')
        print(f'Добавлена запись : {num} | {notehead} | {notebody} | {wr_time}\n')

# Поиск заметки
def search_notes():
     
    search = input('Введите данные для поиска: ').title()
    print()

    with open('notesbook.txt', 'r', encoding='UTF-8') as file:
        notes_list = file.read().split('\n')
       
    check_cont = False
            
    print('\n№пп | Заголовок | Заметка | Дата/время')
    for lines in notes_list:
        if search in lines:
            print(lines)
            check_cont = True

    if not check_cont:
        print('Такого контакта нет')

# Изменение заметки
def change_notes():
    print('\n№пп | Заголовок | Заметка | Дата/время')
    with open('notesbook.txt', 'r', encoding='utf-8') as data:
        notes_book = data.read()
        print(notes_book)
        print('')
    index_change_data = int(input('Введите номер строки для редактирования: ')) - 1
    note_book_lines = notes_book.split('\n')
    edit_note_book_lines = note_book_lines[index_change_data]
    elements = edit_note_book_lines.split(' | ')
    print(elements)
    notehead = input_notehead()
    notebody = input_notebody()
    wr_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    num = elements[0]
    if len(notehead) == 0:
        notehead = elements[1]
    if len(notebody) == 0:
        notebody = elements[2]

    edited_line = f'{num} | {notehead} | {notebody} | {wr_time}'
    note_book_lines[index_change_data] = edited_line
    print(f'Запись - {edit_note_book_lines}, изменена на - {edited_line}\n')
    with open('notesbook.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(note_book_lines))

# Удаление заметки
def delete_notes():
    print('\n№пп | Заголовок | Заметка | Дата/время')
    with open('notesbook.txt', 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    note_book_lines = tel_book.split('\n')
    del_note_book_lines = note_book_lines[index_delete_data]
    note_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_note_book_lines}\n')

    with open('notesbook.txt', 'w', encoding='utf-8') as data:
        data.write('\n'.join(note_book_lines))

# Интерфейс приложения

def interface():
    with open('notesbook.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    os.system('cls')
    while command != '0':
        print('Меню пользователя: \n'
            '1. Вывод заметок на экран \n'
            '2. Добавить заметку \n'
            '3. Поиск заметки \n'
            '4. Изменение заметки \n'
            '5. Удаление заметки \n'
            '0. Выход \n')
        command = input('Выберите пункт меню: ')

        while command not in ('1', '2', '3', '4', '5', '0'):
            print('Не корректный ввод, поворите запрос')
            command = input('Выберите пункт меню: ')

        match command:
            case '1':
                print_notes()
            case '2':
                add_notes()
            case '3':
                search_notes()
            case '4':
                change_notes()
            case '5':
                delete_notes()
            case '0':
                print('Завершение программы')
        print()

if __name__ == '__main__':
    interface()
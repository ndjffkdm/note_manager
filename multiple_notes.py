print('Добро пожаловать в менеджер заметок! Вы можете создать заметку.')
notes = list()
while True:
    answer = input('Хотите создать заметку? ')
    if answer == 'да':
        info = dict()
        info['Имя пользователя'] = input('Введите ваше имя: ')
        info['Заголовки'] = [] # создаем список для хранения нескольких заголовков
        for i in range(3):
            title = input(f"Введите заголовок заметки {i + 1}: ")
            info['Заголовки'].append(title)
        info['Описание'] = input('Введите описание заметки: ')
        info['Статус'] = input('Введите статус заметки (Выполнено/В работе/Отложено): ')
        created_date = input('Введите дату создания заметки (в формате xx-xx-xxxx): ')
        issue_date = input('Введите дату истечения заметки (в формате xx-xx-xxxx): ')
        info['Дата создания'] = created_date[0:5]
        info['Дата истечения'] = issue_date[0:5]
        print('\nУказанные данные')
        for key, value in info.items():
                print(f"{key}: {value}")
        notes.append(info)
    elif answer == 'нет':
        print('\nВаши заметки: ')
        for i in notes:
            note_number = notes.index(i) + 1
            print('\n', note_number, 'заметка')
            for key, value in i.items():
                print(f'{key}: {value}')
        break
    else:
        print('Ошибка!')
        print('Попробуйте ещё раз')
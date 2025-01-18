import datetime

print("Добро пожаловать в менеджер заметок!")
notes = list()
while True:
    print("\nВыберите действие: ", "1. Создать заметку", "2. Удалить заметку",
          "3. Показать список заметок", "4. Завершить работу", sep='\n')
    answer = input()
    if answer == "1":
        answer_create = input("\nХотите создать заметку? \n")
        if answer_create == "да":
            info = dict()
            info["Имя пользователя"] = input("Введите ваше имя: ")
            info["Заголовки"] = titles = []
            while True:
                title = input("Введите название заголовка или 'стоп': ")
                titles.append(title)
                if title == 'стоп':
                    titles.pop()
                    break
            info["Описание"] = input("Введите описание заметки: ")
            status = {1: 'Выполнено', 2: 'В работе', 3: 'Отложено'}
            while True:
                print('Выберите статус заметки:', '1. Выполнено', '2. В работе',
                      '3. Отложено', sep='\n')
                new_status = input()
                if new_status == '1':
                    print('Обновлённый статус заметки:', status[1])
                    info["Статус"] = status[1]
                    break
                elif new_status == '2':
                    print('Обновлённый статус заметки:', status[2])
                    info["Статус"] = status[2]
                    break
                elif new_status == '3':
                    print('Обновлённый статус заметки:', status[3])
                    info["Статус"] = status[3]
                    break
                else:
                    print('Неверно указан статус!')
                    print('Введите только цифру\n')
            created_date = input("Введите дату создания заметки (в формате xx-xx-xxxx): ")
            while True:
                try:
                    issue_date = input('Введите дату истечения заметки (в формате xx-xx-xxxx, например 10-01-2025):')
                    deadline_date = datetime.datetime.strptime(issue_date, "%d-%m-%Y")
                    time_difference = datetime.datetime.today() - deadline_date
                    days_difference = time_difference.days
                    if days_difference > 0:
                        print(f'Дедлайн истек {abs(days_difference):02d} дней назад!')
                    elif days_difference == 0:
                        print('Дедлайн истекает сегодня!')
                    else:
                        print(f'Дедлайн истекает через {abs(days_difference):02d} дней.')
                    break
                except ValueError:
                    print('Ошибка! Пожалуйста, введите дату в формате xx-xx-xx (день-месяц-год)')
                except Exception as e:
                    print(f"Произошла непредвиденная ошибка: {str(e)}")
                    print("Пожалуйста, попробуйте снова.")
            info["Дата создания"] = created_date[0:5]
            info["Дата истечения"] = issue_date[0:5]
            print("\nУказанные данные")
            for key, value in info.items():
                print(f"{key}: {value}")
            notes.append(info)
        elif answer_create == "нет":
            continue
        else:
            print("\nОшибка ввода!")
            print("Попробуйте ещё раз")
    elif answer == "2":
        print("\nУдаление заметки")
        answer_delete = input("\nХотите удалить заметку?\n")
        if answer_delete == "да":
            word = input("Укажите имя пользователя ненужной заметки:\n")
            for i in range(len(notes)):
                if notes[i]["Имя пользователя"] == word:
                    del notes[i]
            print("\nОбновлённый список заметок: ")
            for i in notes:
                note_number = notes.index(i) + 1
                print("\n", f'заметка №{note_number}')
                for key, value in i.items():
                    print(f'{key}: {value}')
        elif answer_delete == "нет":
            continue
    elif answer == "3":
        print("\nВаши заметки: ")
        for i in notes:
            note_number = notes.index(i) + 1
            print("\n", f'заметка №{note_number}')
            for key, value in i.items():
                print(f'{key}: {value}')
    elif answer == "4":
        break
    else:
        print("\nОшибка ввода!")
        print("Попробуйте ещё раз")

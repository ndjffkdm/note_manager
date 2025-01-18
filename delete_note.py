# приветствуем пользователя и создаем список для хранения заметок
print("Добро пожаловать в менеджер заметок! Вы можете создать или удалить заметку.")
notes = list()

# делаем бесконечный цикл для создания небольшого меню
while True:
    print("\nВыберите действие: ", "1. Создать заметку", "2. Удалить заметку", "3. Показать список заметок", sep='\n')
    answer = input()
    if answer == "1":
        # подтверждаем выбор пользователя
        answer_create = input("\nХотите создать заметку? \n")
        if answer_create == "да":
            # если ответ да, то запрашиваем данные для создания заметки
            info = dict()
            info["Имя пользователя"] = input("Введите ваше имя: ")
            info["Заголовок"] = input("Введите заголовок заметки: ")
            info["Описание"] = input("Введите описание заметки: ")
            info["Статус"] = input("Введите статус заметки (Выполнено/В работе/Отложено): ")
            created_date = input("Введите дату создания заметки (в формате xx-xx-xxxx): ")
            issue_date = input("Введите дату истечения заметки (в формате xx-xx-xxxx): ")
            info["Дата создания"] = created_date[0:5]
            info["Дата истечения"] = issue_date[0:5]
            print("\nУказанные данные")
            for key, value in info.items():
                print(f"{key}: {value}")
            notes.append(info) # добавляем заметку в список
        elif answer_create == "нет":
            # если ответ нет, то возвращаемся в меню
            continue
        else:
            print("\nОшибка ввода!")
            print("Попробуйте ещё раз")
    elif answer == "2":
        # подтверждаем выбор пользователя
        print("\nУдаление заметки")
        answer_delete = input("\nХотите удалить заметку?\n")
        if answer_delete == "да":
            # если ответ да, то запрашиваем имя пользователя для удаления заметки
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
            # если ответ нет, то возвращаемся в меню
            continue
    elif answer == "3":
        print("\nВаши заметки: ")
        for i in notes:
            note_number = notes.index(i) + 1
            print("\n", f'заметка №{note_number}')
            for key, value in i.items():
                print(f'{key}: {value}')
    else:
        print("\nОшибка ввода!")
        print("Попробуйте ещё раз")
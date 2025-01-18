# создаем словарь для быстрого доступа к статусам по ключам
status = {1: 'Выполнено', 2: 'В работе', 3: 'Отложено'}

# задаем нашей заметке произвольный статус и уведомляем об этом пользователя
current_status = status[2]
print(f'Текущий статус заметки: {current_status}')
# создаем бесконечный цикл для подтверждения смены статуса
while True:
    answer = input('Хотите изменить статус заметки?\n')
    if answer == 'да':
        # создаем бесконечный цикл для смены статуса
        # предоставляем 3 варианта ответа (по номеру)
        while True:
            print('Выберите статус заметки:', '1. Выполнено', '2. В работе', '3. Отложено', sep='\n')
            new_status = input()
            if new_status == '1':
                print('Обновлённый статус заметки:', status[1])
                current_status = status[1]
                break
            elif new_status == '2':
                print('Обновлённый статус заметки:', status[2])
                current_status = status[2]
                break
            elif new_status == '3':
                print('Обновлённый статус заметки:', status[3])
                current_status = status[3]
                break
            else:
                print('Неверно указан статус!')
                print('Введите только цифру\n')
        break
    elif answer == 'нет':
        print('До свидания!')
        break
    else:
        print('Ошибка!')
        print('Попробуйте да/нет\n')
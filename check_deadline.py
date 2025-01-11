# импорт необходимых модулей
from datetime import datetime

# основной блок кода
while True:
    try:
        # запрашиваем дату дедлайна
        deadline_str = input('Введите дату истечения (в формате xx-xx-20xx, например 10-01-2025): ')

        # преобразуем строку с датой в объект datetime
        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y")

        # вычисляем разницу между текущей датой и дедлайном
        current_date = datetime.now() # текущая дата
        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        # проверяем статус дедлайна и выводим соответствующее сообщение
        if days_difference < 0:
            print(f'Дедлайн истек {abs(days_difference):02d} дней назад!')
        elif days_difference == 0:
            print('Дедлайн истекает сегодня!')
        else:
            print(f'Дедлайн истекает через {days_difference:02d} дней.')

        # прерываем цикл после успешной обработки даты
        break
    except ValueError:
        #  обработка ошибки неверного формата даты
        print('Ошибка! Пожалуйста, введите дату в формате xx-xx-xx (день-месяц-год)')
    except Exception as e:
        # Обработка прочих ошибок
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")

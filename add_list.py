# запрашиваем данные у пользователя
username = input('Введите ваше имя: ')
title1 = input('Первый заголовок заметки: ')
title2 = input('Второй заголовок заметки: ')
title3 = input('Третий заголовок заметки: ')
titles = [title1, title2, title3] # создаем список для хранения заголовков
content = input('Описание заметки: ')
status = input('Укажите статус заметки (Активна/Неактивна): ')
created_date = input('Дата создания заметки (в формате хх-хх-хх): ')
issue_date = input('Дата истечения заметки (в формате хх-хх-хх): ')
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

# выводим указанные данные
print('\nУказанные данные')
print('Имя пользователя:', username)
print('Заголовок:', ', '.join(titles)) # используем функцию join() для вывода без скобок
print('Описание:', content)
print('Статус:', status)
print('Дата создания:', temp_created_date)
print('Дата истечения:', temp_issue_date)

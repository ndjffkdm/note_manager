username = input('Введите ваше имя: ')
title = input('Заголовок  заметки: ')
content = input('Описание хаметки: ')
status = input('Укажите статус заметки (Активна/Неактивна): ')
created_date = input('Дата создания заметки (в формате хх-хх-хх): ')
issue_date = input('Дата истечения заметки (в формате хх-хх-хх): ')
print('\nУказанные данные')
print('Имя пользователя:', username)
print('Заголовок:', title)
print('Описание:', content)
print('Статус:', status)
print('Дата создания:', created_date[0:5])
print('Дата истечения:', issue_date[0:5])

# запрашиваем у пользователя нужные данные с помощью input()
username = input('Введите ваше имя: ')
title = input('Заголовок  заметки: ')
content = input('Описание хаметки: ')
status = input('Укажите статус заметки (Активна/Неактивна): ')
created_date = input('Дата создания заметки (в формате хх-хх-хх): ')
issue_date = input('Дата истечения заметки (в формате хх-хх-хх): ')
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

# выводим полученные данные
print('\nУказанные данные')
print('Имя пользователя:', username)
print('Заголовок:', title)
print('Описание:', content)
print('Статус:', status)
print('Дата создания:', temp_created_date)
print('Дата истечения:', temp_issue_date)

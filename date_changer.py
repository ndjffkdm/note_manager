# запрашиваем данные у пользователя
username = 'райан гослинг'
title = 'поход в магазин'
content = 'купить пиво, кириешки и рыбку'
status = 'Активна'
created_date = '10-11-24'
issue_date = '10-12-24'

# создаем временные переменные
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

# выводим полученные данные
print('имя пользователя:', username )
print('заголовок:', title)
print('описание:', content)
print('статус: ', status)
print('дата создания заметки:', temp_created_date)
print('дата дедлайна:', temp_issue_date)

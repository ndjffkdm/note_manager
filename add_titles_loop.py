# создаем список для заголовков
titles = []
# используем бесконечный цикл для добавления любого числа заметок
while True:
    title = input("Введите название заголовка или 'стоп': ")
    titles.append(title)
    if title == 'стоп':
        titles.pop()
        break
print('\nЗаголовки:')
print(*titles, sep='\n')
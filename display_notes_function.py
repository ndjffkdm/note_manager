def display_page(notes, page):
    start_index = 0 + (page - 1) * 5
    end_index = 5 + (page - 1) * 5

    for index, note in enumerate(notes[start_index:end_index], start=1):
        print(f'''
            __Заметка № {index}__
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание: {note["content"]}
        Статус: {note["status"]}
        Дата создания: {note["created_date"]}
        Дата истечения: {note["issue_date"]}
        ''')
        print('=' * 50)


def display_notes(notes, page_number=1):
    if len(notes) == 0:
        print("У вас нет сохранённых заметок")
    else:
        display_page(notes, page_number)


if __name__ == "__main__":
    notes = [
        {"username": "maks", "title": "заголовок1", "content": "описание1",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-01-2025"},
        {"username": "alex", "title": "заголовок2", "content": "описание2",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-02-2025"},
        {"username": "denis", "title": "заголовок3", "content": "описание3",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-03-2025"},
        {"username": "oleg", "title": "заголовок4", "content": "описание4",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-04-2025"},
        {"username": "masha", "title": "заголовок5", "content": "описание5",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-05-2025"},
        {"username": "nastya", "title": "заголовок6", "content": "описание6",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-06-2025"},
        {"username": "vlad", "title": "заголовок7", "content": "описание7",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-07-2025"},
        {"username": "igor", "title": "заголовок8", "content": "описание8",
         "status": "выполнено", "created_date": "21-01-2025", "issue_date": "30-08-2025"}
        ,
    ]
    display_notes(notes=notes, page_number=2)

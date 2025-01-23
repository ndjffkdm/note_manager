def search_notes(notes, keyword=None, status=None):
    keyword_list = ["username", "title", "content"]
    found_notes = []

    for note in notes:

        if keyword is not None and status is not None:
            for note_key in keyword_list:
                if note["status"] == status:
                    found_notes.append(note)
                    break
                if keyword is not note[note_key]:
                    break

        elif keyword is not None:
            for note_key in keyword_list:
                if keyword == note[note_key]:
                    found_notes.append(note)

        elif status is not None:
            if note["status"] == status:
                found_notes.append(note)

    return found_notes


if __name__ == "__main__":
    notes = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю", "status": "новая"},
        {"username": "Мария", "title": "Учеба", "content": "Подготовиться к экзамену", "status": "в процессе"},
        {"username": "Иван", "title": "План работы", "content": "Завершить проект", "status": "выполнено"},
        {"username": "Иван", "status": "в процессе"}
    ]
    found_notes = search_notes(notes)
    print("Найденные заметки: ")
    print(found_notes)

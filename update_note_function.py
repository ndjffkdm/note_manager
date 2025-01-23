import datetime


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def update_note(note):
    print("=== Обновление заметки ===")
    print("Данные вашей заметки: ")
    for key, value in note.items():
        print(f"{key}: {value}")

    note_keys = ["username", "title", "content", "status", "issue_date"]
    while True:
        note_key = input(f"\nКакое значение вы бы хотели изменить? ({', '.join(note_keys)}): \n").strip().lower()
        if note_key not in note_keys:
            print(f"Ошибка! Значение {note_key} не найдено")
            continue

        if note_key == "issue_date":
            new_value = input(f"Введите новое значение для {note_key} (день-месяц-год): ").strip()
            if not validate_date(new_value):
                print("Ошибка: Неверный формат даты. Используйте формат 'день-месяц-год'.")
                continue

        elif note_key == "status":
            status_options = ["выполнено", "в работе", "отложено"]
            new_value = input(f"Введите новый статус заметки ({', '.join(status_options)}): ").strip().lower()
            while new_value not in status_options:
                print(f"Неверный статус. Доступные варианты: {', '.join(status_options)}.")
                new_value = input(f"Введите статус заметки ({', '.join(status_options)}): ").strip().lower()

        else:
            new_value = input(f"Введите новое значение для {note_key}: ")
            if not new_value:
                print(f"Ошибка: Значение для {note_key} не может быть пустым.")
                continue

        note[note_key] = new_value
        print(f"\nЗаметка успешно обновлена: {note_key} -> {new_value}")

        another_update = input("\nХотите обновить ещё одно поле? (да/нет): ").strip().lower()
        if another_update == "да":
            continue
        else:
            break

    return note


if __name__ == "__main__":
    note = {
        "username": "максим",
        "title": "вишлист",
        "content": "айфон, бмв, квартира",
        "status": "в работе",
        "created_date": "23-01-2025",
        "issue_date": "15-04-2025"
    }
    updated_note = update_note(note)
    print("Обновлённая заметка:")
    for key, value in updated_note.items():
        print(f"{key}: {value}")

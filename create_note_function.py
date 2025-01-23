from datetime import datetime


def create_note():
    print("=== Создание новой заметки ===")
    username = input("Введите имя пользователя: ").strip()
    while not username:
        print("Имя пользователя не может быть пустым.")
        username = input("Введите имя пользователя: ").strip()

    title = input("Введите заголовок заметки: ").strip()
    while not title:
        print("Заголовок заметки не может быть пустым.")
        title = input("Введите заголовок заметки: ").strip()

    content = input("Введите описание заметки: ").strip()
    while not content:
        print("Описание заметки не может быть пустым.")
        content = input("Введите описание заметки: ").strip()

    status_options = ["выполнено", "в работе", "отложено"]
    status = input(f"Введите статус заметки ({', '.join(status_options)}): ").strip().lower()
    while status not in status_options:
        print(f"Неверный статус. Доступные варианты: {', '.join(status_options)}.")
        status = input(f"Введите статус заметки ({', '.join(status_options)}): ").strip().lower()

    created_date = datetime.now().strftime("%d-%m-%Y")

    issue_date = input("Введите дату дедлайна (день-месяц-год): ").strip()
    while not validate_date(issue_date):
        print("Неверный формат даты. Пожалуйста, используйте формат 'день-месяц-год'.")
        issue_date_as_str = input("Введите дату дедлайна (день-месяц-год): ").strip()
        issue_date = datetime.strptime(issue_date_as_str, "%d-%m-%Y")

    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    return note


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    note = create_note()
    print(f"\nЗаметка создана:\n{note}")

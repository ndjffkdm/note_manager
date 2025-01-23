from colorama import init, Fore, Style

from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

init(autoreset=True)


def delete_note(notes):
    while True:
        answer = input("Вы точно хотите удалить заметку?\n")
        if answer == "да":
            word = input("Укажите имя пользователя ненужной заметки:\n")
            for i in range(len(notes)):
                if notes[i]["Имя пользователя"] == word:
                    del notes[i]
            print("\nОбновлённый список заметок: ")
            for i in notes:
                note_number = notes.index(i) + 1
                print("\n", f'заметка №{note_number}')
                for key, value in i.items():
                    print(f'{key}: {value}')
            break
        elif answer == "нет":
            break
        else:
            print("Неверный формат ввода, попробуйте ещё раз")
    return notes


def display_menu(notes):
    while True:
        # Отобразить меню
        print(f"{Fore.GREEN}\nМеню действий:")
        print(f"{Fore.BLUE}1. Создать новую заметку")
        print(f"{Fore.YELLOW}2. Показать все заметки")
        print(f"{Fore.RED}3. Обновить заметку")
        print(f"{Fore.CYAN}4. Удалить заметку")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}5. Найти заметки")
        print("6. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                note = create_note()
                notes.append(note)
            elif choice == "2":
                display_notes(notes)
            elif choice == "3":
                if notes:
                    display_notes(notes)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("Неверный номер заметки.")
                else:
                    print("Список заметок пуст.")
            elif choice == "4":
                notes = delete_note(notes)
            elif choice == "5":
                keyword = input("Введите ключевое слово для поиска: ")
                status = input("Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
            elif choice == "6":
                print("Работа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")


if __name__ == "__main__":
    notes = list()
    display_menu(notes)

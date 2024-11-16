from tkinter import ttk
import tkinter as tk
import json


def save_book_info_to_json(author, title, genre, age, pages, year):
    # Словарь с данными книги
    book_data = {
        "author": author,
        "title": title,
        "genre": genre,
        "age": age,
        "pages": pages,
        "year": year
    }

    # Попытка открыть файл books.json и добавить новые данные
    try:
        # Открытие файла в режиме чтения и записи
        with open('books.json', 'r+', encoding='utf-8') as file:
            try:
                books = json.load(file)
            except json.JSONDecodeError:
                # Если файл пуст или поврежден, создаем пустой список
                books = []

            books.append(book_data)
            file.seek(0)
            json.dump(books, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        # Если файл не существует, создается новый
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump([book_data], file, ensure_ascii=False, indent=4)


def open_book_info_window():
    # Главное окно
    book_window = tk.Toplevel()
    book_window.title("BookInformation")
    book_window.geometry("400x400")  # Размер окна
    book_window.resizable(False, False)

    # "Информация о книге"
    info_label = tk.Label(book_window, text="Информация о книге", font=("Arial", 14))
    info_label.pack(pady=10)

    # Поле "Автор"
    author_label = tk.Label(book_window, text="Автор:")
    author_label.place(x=20, y=60)

    author_entry = tk.Entry(book_window, width=30)
    author_entry.place(x=150, y=60)

    # Поле "Название"
    title_label = tk.Label(book_window, text="Название:")
    title_label.place(x=20, y=100)

    title_entry = tk.Entry(book_window, width=30)
    title_entry.place(x=150, y=100)

    # Поле "Жанр"
    genre_label = tk.Label(book_window, text="Жанр:")
    genre_label.place(x=20, y=140)

    genre_entry = tk.Entry(book_window, width=30)
    genre_entry.place(x=150, y=140)

    # Поле "Возрастной рейтинг"
    age_label = tk.Label(book_window, text="Возрастной рейтинг:")
    age_label.place(x=20, y=180)

    age_entry = tk.Entry(book_window, width=30)
    age_entry.place(x=150, y=180)

    # Поле "Количество страниц"
    pages_label = tk.Label(book_window, text="Количество страниц:")
    pages_label.place(x=20, y=220)

    pages_entry = tk.Entry(book_window, width=30)
    pages_entry.place(x=150, y=220)

    # Поле "Год издания"
    year_label = tk.Label(book_window, text="Год издания:")
    year_label.place(x=20, y=260)

    year_entry = tk.Entry(book_window, width=30)
    year_entry.place(x=150, y=260)

    # Функция для кнопки "Подтвердить"
    def confirm_book_info():
        # Собираем информацию из полей
        author = author_entry.get()
        title = title_entry.get()
        genre = genre_entry.get()
        age = age_entry.get()
        pages = pages_entry.get()
        year = year_entry.get()

        # Вызываем функцию для сохранения данных в файл
        save_book_info_to_json(author, title, genre, age, pages, year)

        book_window.destroy()

    # Кнопка "Подтвердить"
    confirm_button = tk.Button(book_window, text="Подтвердить", command=confirm_book_info)
    confirm_button.place(x=150, y=320)

def load_unique_values(field):
    # Добавление значений в выпадающий список
    try:
        with open('books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)

        field_values = []

        for book in books:
            # Если указанное поле в текущей записи
            if field in book:
                # Добавляется значение поля в список
                field_values.append(book[field])

        # Удаляются дубликаты и сортировка значений
        unique_sorted_values = sorted(set(field_values))

        return unique_sorted_values

    except FileNotFoundError:
        # Если файл не найден, возвращается пустой список
        return []


def create_interface():
    # Главное окно приложения
    root = tk.Tk()
    root.title("BookSelection")
    root.geometry("600x700")
    root.resizable(False, False)

    # Кнопка "Пополнить книжный фонд"
    replenish_button = tk.Button(root, text="Пополнить книжный фонд", command=open_book_info_window)
    replenish_button.pack(pady=10)

    # Поле "Поиск"
    search_label = tk.Label(root, text="Поиск:")
    search_label.place(x=20, y=60)

    # Поле "По автору"
    author_label = tk.Label(root, text="По автору:")
    author_label.place(x=20, y=100)

    author_combobox = ttk.Combobox(root, width=30)
    author_combobox.place(x=150, y=100)
    author_combobox['values'] = load_unique_values('author')

    # Поле "По названию"
    title_label = tk.Label(root, text="По названию:")
    title_label.place(x=20, y=140)

    title_combobox = ttk.Combobox(root, width=30)
    title_combobox.place(x=150, y=140)
    title_combobox['values'] = load_unique_values('title')

    # Поле "По жанру"
    genre_label = tk.Label(root, text="По жанру:")
    genre_label.place(x=20, y=180)

    genre_combobox = ttk.Combobox(root, width=30)
    genre_combobox.place(x=150, y=180)
    genre_combobox['values'] = load_unique_values('genre')

    # Поле "По возрастному ограничению"
    age_label = tk.Label(root, text="По возрастному ограничению:")
    age_label.place(x=20, y=220)

    age_combobox = ttk.Combobox(root, width=30)
    age_combobox.place(x=220, y=220)
    age_combobox['values'] = load_unique_values('age')

    # Поле "По количеству страниц"
    pages_label = tk.Label(root, text="По количеству страниц:")
    pages_label.place(x=20, y=260)

    pages_from_label = tk.Label(root, text="от:")
    pages_from_label.place(x=200, y=260)

    pages_from_entry = tk.Entry(root, width=10)
    pages_from_entry.place(x=230, y=260)

    pages_to_label = tk.Label(root, text="до:")
    pages_to_label.place(x=310, y=260)

    pages_to_entry = tk.Entry(root, width=10)
    pages_to_entry.place(x=340, y=260)

    # Поле "По году издания"
    year_label = tk.Label(root, text="По году издания:")
    year_label.place(x=20, y=300)

    year_from_label = tk.Label(root, text="от:")
    year_from_label.place(x=200, y=300)

    year_from_entry = tk.Entry(root, width=10)
    year_from_entry.place(x=230, y=300)

    year_to_label = tk.Label(root, text="до:")
    year_to_label.place(x=310, y=300)

    year_to_entry = tk.Entry(root, width=10)
    year_to_entry.place(x=340, y=300)

    def search():
        # Сбор данных из полей поиска
        author = author_combobox.get()
        title = title_combobox.get()
        genre = genre_combobox.get()
        age = age_combobox.get()
        pages_from = pages_from_entry.get()
        pages_to = pages_to_entry.get()
        year_from = year_from_entry.get()
        year_to = year_to_entry.get()

        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)

            # Фильтрация книг
            filtered_books = []

            for book in books:
                # Проверяем параметры поочередно
                if author and book.get('author') != author:
                    continue
                if title and book.get('title') != title:
                    continue
                if genre and book.get('genre') != genre:
                    continue
                if age and book.get('age') != age:
                    continue
                pages = book.get('pages')
                if pages is not None:
                    if pages_from and pages < int(pages_from):
                        continue
                    if pages_to and pages > int(pages_to):
                        continue
                year = book.get('year')
                if year is not None:
                    if year_from and year < int(year_from):
                        continue
                    if year_to and year > int(year_to):
                        continue

                # Если книга прошла все проверки, она добавляется в список
                filtered_books.append(book)

            # Очистка таблицы
            tree.delete(*tree.get_children())

            # Добавление результатов в таблицу
            for book in filtered_books:
                tree.insert("", "end", values=(book["author"], book["title"], book["genre"], book["age"], book["pages"], book["year"]))

        except FileNotFoundError:
            print("Файл books.json не найден.")

    # Кнопка "Поиск"
    search_button = tk.Button(root, text="Поиск", command=search)
    search_button.place(x=260, y=340)

    # Поле вывода информации
    columns = ("author", "title", "genre", "age", "pages", "year")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
    tree.place(x=20, y=380, width=560, height=280)

    # Настройка заголовков колонок
    tree.heading("author", text="Автор")
    tree.heading("title", text="Название")
    tree.heading("genre", text="Жанр")
    tree.heading("age", text="Ценз")
    tree.heading("pages", text="Страницы")
    tree.heading("year", text="Год")

    # Цикл окна
    root.mainloop()


if __name__ == "__main__":
    create_interface()




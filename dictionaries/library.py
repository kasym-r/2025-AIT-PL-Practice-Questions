library = {
    "Fiction": [
        {"title": "The Great Gatsby", "available": True},
        {"title": "To Kill a Mockingbird", "available": False}
    ],
    "Science": [
        {"title": "A Brief History of Time", "available": True},
        {"title": "The Selfish Gene", "available": False},
        {"title": "Quantum Mechanics", "available": True}
    ],
    "History": [
        {"title": "The Histories", "available": True},
        {"title": "The Iliad", "available": True},
        {"title": "The Second World War", "available": False},
        {"title": "Hiroshima", "available": True}
    ]
}

# Задания
# 1. Подсчёт всех книг
# count_books(library: dict) -> int — вернуть общее количество книг во всех разделах. 
def count_books(library):
    count = 0
    for sections, books in library.items():
        for book in books:
            count += 1
    return count

# print(count_books(library))
# print(sum(len(books) for books in library.values()))

# 2. Подсчёт доступных книг
# count_available(library: dict) -> int — вернуть число книг, где available == True.
def count_available(library):
    count = 0
    for categories, values in library.items():
        for book in values:
            if book['available'] == True:
                count += 1
    return count

# print(count_available(library))

# 3. Найти раздел по книге
# find_book_section(library: dict, title: str) -> str | None — вернуть название раздела, содержащего книгу (без учёта регистра).
def find_book_section(library, title):
    for section, books in library.items():
        for book in books:
            if book['title'].lower() == title.lower():
                return section
    return None

# print(find_book_section(library, "a brief history of time"))

# 4. Выдать книгу
# checkout(library: dict, title: str) -> bool — если книга существует и доступна, установить available=False; вернуть успех.
def checkout(library, title):
    for books in library.values():
        for book in books:
            if book['title'] == title and book['available'] == True:
                book['available'] = False
                return True
    return False

# print(checkout(library, 'Quantum Mechanics'))

# 5. Вернуть книгу
# return_book(library: dict, title: str) -> bool — если книга существует и выдана, установить available=True; вернуть успех.
def return_book(library, title):
    for categories, values in library.items():
        for book in values:
            if book['title'] == title and book['available'] == False:
                book['available'] = True
                return True
    return False

# print(return_book(library, 'The Second World War'))

# 6. Список доступных книг
# list_available(library: dict) -> list[str] — вернуть отсортированный по алфавиту список доступных названий.
def list_available(library):
    available_books = []
    for categ, val in library.items():
        for book in val:
            if book['available'] == True:
                available_books.append(book['title'])
    return sorted(available_books)

print(list_available(library))

# 7. Размер раздела
# section_size(library: dict, section: str) -> int — вернуть количество книг в разделе (0, если раздел отсутствует).
def section_size(library, section):
    count = 0
    for sections, books in library.items():
        for book in books:
            if section == sections:
                count += 1
    return count

def section_size2(library, section):
    return len(library.get(section, []))

# print(section_size2(library, 'History'))

# 8. Выдать все книги раздела
# checkout_section(library: dict, section: str) -> int — отметить все доступные книги раздела как выданные; вернуть число изменений.
def checkout_section(library, section):
    count = 0
    for sections, books in library.items():
        if section == sections:
            for book in books:
                if book['available'] == True:
                    book['available'] = False
                    count += 1
    return count

# print(checkout_section(library, 'History'))

# 9. Подсчёт выданных книг
# count_checked_out(library: dict) -> int — вернуть количество книг с available == False.
def count_checked_out(library):
    count = 0
    for sections, books in library.items():
        for book in books:
            if book['available'] == False:
                count += 1
    return count

# print(count_checked_out(library))

# 10. Самое длинное название
# longest_title(library: dict) -> str | None — вернуть книгу с самым длинным названием (при равенстве — по алфавиту).
def longest_title(library):
    # arr = []
    # for sections, books in library.items():
    #     for book in books:
    #         arr.append(book['title'])
    # return sorted(arr, key = len)[-1]
    titles = [book['title'] for books in library.values() for book in books]
    if not titles:
        return None
    return max(sorted(titles), key = len)
    
# print(longest_title(library))

# 11. Отчёт по библиотеке
# report(library: dict) -> dict — вернуть {'total_books': int, 'available': int, 'checked_out': 
# int, 'sections': {sec: {'total': int, 'available': int, 'checked_out': int}}}.
def report(library):
    total_books = 0
    available = 0
    checked_out = 0
    sections_report = {}

    for section, books in library.items():
        sec_total = len(books)
        sec_available = sum(1 for book in books if book['available'])
        sec_checked_out = sec_total - sec_available

        sections_report[section] = {
            "total": sec_total,
            "available": sec_available,
            "checked_out": sec_checked_out
        }

        total_books += sec_total
        available += sec_available
        checked_out += sec_checked_out
    
    return {
        "total_books": total_books,
        "available": available,
        "checked_out": checked_out,
        "sections": sections_report
    }

# print(report(library))

# 12. Добавить книгу в раздел
# add_book(library: dict, section: str, title: str, available: bool=True) -> bool
# — создать раздел при необходимости; не допускать дубликаты названий в разделе (без учёта регистра).
def add_book(library, section, title, available: bool = True):
    if section not in library:
        library[section] = []
    
    for book in library[section]:
        if book['title'].lower() == title.lower():
            return False
    
    library[section].append({"title": title, "available": available})
    return True
                
# print(add_book(library, "Fiction", "the great gatsby",), library)

# 13. Удалить книгу по названию
# remove_book(library: dict, title: str) -> bool — удалить первое вхождение книги (по всем разделам).
def remove_book(library, title):
    for books in library.values():
        for i, book in enumerate(books):
            if book['title'].lower() == title.lower():
                books.pop(i)
                return True
    return False

# print(remove_book(library, 'the great gatsby'), library)

# 14. Переместить книгу между разделами
# move_book(library: dict, title: str, to_section: str) -> bool — переместить книгу, сохранив статус; не создавать дубликатов в целевом разделе.
def move_book(library, title, to_section):
    if to_section not in library:
        library[to_section] = []

    for section, books in library.items():
        for i, book in enumerate(books):
            if book['title'] == title:
                books.pop(i)
                library[to_section].append(book)
                return True
    return False

# print(move_book(library, "The Great Gatsby", "Science"), library)

# 15. Удалить дубликаты в разделе
# dedupe_section_titles(library: dict, section: str) -> int — удалить дубли названий в разделе, сохранив первое вхождение; вернуть число удалённых.
# def dedupe_section_titles(library, section): 
def dedupe_section_titles(library, section):
    if section not in library:
        return 0
    
    seen = set()
    unique_books = []
    removed = 0

    for book in library[section]:
        title_lower = book['title'].lower()
        if title_lower not in seen:
            seen.add(title_lower)
            unique_books.append(book)
        else:
            removed += 1

    library[section] = unique_books

    return removed, unique_books

# print(dedupe_section_titles(library, 'Fiction'))

# 16. Поиск по префиксу
# titles_starting_with(library: dict, prefix: str, only_available: bool=False) ->
# list[str] — поиск названий по префиксу (без учёта регистра); опционально только доступные; вернуть отсортированный список.
def titles_starting_with(library, prefix, only_available):
    arr = []
    for section, books in library.items():
        for book in books:
            if book['title'].lower().startswith(prefix.lower()) and book['available'] == only_available:
                arr.append(book['title'])
    return sorted(arr)

# print(titles_starting_with(library, "The", True))

# 17. Доля доступных по разделам
# availability_ratio(library: dict) -> dict[str, float] — вернуть долю доступных книг в каждом разделе (округлить до 2 знаков).
def availability_ratio(library):
    ratios = {}
    for section, books in library.items():
        sec_total = len(books)
        sec_available = sum(1 for book in books if book['available'])
        sec_ratio = round(sec_available / sec_total, 2)

        ratios[section] = {
            "ratio": sec_ratio
        }
    return ratios

# print(availability_ratio(library))

# 18. Top-K доступных книг раздела
# top_k_available_by_section(library: dict, section: str, k: int) -> list[str] — до k доступных названий раздела в алфавитном порядке.
def top_k_available_by_section(library, section, k):
    books = [book['title'] for book in library.get(section, []) if book['available']]
    return sorted(books)[:k]

# print(top_k_available_by_section(library, 'Science', 2))

# 19. Нормализовать названия
# normalize_titles(library: dict) -> int — обрезать пробелы, сжать множественные
# пробелы, применить Title Case; вернуть сколько изменено.
def normalize_titles(library):
    count = 0
    for section, books in library.items():
        for book in books:
            old_name = book['title']
            new_name = " ".join(old_name.split()).title()
            if new_name != old_name:
                book['title'] = new_name
                count += 1
    return count

# print(normalize_titles(library), library)

# 20. Сравнить разделы
# compare_sections(library: dict, section1: str, section2: str) -> list[str] —
# вернуть список книг, которые есть в обоих разделах.
def compare_sections(library, section1, section2):
    set1 = {book['title'] for book in library.get(section1, [])}
    set2 = {book['title'] for book in library.get(section2, [])}
    common = set1 & set2
    # return sorted([book["title"] for sec in (section1, section2) for book in library.get(sec, []) if book["title"].lower() in common])
    titles = []
    for sec in (section1, section2):
        for book in library.get(sec, []):
            if book["title"].lower() in common and book["title"] not in titles:
                titles.append(book["title"])
    return sorted(titles)

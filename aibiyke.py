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

def count_books(library):
    count = 0
    for values in library.values():
        for title in values:
            count += 1
    return count

# print(count_books(library))

def count_available(library):
    count = 0
    for values in library.values():
        for book in values:
            if book['available']:
                count += 1
    return count

# print(count_available(library))

def find_book_section(library, title):
    for section, books in library.items():
        for book in books:
            if book['title'].lower() == title.lower():
                return section
    return 0

# print(find_book_section(library, 'a brief history of time'))

def checkout(ibrary, title):
    for i in library.values():
        for j in i:
            if j['title'] == title and j['available']:
                j['available'] = False
                return True
    return False




seating = {
    "First": [
        {"id": "1A", "occupied": True, "passenger": "Alice Kim"},
        {"id": "1C", "occupied": False, "passenger": None}
    ],
    "Business": [
        {"id": "5A", "occupied": True, "passenger": "B. Lee"},
        {"id": "5B", "occupied": False, "passenger": None},
        {"id": "6C", "occupied": True, "passenger": "Carlos Diaz"}
    ],
    "Economy": [
        {"id": "12A", "occupied": False, "passenger": None},
        {"id": "12B", "occupied": True, "passenger": "D. Singh"},
        {"id": "13C", "occupied": False, "passenger": None},
        {"id": "14A", "occupied": True, "passenger": "E. Toktogul"},
        {"id": "14B", "occupied": False, "passenger": None}
    ]
}

# 1. Подсчёт всех мест
# count_seats(seating: dict) -> int — вернуть общее число мест во всех классах.
def count_seats(seating):
    return sum(len(books) for books in seating.values())

# print(count_seats(seating))

# 2. Подсчёт свободных мест
# count_available(seating: dict) -> int — вернуть число мест с occupied == False.
def count_available(seating): 
    count = 0
    for classes, tickets in seating.items():
        for ticket in tickets:
            if not ticket['occupied']:
                count += 1
    return count

# print(count_available(seating))

# 3. Найти класс по месту
# find_seat_class(seating: dict, seat_id: str) -> str | None — вернуть название класса, где находится seat_id (без учёта регистра).
def find_seat_class(seating, seat_id):
    for classes, tickets in seating.items():
        for ticket in tickets:
            if ticket['id'].lower() == seat_id.lower():
                return classes
    return False

# print(find_seat_class(seating, '6c'))

# 4. Назначить место (чекин)
# assign_seat(seating: dict, seat_id: str, passenger: str) -> bool — если место существует и свободно, установить occupied=True и passenger.
def assign_seat(seating, seat_id, passenger):
    for classes, tickets in seating.items():
        for ticket in tickets:
            if ticket['id'] == seat_id and not ticket['occupied']:
                ticket['occupied'] = True
                ticket['passenger'] = passenger
                return True
    return False

# print(assign_seat(seating, '5B', 'Tr Ton'))

# 5. Освободить место (чекаут)
# release_seat(seating: dict, seat_id: str) -> bool — если место занято, установить occupied=False и passenger=None.
def release_seat(seating, seat_id):
    for classes, tickets in seating.items():
        for ticket in tickets:
            if ticket['id'] == seat_id and ticket['occupied']:
                ticket['occupied'] = False
                ticket['passenger'] = None
                return True
    return False

# print(release_seat(seating, '1A'), seating)

# 6. Список всех свободных мест
# list_available(seating: dict) -> list[str] — вернуть свободные seat_id во всех классах, отсортированные по алфавиту.
def list_available(seating):
    arr = []
    for classes, tickets in seating.items():
        for ticket in tickets:
            if not ticket['occupied']:
                arr.append(ticket['id'])
    return sorted(arr)

# print(list_available(seating))

# 7. Размер класса
# section_size(seating: dict, klass: str) -> int — вернуть количество мест в указанном классе (0, если нет класса).
def section_size(seating, klass):
    for classes, tickets in seating.items():
        if classes == klass:
            return len(tickets)
    return 0

# print(section_size(seating, 'Business'))

# 8. Массовое назначение по классу
# assign_section(seating: dict, klass: str, passenger_prefix: str='Гость') -> int
# — назначить всех свободных как 'Гость-1', 'Гость-2', ...; вернуть количество назначений.
def assign_section(seating, klass, passenger_prefix = 'Гость'):
    count = 0
    if klass not in seating:
        return False
    
    for ticket in seating[klass]:
        if not ticket['occupied']:
            ticket['occupied'] = True
            ticket['passenger'] = f"{passenger_prefix}-{count + 1}"
            count += 1
    return count

print(assign_section(seating, 'Economy'), seating['Economy'])

# 9. Самое длинное имя пассажира
# longest_passenger(seating: dict) -> str | None — вернуть самое длинное имя среди занятых мест (при равенстве — по алфавиту).
def longest_passenger(seating):
    passengers = [ticket['passenger'] for tickets in seating.values() for ticket in tickets if ticket['passenger']]
    if not passengers:
        return None
    return max(sorted(passengers), key = len)

# print(longest_passenger(seating))

# 10. Отчёт по рассадке
# report(seating: dict) -> dict — вернуть суммарные и по классам: {'total_seats',
# 'available', 'occupied', 'sections': {...}}.
# 11. Добавить место в класс
# add_seat(seating: dict, klass: str, seat_id: str, occupied: bool=False,
# passenger: str|None=None) -> bool — создать класс при необходимости; не допускать
# дубликаты seat_id в классе.
# 12. Удалить место по ID
# remove_seat(seating: dict, seat_id: str) -> bool — удалить место с данным ID (по
# всем классам).
# 13. Переместить место между классами
# move_seat(seating: dict, seat_id: str, to_class: str) -> bool — переместить
# запись места в другой класс, сохранив поля; избегать дубликатов.
# 14. Удалить дубликаты в классе
# dedupe_section(seating: dict, klass: str) -> int — удалить повторяющиеся seat_id,
# сохранив первое; вернуть число удалённых.
# 15. Поиск мест по префиксу
# seat_ids_starting_with(seating: dict, prefix: str, only_available: bool=False)
# -> list[str] — поиск по префиксу seat_id; опционально только свободные; вернуть
# отсортированный список.
# 16. Доля занятости по классам
# occupancy_ratio(seating: dict) -> dict[str, float] — вернуть долю occupied/total по
# каждому классу (до 2 знаков).
# 17. Top-K свободных в классе
# top_k_available(seating: dict, klass: str, k: int) -> list[str] — до k свободных
# мест в классе, отсортировано по алфавиту.
def top_k_available(seating, klass, k):
    seats = [seat['id'] for seat in seating.get(klass, []) if not seat['occupied']]
    return sorted(seats)[:k]

# print(top_k_available(seating, 'Economy', 3))

# 18. Нормализовать имена пассажиров
# normalize_passengers(seating: dict) -> int — обрезать/сжать пробелы и применить
# Title Case; вернуть, сколько имён изменено.
# 19. Подсчёт пассажиров с буквой
# count_passengers_with_letter(seating: dict, letter: str) -> int — вернуть
# количество пассажиров, у которых имя содержит данную букву.
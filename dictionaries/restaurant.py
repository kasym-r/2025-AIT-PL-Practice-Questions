menu = {
    "Starters": [
        {"id": "S01", "name": "Garlic Bread", "price": 3.50,
            "stock": 10, "available": True, "veg": True},
        {"id": "S02", "name": "Chicken Wings", "price": 6.00,
            "stock": 0, "available": False, "veg": False}
    ],
    "Mains": [
        {"id": "M01", "name": "Margherita Pizza", "price": 8.99,
            "stock": 5, "available": True, "veg": True},
        {"id": "M02", "name": "Beef Burger", "price": 9.99,
            "stock": 2, "available": True, "veg": False},
        {"id": "M03", "name": "Grilled Salmon", "price": 12.50,
            "stock": 1, "available": True, "veg": False}
    ],
    "Desserts": [
        {"id": "D01", "name": "Chocolate Cake", "price": 4.75,
            "stock": 3, "available": True, "veg": True},
        {"id": "D02", "name": "Ice Cream", "price": 3.25,
            "stock": 6, "available": True, "veg": True}
    ]
}

# 1. Подсчёт блюд
# count_items(menu: dict) -> int — вернуть количество блюд во всех категориях.
def count_items(menu):
    return sum(len(orders) for orders in menu.values()) 

print(count_items(menu))

# 2. Подсчёт доступных к заказу
# count_orderable(menu: dict) -> int — вернуть число блюд, где available == True и stock > 0.
def count_orderable(menu):
    count = 0
    for orders in menu.values():
        for order in orders:
            if order['available'] and order['stock'] > 0:
                count += 1
    return count

# print(count_orderable(menu))

# 3. Найти категорию блюда
# find_category(menu: dict, item_id: str) -> str | None — вернуть категорию, содержащую item_id.
def find_category(menu, item_id):
    for categories, orders in menu.items():
        for order in orders:
            if order['id'] == item_id:
                return categories
    return None

# print(find_category(menu, 'D02'))

# 4. Получить запись блюда
# get_item(menu: dict, item_id: str) -> dict | None — вернуть словарь блюда или None.
def get_item(menu, item_id):
    for orders in menu.values():
        for order in orders:
            if order['id'] == item_id:
                return order
    return None

# print(get_item(menu, 'M01'))

# 5. Список доступных к заказу
# list_orderable(menu: dict) -> list[tuple[str,str]] — вернуть отсортированный список (id, name) доступных блюд.
def list_orderable(menu):
    arr = []
    for orders in menu.values():
        for order in orders:
            if order['available'] and order['stock'] > 0:
                arr.append((order['id'], order['name']))
    return sorted(arr)

# print(list_orderable(menu))

# 6. Пополнить запас
# restock(menu: dict, item_id: str, amount: int) -> bool — увеличить stock на
# amount>0; если stock>0, установить available=True.
def restock(menu, item_id, amount):
    for orders in menu.values():
        for order in orders:
            if order['id'] == item_id:
                order['stock'] += amount
                if order['stock'] > 0:
                    order['available'] = True
                    return True
    return False

# print(restock(menu, 'S02', 3))

# 7. Установить флаг доступности
# set_available(menu: dict, item_id: str, is_available: bool) -> bool —
# переключить available без изменения stock.
def set_available(menu, item_id, is_available):
    for orders in menu.values():
        for order in orders:
            if order['id'] == item_id:
                order['available'] = is_available
                return True
    return False

# print(set_available(menu, 'D02', False))

# 8. Добавить блюдо в категорию
# add_item(menu: dict, category: str, item: dict) -> bool — создать категорию при
# необходимости; запретить дубликаты id в категории; валидировать поля.
# def add_item(menu, category, item):

# 9. Удалить блюдо по ID
# remove_item(menu: dict, item_id: str) -> bool — удалить первое совпадение по всем категориям.
def remove_item(menu, item_id):
    for orders in menu.values():
        for i, order in enumerate(orders):
            if order['id'] == item_id:
                orders.pop(i)
                return True
    return False

# print(remove_item(menu, 'M03'))

# 10. Изменить цену
# update_price(menu: dict, item_id: str, new_price: float) -> bool — установить неотрицательную цену new_price.
def update_price(menu, item_id, new_price):
    for orders in menu.values():
        for order in orders:
            if order['id'] == item_id and new_price > 0:
                order['price'] = new_price
                return True
    return False

# print(update_price(menu, 'M03', 87.99))

# 11. Поиск по префиксу названия
# search_by_prefix(menu: dict, prefix: str, only_orderable: bool=False) ->
# list[tuple[str,str]] — поиск по префиксу (без регистра); опция только доступных; вернуть (id, name).
def search_by_prefix(menu, prefix, only_orderable: bool = False):
    arr = []
    for orders in menu.values():
        for order in orders:
            if order['name'].lower().startswith(prefix.lower()):
                if only_orderable:
                    if order['available'] and order['stock'] > 0:
                        arr.append((order['id'], order['name']))
                else:
                    arr.append((order['id'], order['name']))
    return arr

# print(search_by_prefix(menu, 'c', True))


# 12. Только вегетарианские
# list_veg(menu: dict, only_orderable: bool=True) -> list[tuple[str,str]] —
# вернуть (id, name) блюд с veg==True, опционально только доступных.
def list_veg(menu, only_orderable: bool = True):
    arr = []
    for orders in menu.values():
        for order in orders:
            if order['veg']:
                if only_orderable:
                    if order['available'] and order['stock'] > 0:
                        arr.append((order['id'], order['name']))
                else:
                    arr.append((order['id'], order['name']))
    return arr

# print(list_veg(menu, True))

# 13. Сводка по категориям
# category_summary(menu: dict) -> dict[str, dict] — вернуть {category: {'total': int,
# 'orderable': int, 'veg': int}}.
def category_summary(menu):
    summary = {}

    for categories, orders in menu.items():
        total = len(orders)
        orderable = sum(1 for order in orders if order['available'] and order['stock'] > 0)
        veg = sum(1 for order in orders if order['veg'])

        summary[categories] = {
            "total": total,
            "orderable": orderable,
            "veg": veg
        }

    return summary
    
# print(category_summary(menu))

# 14. Самые дешёвые k блюд
# cheapest_k(menu: dict, k: int) -> list[tuple[str,str,float]] — до k самых
# дешёвых доступных блюд, отсортированных по цене и имени.
# 15. Скидка на категорию
# apply_category_discount(menu: dict, category: str, percent: float) -> int —
# снизить цену на percent; минимум 0.01; округлить до 2 знаков.
# 16. Счёт (без изменения состояния)
# compute_bill(menu: dict, order: list[tuple[str,int]], tax_rate: float=0.0,
# service_rate: float=0.0, discount_percent: float=0.0) -> dict — вернуть разбивку
# заказа и суммы; валидация количества и наличия.
# 17. Оформить заказ (меняет остатки)
# place_order(menu: dict, order: list[tuple[str,int]]) -> float — если всё валидно
# — уменьшить stock и вернуть сумму; иначе -1.0 без изменений.
# 18. Максимальный потенциал выручки
# top_revenue_item(menu: dict, category: str) -> tuple[str,str,float] | None —
# вернуть (id,name,price*stock) максимального доступного в категории, или None.
# 19. Нормализовать названия и ID
# normalize_menu(menu: dict) -> int — обрезать/сжать пробелы; Title Case для name;
# сделать id верхним регистром.
# 20. Подсчёт блюд без запаса
# count_out_of_stock(menu: dict) -> int — вернуть количество блюд, у которых stock
# == 0.
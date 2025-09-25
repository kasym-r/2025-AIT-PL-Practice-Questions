seats = [False]*15
prices = [300, 300, 300, 400, 400, 400, 500, 500, 500, 600, 600, 600, 700, 700, 700]
# prices = [700, 700, 700, 600, 600, 600, 500, 500, 500, 400, 400, 400, 300, 300, 300]

def assign_seat(name, seat_idx=None):
    if seat_idx is not None:
        if seats[seat_idx] is False:
            seats[seat_idx] = name
            return True
    else:
        for i in range(len(seats)):
            if seats[i] is False:
                seats[i] = name
                return True
    return False

def count_available():
    return sum(1 for i in range(len(seats)) if seats[i] is False)

def total_profit():
    return sum(prices[i] for i in range(len(seats)) if seats[i] is not False)

def find_person(name):
    for i, person in enumerate(seats):
        if person == name:
            return i
    return -1

def rename_client(old_name, new_name):
    idx = find_person(old_name)
    if idx != -1:
        seats[idx] = new_name
        return True
    return False

def cancel_seat(name):
    idx = find_person(name)
    if idx != -1:
        seats[idx] = False
        return True
    return False

def move_person(name, new_idx):
    old_idx = find_person(name)
    if old_idx != -1 and seats[new_idx] is False:
        seats[old_idx] = False
        seats[new_idx] = name
        return True
    return False

def cheapest_available():
    min_price, min_idx = float('inf'), -1
    for i, (seat, price) in enumerate(zip(seats, prices)):
        if seat is False and price < min_price:
            min_price = price
            min_idx = i
    return min_idx

def bulk_assign(names):
    assigned = 0
    for name in names:
        if assign_seat(name):
            assigned += 1
    return assigned

def top_spenders(m):
    clients = [(seats[i], prices[i]) for i in range(len(seats)) if seats[i] is not False]
    clients.sort(key=lambda x: (-x[1], seats.index(x[0])))
    return clients[:m]

def best_block(k):
    idx, min = -1, float('inf')
    for i in range(len(seats)-k+1):
        row, summa = True,0
        for j in range(i, i+k):
            if seats[j] != False:
                row = False
                break
            summa += prices[j]
        if row and summa<min: 
            idx = i
            min = summa
    return ([idx+r for r in range(k)], min) if idx != -1 else (-1, -1)
      
print(assign_seat("Никита"))
print(assign_seat("Мария", 5))
print(assign_seat("Азема", 13))
print(rename_client("Мария", "Алина"))
print(find_person(("Алина")))
print(cancel_seat("Никита"))
print(move_person("Азема", 7))
print(bulk_assign(["Анна", "Иван"]))
print(top_spenders(3))
print(count_available())
print(cheapest_available())
print(total_profit())
print(seats)
print(prices)
print(best_block(3))
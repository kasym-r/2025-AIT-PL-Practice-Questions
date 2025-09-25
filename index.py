def bin_to_int(binary):
    binary = binary[::-1]
    sum = 0
    for index, value in enumerate(binary):
        sum += 2**index * int(value)
    return sum

# print(bin_to_int('100'))

def int_to_bin(number):
    if number == 0:
        return 0

    binary = ''

    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2

    return binary

print(int_to_bin(15))

store = {
    "Bread": 45,
    "Milk": 65,
    "Cheese": 120,
    "Egg": 80,
    "Tea": 150,
    "Apple": 90
}

store2 = {
    "Bread": 50,
    "Cola": 80
}

def is_in_store(product):
    for name in store:
        if name == product:
            return True
    return False

def combined_max():
    for k1, v1 in store.items():
        for k2, v2 in store2.items():
            if k1 == k2:
                store[k1] = max(v1, v2)
    return store.items()
# or just store.update(store2) but it doesn't take max of two
# print(store)

def addition_pct(pct):
    for name, price in store.items():
        store[name] = round(price * (1 + pct/100), 2)
    return store.items()

def alph_sort():
    return sorted(store.keys())

print(is_in_store("Egg"))
print(combined_max())
print(addition_pct(50))
print(alph_sort())

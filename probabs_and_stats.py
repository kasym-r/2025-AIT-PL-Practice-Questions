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

# print(int_to_bin(15))

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

# print(is_in_store("Egg"))
# print(combined_max())
# print(addition_pct(50))
# print(alph_sort())


from random import randint 
arr = [randint(1, 20) for i in range(1, 21)]
print(arr)

def summa(arr):
    total = 0
    for i in arr:
        total += i
    return total 

# print(summa(arr))

def avg(arr):
    total = 0
    for i in arr:
        total += i
    return round(total / len(arr), 2)

# print(avg(arr))

def minimum(avg):
    x = float('inf')
    for i in arr:
        if i < x:
            x = i
    return x

# print(minimum(avg))

def maximum(avg):
    x = float('-inf')
    for i in arr:
        if i > x:
            x = i
    return x

# print(maximum(avg))

def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else: 
        return arr[len(arr) // 2]

# print(median(arr))


def mode(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    
    max_count = max(freq.values())

    modes = [k for k,v in freq.items() if v == max_count]

    return modes[0] if len(modes) == 1 else -1

print(mode(arr))
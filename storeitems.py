names = ["Bread", "Milk", "Cheese", "Eggs", "Tea"]
prices = [45, 65, 120, 80, 150]

def add_item(name, price):
    names.append(name)
    prices.append(price)
    return True

def count_items():
    return len(names)

def total_value():
    total = 0
    for i in prices:
        total += i
    return total

def find_item(name: str):
    for i in range(len(names)):
        if names[i] == name:
            return i
    return -1

def rename_item(old_name, new_name):
    for i in range(len(names)):
        if names[i] == old_name:
            names[i] = new_name
            return True
    return False

def reprice(name, new_price):
    idx = find_item(name)
    for i in range(len(prices)):
        prices[idx] = new_price
        return True
    return False

def remove_item(name):
    if name in names:
        idx = names.index(name)
        names.pop(idx)
        prices.pop(idx)
        return True
    return False

def max_price():
    return max(prices)

def min_price():
    return min(prices)

def top_m_names(m):
    paired = list(zip(names, prices))
    paired.sort(key = lambda x: -x[1])
    return [name for name, price in paired[:m]]

def bulk_add(new_names, new_prices):
    added = min(len(new_names), len(new_prices))
    names.extend(new_names[:added])
    prices.extend(prices[:added])
    return added

def discount_over(threshold, pct):
    count = 0
    for i, price in enumerate(prices):
        if price > threshold:
            prices[i] = round(price * (1 - pct/100), 2)
            count += 1
    return count

def names_in_range(lo, hi):
    return [names[i] for i, price in enumerate(prices) if lo <= price <= hi]

def prices_in_range(lo, hi):
    return [price for price in prices if lo <= price <= hi]

def median_price():
    sorted_prices = sorted(prices)
    n = len(sorted_prices)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_prices[mid])
    else:
        return (sorted_prices[mid - 1] + sorted_prices[mid]) / 2

def increase_price(name, pct):
    if name in names:
        idx = names.index(name)
        prices[idx] = round(prices[idx] * (1 - pct/100), 2)
        return True
    return False

def prefix_search(prefix):
    return [name for name in names if name.startswith(prefix)]
    # return [i for i in names if prefix == i[:len(prefix)]]

def sort_by_price(ascending: bool = True):
    paired = list(zip(names, prices))
    paired.sort(key = lambda x: x[1], reverse = not ascending)
    names[:] = [name for name, price in paired]
    prices[:] = [price for name, price in paired]

def avg_price():
    return sum(prices) / len(prices) if prices else 0



print(add_item("Apple", 30))
print(count_items())
print(total_value())
print(find_item("Tea"))
print(rename_item("Apple", "Yabloko"))
print(reprice("Bread", 50))
print(remove_item("Eggs"))
print(max_price())
print(min_price())
print(top_m_names(3))
print(bulk_add(["Cola"],["55"]))
print(discount_over(80, 10))
print(names_in_range(40, 100))
print(prices_in_range(100, 160))
print(prefix_search("Y"))
print(sort_by_price())
print(avg_price())
print(names, prices)




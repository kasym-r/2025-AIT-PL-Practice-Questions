def set_addition(a, b):
    a = set(a)
    b = set(b)
    return list(a.union(b))
    # for i in a:
    #     if i not in b:
    #         b.append(i)
    # return sorted(b)

def set_intersection(a, b):
    a = set(a)
    b = set(b)
    return list(a.intersection(b))
    # c = []
    # for i in a:
    #     if i in b:
    #         c.append(i)
    # return c


def set_difference(a, b):
    a = set(a)
    b = set(b)
    return sorted(list(a.difference(b)))
    # c = []
    # for i in a:
    #     if i not in b:
    #         c.append(i)
    # return sorted(c)

def has_dublicates(a):
    b = list(set(a))
    if len(b) != len(a):
        return True
    else:
        return False

arr = [1, 2, 2, 3, 3, 5]
b = [i for i in arr if arr.count(i) > 1]
print(b)

print(set_addition([1, 2, 3], [2, 3, 4, 5, 6]))
print(set_intersection([1, 2, 3], [2, 3, 4, 5, 6]))
print(set_difference([1, 2, 3, 7, 8], [2, 3, 4, 5, 6]))
print(has_dublicates([1, 2, 2, 2, 3, 4, 5]))



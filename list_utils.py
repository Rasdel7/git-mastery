def find_max(lst):
    if not lst:
        raise ValueError("Cannot find max of empty list")
    return max(lst)

def find_min(lst):
    if not lst:
        raise ValueError("Cannot find min of empty list")
    return min(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(remove_duplicates([3, 1, 2, 1, 3]))
print(flatten([1, [2, 3], [4, [5, 6]]]))
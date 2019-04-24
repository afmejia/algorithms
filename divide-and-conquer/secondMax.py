def find_second_max(lst):
    compared = find_max(lst)
    compared2 = find_max(compared[1])
    return compared2[0]

def find_max(lst):
    if (len(lst) == 1):
        compared = []
        compared.append(lst[0])
        compared.append([])
        return compared
    else:
        middle = len(lst) // 2
        compared1 = find_max(lst[:middle])
        compared2 = find_max(lst[middle:])
        if (compared1[0] > compared2[0]):
            compared1[1].append(compared2[0])
            return compared1
        else:
            compared2[1].append(compared1[0])
            return compared2

lst = [10, 4, 5, 8, 307, 2, 12, 3, 1, 6, 9, 11, 200, 300]
#lst = [50, 30, 23]
print(find_second_max(lst))
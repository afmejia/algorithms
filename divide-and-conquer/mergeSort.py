def merge (a, b):
    i = 0
    j = 0
    ans = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    while i < len(a):
        ans.append(a[i])
        i += 1

    while j < len(b):
        ans.append(b[j])
        j += 1

    return ans

def mergeSort (lst):
    if len(lst) == 1:
        return lst
    else:
        a = mergeSort(lst[: int(len(lst) / 2)])
        b = mergeSort(lst[int(len(lst) / 2) :])
        return merge(a, b)

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mergeSort(arr))
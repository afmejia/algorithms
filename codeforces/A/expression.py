#479A brute force math
def max_val_edit(a, b, c):
    ans = a + b + c
    ans = max(ans, (a + b) * c)
    ans = max(ans, a * (b + c))
    ans = max(ans, a * b * c)
    return ans

def max_val(a, b, c):
    val = a * b * c

    temp = a * b + c
    if (temp > val):
        val = temp

    temp = a * (b + c)
    if (temp > val):
        val = temp

    temp = a + b * c
    if (temp > val):
        val = temp

    temp = (a + b) * c
    if (temp > val):
        val = temp
    
    temp = a + b + c
    if (temp > val):
        val = temp

    return val

a, b, c = int(input()), int(input()), int(input())

print(max_val_edit(a, b, c))

def fixlength(x, y):
    if len(y) > len(x):
        x, y = y, x
    
    for i in range(len(x) - len(y)):
        y = '0' + y

    return x, y


def karatsuba(x, y):
    if (len(x) == 1 and len(y) == 1):
        return int(x) * int(y)
    else:
        x = str(int(x))
        y = str(int(y))
        if (len(x) % 2 == 1):
            x = '0' + x
        if (len(y) % 2 == 1):
            y = '0' + y
        if (len(y) != len(x)):
            x, y = fixlength(x, y)

        n = len(x)
        a = x[:int(n / 2)]
        b = x[int(n / 2) :]
        c = y[:int(n / 2)]
        d = y[int(n / 2) :]
        return int((10 ** n * karatsuba(a, c)) + (10 ** (n // 2) * (karatsuba(a, d) + karatsuba(b, c))) + karatsuba(b, d))

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
ans = karatsuba(str(x), str(y))
print(ans)
print(x * y)
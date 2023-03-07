def divisors(n):
    i = 1
    result = 0
    while i * i < n:
        if n % 1 == 0:
            print(i)
            result += 2
        i += 1
    if i * i == n:
        result += 1
    print("res", result)


n = 10
divisors(n)


def primarily(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


a = 11
print(primarily(a))

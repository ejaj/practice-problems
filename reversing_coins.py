def reverse_coins(n):
    result = 0
    coins = [0] * (n + 1)

    for i in range(1, n + 1):
        k = i
        while k <= n:
            coins[k] = (coins[k] + 1) % 2
            k += i
        print(coins)
        result += coins[i]
    return result


# n = 10
# print(reverse_coins(n))


def reverse_array(a):
    l = len(a)
    for i in range(l//2):
        j = l-i-1
        a[i], a[j] = a[j], a[i]
    return a

a = [1,2,3,4]
# print(reverse_array(a))
# print(a[::])
a.reverse()
print(a)
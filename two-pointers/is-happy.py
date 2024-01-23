def is_happy(n):
    def square_sum(num):
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = square_sum(n)
    return n == 1


number = 19
print(f"Is {number} a happy number? {is_happy(number)}")

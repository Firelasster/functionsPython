def divisorsCount(n):
    result = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result


def divider(a, b):
    maxCount = 0
    numbers = []
    for i in range(a, b + 1):
        numbers.append(i)
    for i in numbers:
        if len(divisorsCount(i)) > maxCount:
            maxCount = len(divisorsCount(i))
    for i in numbers:
        if len(divisorsCount(i)) == maxCount:
            print(i)


divider(1, 10)

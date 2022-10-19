def pascal(n):
    trow = [1]
    y = [0]
    for x in range(n):
        print(trow)
        trow = [left + right for left, right in zip(trow + y, y + trow)]


while True:
    try:
        n = int(input("Введите число n: "))
        if n < 1:
            raise Exception
        pascal(n)
        break
    except ValueError:
        print('Некорректное число')
    except Exception:
        print('Введите число,большее 0:')

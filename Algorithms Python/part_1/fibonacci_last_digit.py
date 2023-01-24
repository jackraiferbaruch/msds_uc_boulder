def fibonacci_last_digit(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        previous = 0
        last = 1
        for i in range(2, n+1):
            x = (previous + last) % 10
            previous = last
            last = x
    return last


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))

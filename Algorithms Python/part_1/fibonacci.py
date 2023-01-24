def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        previous = 0
        last = 1
        for i in range(2, n+1):
            x = previous + last
            previous = last
            last = x
    return last

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

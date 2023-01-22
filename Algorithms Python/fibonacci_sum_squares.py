def fibonacci_sum_squares(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        a,b = b%10, ((a+b)**2)%10
        sum = (sum + a) % 10
    return sum


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))

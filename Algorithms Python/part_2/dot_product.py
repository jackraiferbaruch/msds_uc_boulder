from itertools import permutations


def max_dot_product(a, b):
    #write your code here
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    

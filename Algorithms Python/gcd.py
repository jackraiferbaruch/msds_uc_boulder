def gcd(a, b):
    if b == 0:
        return a
    else:
        a_p = a % b
        return(gcd(b, a_p))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))

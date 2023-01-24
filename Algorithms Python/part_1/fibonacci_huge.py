def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    arr = [0, 1]
    previousMod = 0
    currentMod = 1

    for i in range(n - 1):
        tempMod = previousMod
        previousMod = currentMod % m
        currentMod = (tempMod + currentMod) % m
        arr.append(currentMod)
        if currentMod == 1 and previousMod == 0:
            index = (n % (i + 1))
            return arr[index]

    return currentMod


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))

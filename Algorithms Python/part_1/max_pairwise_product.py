def max_pairwise_product(numbers):

    return sorted(numbers)[-1] * sorted(numbers)[-2]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

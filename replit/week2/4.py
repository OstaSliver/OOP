def count_minus(input_list):
    # return sum(1 for i in input_list if i < 0)
    return len([i for i in input_list if i < 0])

x = list(map(int, input().split()))

print(count_minus(x))


def count_char_in_string(x, c):
    return [string.count(c) for string in x]

x = list(map(str, input().split()))
c = input()

result = count_char_in_string(x, c)
print(result)

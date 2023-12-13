def delete_minus(x):
    return [i for i in x if i >= 0]

x = [[1, 2, 3], [-1, -2, -3], [1, -2, 3], [-1, 2, -3]]
result = list(map(delete_minus, x))
print(result)
from itertools import permutations

numlist = list(map(int, input().split()))[:10]
all_permutations = list(permutations(numlist))
sorted_permutations = sorted(all_permutations)

for i in sorted_permutations:
    if(i[0] == 0):
        continue
    else:
        answer = "". join(map(str, i))
        print(answer)
        break

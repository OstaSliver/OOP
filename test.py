list_0 = [ x for x in input("Enter Number : ").split()]
print("list0 = " + str(list_0))
list_1 = [int(x) for x in list_0 if x.isdigit()]
print("list1 = " + str(list_1))
print("mean = " + str(sum(list_1)/len(list_1)))
print("sorted list = " + str(sorted(list_1)))
if len(list_1) % 2 == 0:
    print("median = " + str((list_1[int(len(list_1)/2)] + list_1[int(len(list_1)/2) - 1])/2))
else:
    print("median = " + str(list_1[int(len(list_1)/2)]))

print("list2 = " + str([ x for x in list_0 if not x.isdigit()]))